# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/03/10
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication


class ImageScale(QWidget):

    def __init__(self):
        super(ImageScale, self).__init__()

    def scale_image(self, src_img_path, width, height):
        pixmap = QPixmap(src_img_path)
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap.save(src_img_path, "PNG")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    scaler = ImageScale()
    image_path = '../images/logo.png'
    scaler.scale_image(image_path, 20, 20)

    sys.exit(app.exec_())
