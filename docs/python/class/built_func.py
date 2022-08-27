#!/usr/bin/env python3
# -*- coding:utf8 -*-

class App:
    def __init__(self, name, age):
        print("init function")
        self.name = name
        self.age = age

    def __str__(self):
        print("str function")
        return f"name is {self.name},age is {self.age}"

    def __repr__(self):
        print("repr function")
        return f"name is {self.name},age is {self.age}"

    def __add__(self, other):
        return f"name is {self.name}, welcome to {other}"


if __name__ == "__main__":
    a = App("app", 16)
    print(a)
    print(repr(a))

    b = a + "abc"
    print(b)
