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
    if crash_dll:
        print("Load lib sucess....")
        ret = crash_dll.install_crashrpt("lieyou", "1.2.3", "./")
        if ret == 0:
            print('------ install success ---------')
            crash_dll.test_crashrpt()
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
