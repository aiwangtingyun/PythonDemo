# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/04/14

import threading

num = 0
lock = threading.Lock()


def changed_num(n):
    global num
    num = n
    print('num is ------ ', num, threading.current_thread().name)


def thread_run(num):
    for i in range(10):
        lock.acquire()
        try:
            changed_num(i)
        finally:
            lock.release()


if __name__ == '__main__':
    thread_1 = threading.Thread(target=thread_run, args=(5,))
    thread_2 = threading.Thread(target=thread_run, args=(10,))

    thread_1.start()
    thread_2.start()
