# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/05/06


def test_create():
    from rx import create

    def push_strings(observer, scheduler):
        observer.on_next("Alpha")
        observer.on_next("Beta")

    source = create(push_strings)

    source.subscribe(lambda i: print("Received data: {0}".format(i)))


def test_of():
    from rx import of, from_

    # source = of(*[1, "Alpha", [2, 3]])
    source = of(1, "Alpha", [2, 3])

    source.subscribe(lambda i: print("Received data: {0}".format(i)))


def test_pipe():
    import rx
    from rx import operators

    rx.of("Alpha", "Beta", "GammaRay").pipe(
        operators.map(lambda s: len(s)),
        operators.filter(lambda i: i >= 5)
    ).subscribe(lambda data: print("Received data: {0}".format(data)))


def test_pipe_function():
    import rx
    from rx import operators

    def filter_string_length():
        return rx.pipe(
            operators.map(lambda s: len(s)),
            operators.filter(lambda i: i >= 5)
        )

    rx.of("Alpha", "Beta", "GammaRay").pipe(
        filter_string_length()
    ).subscribe(lambda data: print("Received data: {0}".format(data)))


def test_zip():
    import operator
    import rx
    from rx import operators

    a = rx.of(1, 2, 3)
    b = rx.of(1, 2, 3)

    a.pipe(
        operators.zip(b),   # 返回一个由 a 和 b 数据项组成的元组
        operators.map(lambda z: operator.mul(z[0], z[1]))
        # operators.starmap(operator.mul)
    ).subscribe(lambda data: print("Received data: {0}".format(data)))


def test_merge():
    import rx

    obs1 = rx.of(1, 2)
    obs2 = rx.of(3, 4)

    res = rx.merge(obs1, obs2)
    res.subscribe(lambda data: print("Received data: {0}".format(data)))


def test_custom_operator():
    import rx

    def lowercase():
        # source 为传进来 Observable
        def observable_handle(source):
            def subscribe(observer, scheduler=None):
                # 重写 on_next 来达到处理数据项的目的
                def on_next(value):
                    observer.on_next(value.lower())

                return source.subscribe(
                    on_next,    # 替换为自己的 on_next
                    observer.on_error,
                    observer.on_completed,
                    scheduler
                )
            # 返回一个自定义的新的 Observable
            return rx.create(subscribe)

        return observable_handle

    rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        lowercase()
    ).subscribe(lambda data: print("Received data: {0}".format(data)))


if __name__ == "__main__":
    test_create()
