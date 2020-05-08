# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/04/28

import sys


def get_input_demo():
    """
    从输入框获取输入，从第 10 次输入开始取前5次的输入，打印出来
    """
    from rx import Observable

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

    Observable.create(get_input) \
        .skip(5) \
        .take(10) \
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
    from rx import Observable

    # 创建 Observable 对象
    source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

    # 订阅观察者，on_next、on_completed、on_error 可选的
    source.subscribe(on_next=lambda value: print("Received {0}".format(value)),
                     on_completed=lambda: print("Done!"),
                     on_error=lambda error: print("Error Occurred: {0}".format(error))
                     )


def test_map_and_filter():
    from rx import Observable

    chaining = True

    if chaining:
        Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
            .map(lambda s: len(s)) \
            .filter(lambda i: i >= 5) \
            .subscribe(lambda value: print("Received {0}".format(value)))
    else:
        # 创建 Observable 对象
        source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

        # 对数据项进行映射
        lengths = source.map(lambda s: len(s))

        # 过滤数据项
        filterd = lengths.filter(lambda i: i >= 5)

        # 开始订阅观察者
        filterd.subscribe(on_next=lambda value: print("Received {0}".format(value)))


def test_interval():
    from rx import Observable

    Observable.interval(1000) \
        .map(lambda i: "收到了数据 {0}".format(i)) \
        .subscribe(lambda s: print(s))

    input("---- 按任意退出 -----\n")


def test_multicasting():
    from rx import Observable
    from random import randint

    def no_connected():
        emission_ints = Observable.range(1, 3).map(lambda i: randint(1, 100))
        emission_ints.subscribe(lambda data: print("subscribe_1 收到数据：{0}".format(data)))
        emission_ints.subscribe(lambda data: print("subscribe_2 收到数据：{0}".format(data)))

    def connected():
        emission_ints = Observable.range(1, 3).map(lambda i: randint(1, 100)).publish()
        emission_ints.subscribe(lambda data: print("subscribe_1 收到数据：{0}".format(data)))
        emission_ints.subscribe(lambda data: print("subscribe_2 收到数据：{0}".format(data)))
        emission_ints.connect()

    def auto_connected():
        emission_ints = Observable.range(1, 3).map(lambda i: randint(1, 100)).publish().auto_connect(2)
        emission_ints.subscribe(lambda data: print("subscribe_1 收到数据：{0}".format(data)))
        emission_ints.subscribe(lambda data: print("subscribe_2 收到数据：{0}".format(data)))

    auto_connected()


def test_zip():
    import operator
    from rx import Observable

    a = Observable.of(1, 2, 3, 4, 5)
    b = Observable.of(1, 2, 3, 4, 5)

    a.zip(b, lambda i, j: operator.mul(i, j)) \
        .subscribe(lambda data: print("Received data: {0}".format(data)))


def test_combine_observable():
    from rx import Observable

    word = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
    interval = Observable.interval(1000)

    Observable.zip(word, interval, lambda w, i: (w, i)) \
        .subscribe(lambda data: print(data))

    input("---- 按任意退出 -----\n")


def test_concurrency():
    import time
    import multiprocessing
    from threading import current_thread

    from rx import Observable
    from rx.concurrency import ThreadPoolScheduler

    # 根据 CPU 的核心个数创建线程池调度器
    optimal_thread_count = multiprocessing.cpu_count()
    pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

    # 通过休眠来模拟长时间运算
    def intense_calculation(value):
        time.sleep(1)
        print("Observable run in: {0}".format(current_thread().name))
        return value

    Observable.range(1, 3) \
        .map(lambda i: intense_calculation(i)) \
        .subscribe_on(pool_scheduler) \
        .subscribe(on_next=lambda i: print("subscriber run in: {0} data: {1}".format(current_thread().name, i)))


def test_python_alignment():
    from rx import Observable

    def concat():
        xs = Observable.from_([0, 1, 2, 3, 4, 5, 6])
        ys = Observable.from_([7, 8, 9])
        zs = xs + ys
        zs.subscribe(lambda data: print("data: {0}".format(data)))

    def duplicate():
        xs = Observable.from_([0, 1])
        ys = xs * 3
        ys.subscribe(lambda data: print("data: {0}".format(data)))

    def slice():
        xs = Observable.from_([0, 1, 2, 3, 4, 5, 6])
        ys = xs[2:6]
        ys.subscribe(lambda data: print("data: {0}".format(data)))

    slice()


def test_blocking():
    from rx import Observable

    res = Observable.of(1, 2, 3, 4, 6).to_blocking().last()
    print("Received last data: {0}".format(res))


if __name__ == '__main__':
    test_concurrency()
