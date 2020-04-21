
import os
from PyQt5.QtCore import QFile, QIODevice


# 工程根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 图片根目录
IMAGE_DIR = os.path.join(ROOT_DIR, 'images')
# qss根目录
QSS_DIR = os.path.join(ROOT_DIR, 'qss')
# qml根目录
QML_DIR = os.path.join(ROOT_DIR, 'qmls')


def get_style_sheet(name='', way='python'):
    """获取qss样式表"""
    style_sheet_file = os.path.join(QSS_DIR, name)
    if os.path.exists(style_sheet_file):
        try:
            if way == 'python':
                file = open(style_sheet_file, 'r')
                return file.read()
            elif way == 'qt':
                file = QFile(style_sheet_file)
                if file.open(QIODevice.ReadOnly | QIODevice.Text):
                    return str(file.readAll(), encoding='utf-8')
        except Exception as e:
            print('[Exception] read qss file failed : ', e)


def get_qml_path(name=''):
    """获取qml文件路径"""
    qml_path = os.path.join(QML_DIR, name)
    if os.path.exists(qml_path):
        return qml_path
    else:
        return ''
