# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

import os

import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QWidget, QLabel, QOpenGLWidget, QApplication


class MoviePlayer(QWidget):

    def __init__(self, parent=None, width=640, height=480):
        super(MoviePlayer, self).__init__(parent)
        self.resize(width, height)
        self.setWindowFlags(self.windowFlags() | Qt.NoDropShadowWindowHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.movie_label = QLabel(self)
        self.movie_label.setGeometry(0, 0, width, height)
        self.movie_label.setAlignment(Qt.AlignCenter)
        self.movie_label.setStyleSheet('QLabel{background-color:transparent;}')

        self.movie = QMovie(self)
        self.movie.frameChanged.connect(self.on_frame_changed)
        print(QMovie.supportedFormats())

        self.loop_count = 0
        self.max_loop_count = 1

    def resizeEvent(self, event):
        self.movie_label.setGeometry(self.geometry())

    def set_movie_path(self, path=''):
        ''' 设置动画路径 '''
        if not os.path.exists(path):
            return
        self.movie.setFileName(path)

    def start_movie(self):
        self.movie.start()

    def stop_movie(self):
        self.movie.stop()

    def on_frame_changed(self, frame):
        if frame == self.movie.frameCount() - 1:
            self.loop_count += 1
            if self.loop_count == self.max_loop_count:
                self.movie.stop()
        cur_pixmap = self.movie.currentPixmap()
        cur_pixmap = cur_pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.movie_label.setPixmap(cur_pixmap)

        # 保存帧动画
        # self.save_frame(frame, cur_pixmap)

    def save_frame(self, frame, picture):
        picture.save('../webp/{}.png'.format(frame), 'png')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Demo')
    window.resize(750, 400)

    window.player = MoviePlayer(window)
    window.player.setGeometry(window.geometry())
    movie_path = '../images/webp/pk_start_anim_launch.webp'
    window.player.set_movie_path(movie_path)
    window.player.start_movie()
    window.show()

    widget = QWidget()
    widget.show()

    sys.exit(app.exec_())
