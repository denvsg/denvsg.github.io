#!/usr/bin/env python3
# -*- coding:utf8 -*-


def deco_func(f):
    def inner():
        print("This is inner of deco_func")
        f()

    return inner


@deco_func
def func():
    print("This is func")


if __name__ == "__main__":
    # f = deco_func
    # f(func()) # 此两行等同下面一行
    func()
