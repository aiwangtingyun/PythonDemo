
import os
from PyQt5.QtCore import QFile, QIODevice


# 工程根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 图片根目录
IMAGE_DIR = os.path.join(ROOT_DIR, 'images')
# qss根目录
QSS_DIR = os.path.join(ROOT_DIR, 'qss')


def get_style_sheet(name=''):
    # python way
    style_sheet_file = os.path.join(QSS_DIR, name)
    if os.path.exists(style_sheet_file):
        try:
            file = open(style_sheet_file, 'r')
            return file.read()
        except Exception as e:
            print('read file failed : ', e)


def get_style_sheet_2(name=''):
    # Qt way
    style_sheet_file = os.path.join(QSS_DIR, name)
    if os.path.exists(style_sheet_file):
        try:
            file = QFile(style_sheet_file)
            if file.open(QIODevice.ReadOnly | QIODevice.Text):
                return str(file.readAll(), encoding='utf-8')
        except Exception as e:
            print('read file failed : ', e)
