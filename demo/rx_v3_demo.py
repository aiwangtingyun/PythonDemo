# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/04/28

import sys
from rx import of, create


def push_five_strings(observer, scheduler):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Esilon")
    observer.on_completed()


def get_input(observer):
    while True:
        line = sys.stdin.readline()
        if line == '\n':
            observer.on_completed()
            break
        observer.on_next(line)


if __name__ == '__main__':
    # 通过 create 创建 Observable
    # observable = create(push_five_strings)

    # 通过 of 创建 Observable
    observable = of("Alpha", "Beta", "Gamma", "Delta", "Esilon")

    # 启动
    observable.subscribe(
        on_next=lambda i: print("Received {0}".format(i)),
        on_error=lambda e: print("Error occured {0}".format(e)),
        on_completed=lambda: print("Done!")
    )
