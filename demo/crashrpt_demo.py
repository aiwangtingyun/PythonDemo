#!/bin/python3
# -*- coding: utf-8 -*-

import os
import ctypes
import time
from ctypes import *

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from center.config_center import LIB_DIR


def install_dll():
    lib_path = os.path.join(LIB_DIR, "CrashRpt1402.dll")
    crash_dll = ctypes.cdll.LoadLibrary(lib_path)

    app_name = c_char_p(bytes("lieyou", "utf-8"))
    app_version = c_char_p(bytes("1.2.4", "utf-8"))
    crp_path = c_char_p(bytes("./crash_rpt", "utf-8"))
    report_url = c_char_p(bytes("http://14.152.59.165/crashfix/index.php/crashReport/uploadExternal", "utf-8"))

    # 安装
    if crash_dll:
        print("Load lib sucess....")
        ret = crash_dll.install_crashrpt(app_name, app_version, crp_path, report_url)
        if ret == 0:
            print('------ install success ---------')

    # 测试
    # crash_dll.test_crashrpt()

    # 卸载
    ret = crash_dll.uninstall_crashrpt()
    if ret == 0:
        print('------ uninstall success ---------')


if __name__ == "__main__":
    install_dll()
    # app = QApplication(sys.argv)
    #
    # window = QWidget()
    #
    # btn = QPushButton(window)
    # btn.resize(window.size())
    # btn.clicked.connect(install_dll)
    #
    # window.show()
    #
    # code = app.exec_()
    # sys.exit(code)
