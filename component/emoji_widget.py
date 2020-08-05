import sys
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QRect, QVariant, QAbstractListModel
from PyQt5.QtGui import QPainter, QBrush, QColor, QPainterPath, QImage, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QAbstractItemView, QLabel, QStyledItemDelegate, QStyle, \
    QStackedWidget, QToolButton

from center.icon_center import IconCenter
from center.signal_center import SignalCenter
from tools import emoji_tool


class EmojiWidget(QWidget):

    def __init__(self, parent=None):
        super(EmojiWidget, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        self._shadow_depth = 12
        self._width = 384
        self._height = 216 + 12

        self.setFixedWidth(self._width + self._shadow_depth * 2)
        self.setFixedHeight(self._height + self._shadow_depth * 2)
        self.widget = BackWidget(self)
        self.widget.setGeometry(self._shadow_depth, self._shadow_depth, self._width, self._height)

        self.stackWidget = QStackedWidget(self.widget)
        self.stackWidget.setGeometry(8, 4, self.widget.width() - 8, self.widget.height() - 44 - 6)
        self.init_tab_button()

        emoji_listview = EmojiListView()
        emoji_listview.emoji_click.connect(self.on_emoji_click)
        data_list = []
        for item in emoji_tool.get_all_emoji():
            data_list.append({
                'path': IconCenter().res_path('emoji/{}.png'.format(item[1])),
                'code': item[0]
            })
        emoji_listview.init_data(data_list)
        emoji_listview.setStyleSheet("QWidget{border-radius:4px;}")
        emoji_listview.set_fixed_size(self.stackWidget.width(), self.stackWidget.height())
        self.stackWidget.addWidget(emoji_listview)

    def init_tab_button(self):
        '''自定义tab控件按钮'''

        btn_style = 'QToolButton{background: url([icon]) center center no-repeat [color]; border: none;' \
                    'border-bottom-left-radius: 4px;}'
        emoji_btn_style = btn_style.replace('[icon]', IconCenter().res_path('emoji/emoji_tab.png'))
        like_btn_style = btn_style.replace('[icon]', IconCenter().res_path('emoji/like_tab.png'))

        self.emoji_style_select = emoji_btn_style.replace('[color]', '#ffffff')
        self.emoji_style_unselect = emoji_btn_style.replace('[color]', '#F3F3F3')
        self.like_emoji_select = like_btn_style.replace('[color]', '#ffffff')
        self.like_emoji_unselect = like_btn_style.replace('[color]', '#F3F3F3')

        self.emoji_btn = QToolButton(self.widget)
        self.emoji_btn.setCursor(Qt.PointingHandCursor)
        self.emoji_btn.clicked.connect(self.on_emoji_tab_click)
        self.emoji_btn.setGeometry(0, self.widget.height() - 44, 56, 36)
        self.emoji_btn.setStyleSheet(self.emoji_style_select)

        # self.like_btn = QToolButton(self.widget)
        # self.like_btn.setCursor(Qt.PointingHandCursor)
        # self.like_btn.clicked.connect(self.on_like_tab_click)
        # self.like_btn.setGeometry(56, self.widget.height() - 44, 56, 36)
        # self.like_btn.setStyleSheet(self.like_emoji_unselect)

    def on_emoji_tab_click(self):
        self.emoji_btn.setStyleSheet(self.emoji_style_select)
        self.like_btn.setStyleSheet(self.like_emoji_unselect)
        self.stackWidget.setCurrentIndex(0)

    def on_emoji_click(self, data):
        SignalCenter().emoji_item_click.emit(data)


class EmojiListView(QWidget):
    emoji_click = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(EmojiListView, self).__init__(parent)

        self._listview = QListView(self)
        self._listview.clicked.connect(self._on_click)
        self._listview.setSpacing(0)
        self._listview.setFixedWidth(380)
        self._listview.setFocusPolicy(Qt.NoFocus)
        self._listview.setMouseTracking(True)
        self._listview.setUniformItemSizes(True)
        self._listview.setLayoutMode(QListView.Batched)
        self._listview.setBatchSize(100)
        self._listview.setSelectionMode(QListView.NoSelection)
        self._listview.setTextElideMode(Qt.ElideRight)
        self._listview.setViewMode(QListView.IconMode)
        self._listview.setResizeMode(QListView.Adjust)
        self._listview.setIconSize(QSize(24, 24))
        self._listview.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self._model = EmojiModel()
        self._delegate = EmojiDelegate()
        self._listview.setModel(self._model)
        self._listview.setItemDelegate(self._delegate)
        self._listview.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical{margin-top:6px; width:6px; background-color: transparent; border-radius:3px;} 
            QScrollBar::handle:vertical {width:6px; border-radius:3px; background-color:#D8D8D8;}
            QScrollBar::handle:vertical:hover {background-color:#999999;}  
            QScrollBar::sub-page:vertical,QScrollBar::add-page:vertical{background: transparent;}
            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical{border-radius:4px;}
        """)

        self.openAllEditor = True

    def set_fixed_size(self, width, height):
        self._listview.setFixedSize(width, height)

    def init_listener(self):
        self._delegate.data_change.connect(self.refresh_item)

    def refresh_item(self, index):
        self._model.dataChanged.emit(index, index)

    def set_spacing(self, spacing):
        self._listview.setSpacing(spacing)

    def set_item_size(self, size):
        self._delegate.set_size(size)

    def get_datas(self):
        return self._model.icon_cache

    def init_data(self, emoji_list):
        self._model.setIcon(emoji_list)
        self._model.reset(emoji_list)

        if self.openAllEditor:
            for row in range(self._model.rowCount()):
                self._listview.openPersistentEditor(self._model.index(row))

    def _on_click(self, index):
        data = index.model().get(index.row())
        if data:
            self.emoji_click.emit(data)


class EmojiModel(QAbstractListModel):

    def __init__(self, roles=set()):
        super(EmojiModel, self).__init__()
        self._roleName = roles
        self._data = list()

        self._roleName = ('path')

        self.icon_cache = None

    def reset(self, data):
        self.beginResetModel()
        self._data = data
        self.endResetModel()

    def clear(self):
        self.reset([])

    def data(self, index, role=None):
        row = index.row()
        if row >= len(self._data):
            return QVariant()
        item = self._data[row]
        if role in self.roleNames().keys():
            return item.get(self.roleNames()[role], QVariant())
        elif role is None:
            return item
        else:
            return QVariant()

    def get(self, row, roleName=None):
        if row < 0 or row >= len(self._data):
            return None
        if roleName in self.roleNames().keys():
            return self._data[row].get(roleName)
        elif roleName is None:
            return self._data[row]
        else:
            return None

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    def setData(self, index, value, role=None):
        if not index.isValid() or role not in self.roleNames().keys():
            return False
        row = index.row()
        if row >= len(self._data):
            return False
        if role is None and self._data[row] != value:
            self._data[row] = value
            self.dataChanged.emit(index, index)
            return True
        if role in self.roleNames().keys():
            item = self._data[row]
            if item[self.roleNames()[role]] != value:
                item[self.roleNames()[role]] = value
                self.dataChanged.emit(index, index)
                return True
        return False

    def setIcon(self, icon_list):
        self.icon_cache = icon_list


class EmojiDelegate(QStyledItemDelegate):
    data_change = pyqtSignal(QVariant)

    def __init__(self, parent=None, editable=True):
        super(EmojiDelegate, self).__init__(parent)

        self.editable = editable
        self.size = QSize(36, 36)

    def sizeHint(self, options, index):
        return self.size

    def set_size(self, size):
        self.size = size

    def createEditor(self, parent, option, index):
        editor = EmojiEditor(parent, self.editable)

        return editor

    def destroyEditor(self, editor, index):
        editor.disconnect()
        editor.deleteLater()

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def setEditorData(self, editor, index):
        editor.set_item(index.model().get(index.row()))

    def setModelData(self, editor, model, index):
        pass

    def refresh_index(self, index):
        self.data_change.emit(index)

    def paint(self, painter, option, index):
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        if option.state & QStyle.State_HasFocus or option.state & QStyle.State_MouseOver:
            painter.setBrush(QColor('#1f000000'))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(option.rect, 4, 4)

        data = index.model().get(index.row())
        # name = data.get('name')
        # if name:
        #     url = data.get('url')
        #     icon = IconCenter().cache_icon(url, QSize(40, 40))
        #     if icon.isNull():
        #         icon = IconCenter().default_size_icon(40, 40)
        #         IconCenter().download_img(url, success=lambda: self.refresh_index(index))
        #     rect = option.rect
        #     img_rect = QRect(rect.x() + 25,
        #                      rect.y() + 15, 40, 40)
        #     painter.drawImage(img_rect, icon)
        #     pen = QPen()
        #     pen.setColor(QColor('#FF666666'))
        #     painter.setPen(pen)
        #     name_rect = QRect(rect.x(), rect.y() + 58, rect.width(), 20)
        #     painter.drawText(name_rect, Qt.AlignCenter, name)
        # else:
        #     rect = option.rect
        #     img_rect = QRect(rect.x() + 6, rect.y() + 6, 24, 24)
        #     path = data.get('path')
        #     painter.drawImage(img_rect, QImage(path))
        rect = option.rect
        img_rect = QRect(rect.x() + 6, rect.y() + 6, 24, 24)
        path = data.get('path')
        painter.drawImage(img_rect, QImage(path))


class EmojiEditor(QWidget):

    def __init__(self, parent, editable=True):
        super(EmojiEditor, self).__init__(parent)

        self.setFixedWidth(24)
        self.setFixedHeight(24)
        # 用来显示gif动画
        self.label = QLabel(self)

    def set_item(self, data):
        path = data.get('path')


class BackWidget(QWidget):

    def __init__(self, parent=None):
        super(BackWidget, self).__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        painter.setBrush(QBrush(QColor('#FFFFFF')))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, self.width(), self.height() - 8, 4, 4)

        path = QPainterPath()
        path.moveTo(20, self.height() - 8)
        path.lineTo(30, self.height())
        path.lineTo(40, self.height() - 8)
        painter.drawPath(path)

        painter.setBrush(QBrush(QColor('#F3F3F3')))
        painter.drawRoundedRect(0, self.height() - 36 - 8, self.width(), 36, 4, 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = EmojiWidget()
    widget.move(300, 200)
    widget.show()

    sys.exit(app.exec_())
