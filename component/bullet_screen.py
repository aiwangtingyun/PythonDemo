# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/03/13


from PyQt5.QtWidgets import QWidget, QLabel

from component.circle_image import CircleImage


class NobilityBulletScreen(QWidget):
    '''贵族弹幕'''

    def __init__(self, parent=None):
        super(NobilityBulletScreen, self).__init__(parent)
        self.resize(222, 24)
        self.bg_image = QLabel(self)
        self.head_image = CircleImage(22, 22)
        self.noble_tag = QLabel(self)
        self.lb_name = QLabel(self)
        self.lb_content = QLabel(self)

        self.test_widget()

    def test_widget(self):
        info = {
            'background': '',
            'head_image': '',
            'noble_tag': '',
            'name': '',
            'content': ''
        }
        self.set_info(info)

    def set_info(self, info):
        background = info.get('background')
        head_image = info.get('head_image')
        noble_tag = info.get('noble_tag')
        name = info.get('name')
        content = info.get('content')


class NobilityEnterRoom(QWidget):
    '''贵族进房'''

    def __init__(self, parent=None):
        super(NobilityEnterRoom, self).__init__(parent)
