from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QLabel


class RippleWidget(QWidget):

    def __init__(self, parent=None, width=80, height=80):
        super(RippleWidget, self).__init__(parent)
        self.resize(width, height)
        self.color = QColor('#ffffff')
        self.setObjectName('WaveWidget')
        self.setStyleSheet('QWidget{background-color:transparent;}')

        self.wave_timer = QTimer()
        self.wave_timer.timeout.connect(self.time_out)
        self.wave_timer.setInterval(70)

        self.circle_list = []
        self.alpha_list = []
        self.radius_list = []
        self.start_flag_list = []
        self.wave_space = 16
        self.circle_geometry = QRect((self.width() - 16) / 2, (self.height() - 16) / 2, 16, 16)
        self.max_radius = width // 16 * 16 - 16
        self.ripple_count = width // 16

        self._set_ripple_count(self.ripple_count)
        self.init_ripple()

    def _set_ripple_count(self, count=3):
        '''更改波纹数量'''

        if not isinstance(count, int) or count <= 0:
            return

        for i in range(count):
            label = QLabel(self)
            label.setGeometry(self.circle_geometry)
            # label.hide()
            self.circle_list.append(label)
            self.alpha_list.append(240)
            self.radius_list.append(0)
            self.start_flag_list.append(False)

    def set_color(self, color):
        '''更改波纹颜色'''

        if not isinstance(color, QColor):
            return
        self.color = color

    def start_ripple_animation(self):
        '''启动波纹'''
        for item in self.circle_list:
            item.show()
        self.wave_timer.start()

    def stop_ripple_animation(self):
        '''关闭波纹'''
        for item in self.circle_list:
            item.hide()
        self.wave_timer.stop()

    def init_ripple(self):
        self.time_out()
        if self.radius_list[0] < 48:
            QTimer.singleShot(50, self.init_ripple)

    def reset_time_out(self):
        self.time_out()
        if self.radius_list[0] >= 48:
            self.reset_timer.stop()

    def time_out(self):
        # 第一个波纹先走
        self.count_alpht_radius(0)
        self.wave(0)

        # 后面的波纹根据前面波纹走的间隔距离再走
        for index in range(1, len(self.circle_list)):
            if not self.start_flag_list[index] and self.radius_list[index-1] >= self.wave_space:
                self.start_flag_list[index] = True
            if self.start_flag_list[index]:
                self.count_alpht_radius(index)
                self.wave(index)

    def count_alpht_radius(self, index):
        '''计算alpht和radius值'''

        self.alpha_list[index] -= 240 // (self.max_radius//2)
        self.radius_list[index] += 2
        x = self.circle_geometry.x() - self.radius_list[index] / 2
        y = self.circle_geometry.y() - self.radius_list[index] / 2
        w = self.circle_geometry.width() + self.radius_list[index]
        h = self.circle_geometry.height() + self.radius_list[index]
        self.circle_list[index].setGeometry(x, y, w, h)
        if self.radius_list[index] >= self.max_radius or self.alpha_list[index] <= 0:
            self.alpha_list[index] = 240
            self.radius_list[index] = 0
            self.circle_list[index].setGeometry(self.circle_geometry)

    def wave(self, index):
        '''开始波动'''

        rgba = '%d,%d,%d,%d' % (self.color.red(), self.color.green(), self.color.blue(), self.alpha_list[index])
        radius = self.circle_list[index].width() / 2
        style_sheet = 'QLabel{background-color:rgba(%s); border-radius:%d;}' % (rgba, radius)
        self.circle_list[index].setStyleSheet(style_sheet)
