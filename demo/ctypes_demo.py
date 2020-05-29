#!/bin/python3
# -*- coding: utf-8 -*-

import ctypes


def test_array():
    """ 测试数组 """
    # 构建10个元素的数组
    type_int_array_10 = ctypes.c_int * 10
    my_array = type_int_array_10()

    # 给数组赋值
    for i in range(10):
        my_array[i] = ctypes.c_int((i + 1) * 2)

    # 遍历数组
    for i in range(len(my_array)):
        print(my_array[i])


def test_pointer():
    """ 测试指针 """
    int_value = ctypes.c_int(5)
    int_value.value = 10

    # -------------- 方式一 ---------------
    type_p_int = ctypes.POINTER(ctypes.c_int)
    p_int = type_p_int(int_value)
    print("type(p_int): ", type(p_int), "p_int[0]: ", p_int[0], "p_int.contents: ", p_int.contents)

    # -------------- 方式二 ---------------
    p_int = ctypes.pointer(int_value)
    print("type(p_int): ", type(p_int), "p_int[0]: ", p_int[0], "p_int.contents: ", p_int.contents)


if __name__ == "__main__":
    test_array()
