# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/04/03

import os

if __name__ == '__main__':
    path = '/python/demo/test.py'
    print(__file__)
    print(os.path.split(path))
    print(os.path.dirname(path), os.path.basename(path))
    print(os.path.dirname(os.path.dirname(path)))
    print(os.path.dirname(os.path.dirname(os.path.dirname(path))))
    print(os.path.join('/python', 'demo', 'test.py'))
    print(os.path.splitext('/python/demo/test'))
    print(os.path.splitdrive('D:\\python\\demo\\test.py'))
    print(os.path.islink('C:\\Users\\Administrator\\Desktop\\猎游直播PC客户端'))
    print(os.path.isfile('C:\\Users\\Administrator\\Desktop\\猎游直播PC客户端'))
    print(os.path.isdir('C:\\Users\\Administrator\\Desktop'))
    print(os.path.isabs('test.py'))
    print(os.path.ismount('D:'))
    print(os.path.abspath('test.py'))
    print(os.path.realpath('C:/Users/Administrator/Desktop'))
    print(os.path.normpath('C:/Users/Administrator/Desktop'))
    print(__file__)
    file = 'C:\\Users\\Administrator\\Desktop\\777.exe'
    print(os.path.getsize(file))
    print(os.path.getctime(file))
    print(os.path.getatime(file))
    print(os.path.getmtime(file))
