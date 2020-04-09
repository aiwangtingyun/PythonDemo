from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class ClickableSlider(QSlider):
    '''
    自定义Slider，实现点击任何位置都可以精确跳转的功能
    '''

    def __init__(self, *args, **kwargs):
        super(ClickableSlider, self).__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        super(ClickableSlider, self).mousePressEvent(event)

        if event.button() == Qt.LeftButton and not self.isSliderDown():
            pos = self.sliderPosition()
            if self.orientation() == Qt.Horizontal:
                pos = (self.maximum() - self.minimum()) * event.x() / self.width()
            else:
                pos = (self.maximum() - self.minimum()) * (self.height() - event.y()) / self.height()
            self.setSliderPosition(int(pos))
