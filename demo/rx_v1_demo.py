# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/04/28

import sys
from rx import Observable, Observer


def get_input_demo():
    """
    从输入框获取输入，从第 10 次输入开始取前5次的输入，打印出来
    """
    def get_input(observer):
        count = 0
        while True:
            count += 1
            print("请输入第{}条数据：".format(count), sep=' ')
            line = sys.stdin.readline()
            if line == '\n':
                observer.on_completed()
                break
            observer.on_next(line)

    method = 1
    if method == 1:
        # 方式一
        Observable.create(get_input) \
            .skip(10) \
            .take(5) \
            .map(lambda line: "接收的数据为：{}".format(line)) \
            .subscribe(print)
    elif method == 2:
        # 方式二
        Observable.create(get_input) \
            .skip(10) \
            .take(5) \
            .subscribe(lambda line: print("接收的数据为：{}".format(line)))


def test_create_operator():
    """
    测试 create 操作符
    """
    from rx import Observable, Observer

    def push_five_strings(observer):
        """
        订阅函数，用于调用观察者的 on_next、on_completed、on_error 方法
        """
        observer.on_next("Alpha")
        observer.on_next("Beta")
        observer.on_next("Gamma")
        observer.on_next("Delta")
        observer.on_next("Epsilon")
        observer.on_completed()

    class PrintObserver(Observer):
        """
        继承Observer重写观察者的 on_next、on_completed、on_error 方法
        """
        def on_next(self, value):
            print("Received {0}".format(value))

        def on_completed(self):
            print("Done!")

        def on_error(self, error):
            print("Error Occurred: {0}".format(error))

    # 创建 Observable 对象
    source = Observable.create(push_five_strings)

    # 订阅观察者
    source.subscribe(PrintObserver())


def test_from_operator():
    """
    测试 create 操作符
    """
    from rx import Observable, Observer

    class PrintObserver(Observer):
        """
        继承Observer重写观察者的 on_next、on_completed、on_error 方法
        """
        def on_next(self, value):
            print("Received {0}".format(value))

        def on_completed(self):
            print("Done!")

        def on_error(self, error):
            print("Error Occurred: {0}".format(error))

    # 创建 Observable 对象
    source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

    # 订阅观察者
    source.subscribe(PrintObserver())


def simplify_subscribe():
    """
    简化 subscribe 订阅函数
    """
    from rx import Observable, Observer

    # 创建 Observable 对象
    source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

    # 订阅观察者，on_next、on_completed、on_error 可选的
    source.subscribe(on_next=lambda value: print("Received {0}".format(value)),
                     on_completed=lambda: print("Done!"),
                     on_error=lambda error: print("Error Occurred: {0}".format(error))
                     )


def test_map_and_filter():
    from rx import Observable, Observer

    # 创建 Observable 对象
    # source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

    # 对数据项进行映射
    # lengths = source.map(lambda s: len(s))

    # 过滤数据项
    # filterd = lengths.filter(lambda i: i >= 5)

    # 开始订阅观察者
    # filterd.subscribe(on_next=lambda value: print("Received {0}".format(value)))

    Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
        .map(lambda s: len(s)) \
        .filter(lambda i: i >= 5) \
        .subscribe(lambda value: print("Received {0}".format(value)))


if __name__ == '__main__':
    test_map_and_filter()
