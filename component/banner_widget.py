# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/03/10

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont, QFontMetrics, QPixmap, QPainter, QBrush, QImage
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from component.circle_image import CircleImage


class WorldBannerWidget(QWidget):
    '''世界横幅'''

    def __init__(self, parent=None):
        super(WorldBannerWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(700, 70)

        self.background_img = QLabel(self)
        self.head_image = CircleImage(self, 32, 32)
        self.sender_name = QLabel(self)
        self.sender_name.setObjectName('bannerSener')
        self.receiver_name = QLabel(self)
        self.receiver_name.setObjectName('bannerReceiver')
        self.lb_text = QLabel(self)
        self.lb_text.setObjectName('bannerNormalText')
        self.gift_image = QLabel(self)
        self.gift_count = QLabel(self)
        self.gift_count.setObjectName('bannerGiftCount')
        self.btn_onlook = QPushButton(self)
        self.btn_onlook.setObjectName('bannerOnlookBtn')

        self.test_widget()

    def test_widget(self):
        '''功能测试'''
        info = {
            'background': 'image/word_banner_1.png',
            'portrait': 'image/user_icon.png',
            'sender': '聪明的王廷云哈哈哈哈哈哈',
            'receiver': '帅气的王廷云哈哈哈哈哈哈',
            'gift_image': 'image/gift.png',
            'gift_count': '1234'
        }
        self.set_info(info)

    def set_info(self, info):
        bg_image = info.get('background')
        head_url = info.get('portrait')
        sender_name = info.get('sender')
        receiver_name = info.get('receiver')
        gift_image_url = info.get('gift_image')
        gift_count = 'x' + str(info.get('gift_count'))
        position_x = 2

        font = QFont('Microsoft YaHei')
        font.setPixelSize(14)
        font_metric = QFontMetrics(font)

        # 背景
        image = QPixmap(bg_image)
        self.background_img.setGeometry(0, self.height() - image.height(), image.width(), image.height())
        self.background_img.setStyleSheet('''
            QLabel{background: url(''' + bg_image + ''') left bottom no-repeat transparent;}
        ''')

        # 头像
        self.head_image.set_image(QPixmap(head_url))
        self.head_image.move(position_x, self.height() - 32 - 2)
        position_x = 56

        # 送礼者
        name_len = font_metric.boundingRect(sender_name).width()
        if name_len > 120:
            sender_name = font_metric.elidedText(sender_name, Qt.ElideRight, 120)
            name_len = font_metric.boundingRect(sender_name).width()
        self.sender_name.setGeometry(position_x, self.height() - 9 - 20, name_len, 20)
        self.sender_name.setText(sender_name)
        position_x += name_len

        # 打赏
        position_x += 5
        self.lb_text.setGeometry(position_x, self.height() - 9 - 20, 30, 20)
        self.lb_text.setText('打赏')
        position_x += self.lb_text.width()

        # 送礼者
        position_x += 5
        name_len = font_metric.boundingRect(receiver_name).width()
        if name_len > 120:
            receiver_name = font_metric.elidedText(receiver_name, Qt.ElideRight, 120)
            name_len = font_metric.boundingRect(receiver_name).width()
        self.receiver_name.setGeometry(position_x, self.height() - 9 - 20, name_len, 20)
        self.receiver_name.setText(receiver_name)
        position_x += name_len

        # 礼物
        position_x += 15
        self.gift_image.setStyleSheet('''
            QLabel{background: url(''' + gift_image_url + ''') center bottom no-repeat transparent;}
        ''')
        image = QPixmap(gift_image_url)
        self.gift_image.setGeometry(position_x, self.height() - image.height(), image.width(), image.height())
        position_x += image.width()

        # 礼物数量
        position_x += 15
        font.setFamily('Segoe UI Black')
        font.setPixelSize(26)
        font_metric = QFontMetrics(font)
        text_len = font_metric.boundingRect(gift_count).width()
        self.gift_count.setGeometry(position_x, self.height() - 8 - 26, text_len, 26)
        self.gift_count.setText(gift_count)
        position_x += text_len

        # 立即围观按钮
        position_x += 15
        self.btn_onlook.setGeometry(position_x, self.height() - 6 - 24, 80, 24)
        self.btn_onlook.setText('立即围观')

class OpenNobilityBannerWidget(QWidget):
    '''开通贵族横幅'''

    def __init__(self, parent=None):
        super(OpenNobilityBannerWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(502, 71)

        self.background_img = QLabel(self)
        self.head_image = CircleImage(self, 32, 32)
        self.opener_name = QLabel(self)
        self.opener_name.setObjectName('bannerOpener')
        self.room_id = QLabel(self)
        self.room_id.setObjectName('bannerNormalText')
        self.open_type = QLabel(self)
        self.open_type.setObjectName('bannerOpenType')
        self.btn_onlook = QPushButton(self)

        self.test_widget()

    def test_widget(self):
        '''功能测试'''
        info = {
            'background': 'image/bg_open_duke.png',
            'portrait': 'image/user_icon.png',
            'opener': '聪明的王廷云王廷云',
            'room_id': '11019',
            'open_type': '猎游贵族·公爵',
            'btn_onlook': 'image/onlook_now.png'
        }
        self.set_info(info)

    def set_info(self, info):
        bg_image = info.get('background')
        head_url = info.get('portrait')
        opener_name = info.get('opener')
        room_id = info.get('room_id')
        open_type = info.get('open_type')
        btn_onlook = info.get('btn_onlook')
        position_x = 3

        font = QFont('Microsoft YaHei')
        font.setPixelSize(14)
        font_metric = QFontMetrics(font)

        # 背景
        image = QPixmap(bg_image)
        self.background_img.setGeometry(0, self.height() - image.height(), image.width(), image.height())
        self.background_img.setStyleSheet('''
            QLabel{background: url(''' + bg_image + ''') left bottom no-repeat transparent;}
        ''')

        # 头像
        self.head_image.setGeometry(position_x, 19, 32, 32)
        self.head_image.set_image(QPixmap(head_url))
        position_x = 56

        # 开通者
        text_len = font_metric.boundingRect(opener_name).width()
        if text_len > 90:
            opener_name = font_metric.elidedText(opener_name, Qt.ElideRight, 90)
            text_len = font_metric.boundingRect(opener_name).width()
        self.opener_name.setGeometry(position_x, 26, text_len, 16)
        self.opener_name.setText(opener_name)
        position_x += text_len

        # 开通的房间
        position_x += 5
        room_text = '在房间{}开通'.format(room_id)
        text_len = font_metric.boundingRect(room_text).width()
        self.room_id.setGeometry(position_x, 26, text_len, 16)
        self.room_id.setText(room_text)
        position_x += self.room_id.width()

        # 开通类型
        text_len = font_metric.boundingRect(open_type).width()
        self.open_type.setGeometry(position_x, 26, text_len, 16)
        self.open_type.setText(open_type)
        position_x += text_len

        # 立即围观按钮
        position_x += 23
        self.btn_onlook.setStyleSheet('''
            QPushButton{background: url(''' + btn_onlook + ''') center center no-repeat transparent;
                        border:none;}
        ''')
        self.btn_onlook.setGeometry(355, 23, 82, 26)
