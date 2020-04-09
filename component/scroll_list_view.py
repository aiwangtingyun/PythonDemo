# -*- coding: utf-8 -*-
# @Time    : 2019/11/23
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import QListView, QAbstractItemView

class ScrollListView(QListView):
    ''' 自定义滚动列表视图 '''
    end_scroll = pyqtSignal()

    def __init__(self, parent=None):
        super(ScrollListView, self).__init__(parent)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.verticalScrollBar().setSingleStep(5)

        self._interval_time = QTimer()
        self._interval_time.timeout.connect(self.count_scroll_value)
        self._scroll_timer = QTimer()
        self._scroll_timer.timeout.connect(self.start_scroll)
        self._total_scroll_value = 0
        self._scroll_value_list = [i for i in range(20, 200, 6)]
        self._scroll_data = {'direction':1, 'step':0}

        self._init_ui()

    def _init_ui(self):
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical{margin:0px; width:6px; background-color: transparent; border-radius:3px;} 
            QScrollBar::handle:vertical {width:6px; border-radius:3px; background-color:#D8D8D8;}
            QScrollBar::handle:vertical:hover {background-color:#999999;}  
        """)

    def wheelEvent(self, event):
        ''' 鼠标滚动事件统计滚动的步数 '''

        self._interval_time.stop()
        self._scroll_timer.stop()
        if event.angleDelta().y() < 0:          # 往下滚动
            if self.verticalScrollBar().value() < self.verticalScrollBar().maximum():
                self._scroll_data['direction'] = -1
                self._scroll_data['step'] += 1
        else:                                   # 往上滚动
            if self.verticalScrollBar().value() <= self.verticalScrollBar().minimum():
                return
            self._scroll_data['direction'] = 1
            self._scroll_data['step'] += 1
        self._interval_time.start(45)   # 这个时间值越大，单次滚动统计的步数越多

    def count_scroll_value(self):
        ''' 根据步数设置滚动值 '''

        self._interval_time.stop()
        self._scroll_timer.stop()

        if self._scroll_data['step'] > len(self._scroll_value_list) - 1:
            self._scroll_data['step'] = 0

        if self._scroll_data['direction'] < 0:      # 往下滚动
            if self.verticalScrollBar().value() >= self.verticalScrollBar().maximum():
                self.end_scroll.emit()
                return
            self._total_scroll_value = self._scroll_value_list[self._scroll_data['step']]
            if self._total_scroll_value + self.verticalScrollBar().value() > self.verticalScrollBar().maximum():
                self._total_scroll_value = self.verticalScrollBar().maximum() - self.verticalScrollBar().value()
        else:                                       # 往上滚动
            self._total_scroll_value = -self._scroll_value_list[self._scroll_data['step']]
            if self.verticalScrollBar().value() - self._total_scroll_value < self.verticalScrollBar().minimum():
                self._total_scroll_value = -self.verticalScrollBar().value()

        self._scroll_timer.start(30)    # 这个时间设置滚动的频率，值越小越快完成
        self._scroll_data['step'] = 0

    def start_scroll(self):
        ''' 执行滚动操作 '''

        if self._total_scroll_value > 0:      # 往下滚动
            self._total_scroll_value -= 2
            scroll_value = self.verticalScrollBar().value()+self._total_scroll_value
            if scroll_value >= self.verticalScrollBar().maximum():
                scroll_value = self.verticalScrollBar().maximum()
                self._scroll_timer.stop()
            self.verticalScrollBar().setSliderPosition(scroll_value)
        elif self._total_scroll_value < 0:   # 往上滚动
            self._total_scroll_value += 2
            scroll_value = self.verticalScrollBar().value()+self._total_scroll_value
            if scroll_value <= self.verticalScrollBar().minimum():
                scroll_value = self.verticalScrollBar().minimum()
                self._scroll_timer.stop()
            self.verticalScrollBar().setSliderPosition(scroll_value)
