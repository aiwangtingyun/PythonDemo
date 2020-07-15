import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class CountDownAnimate(QWidget):
    def __init__(self, parent=None):
        super(CountDownAnimate, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(100, 50)
        self.time_label = QLabel(self)
        self.time_label.setGeometry(35, 0, 50, 50)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setText("3")
        self.time_label.setStyleSheet("""
            QLabel{font-size: 40px; color: yellow; font-weight: bold;}
        """)

        self.count_timer = QTimer()
        self.count_timer.setInterval(1000)
        self.count_timer.timeout.connect(self.count_down)
        self.count = 3

    def count_start(self):
        self.show()
        self.count_timer.start()

    def count_down(self):
        if self.count == 0:
            self.count_timer.stop()
            self.hide()
            self.time_label.setText("3")

        self.count -= 1
        self.time_label.setText("{}".format(self.count))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = CountDownAnimate()
    widget.count_start()

    sys.exit(app.exec_())
