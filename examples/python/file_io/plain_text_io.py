#!/usr/bin/env python3
# coding=utf8

def open_plain(filename):
    with open(filename) as fp:
        print(fp.read())


if __name__ == '__main__':
    plaintext = ""
    open_plain(plaintext)
