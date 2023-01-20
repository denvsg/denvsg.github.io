#!/usr/bin/env python3
# -*- coding:utf8 -*-

import json
import rtoml
import toml
import yaml


def main():
    yaml_str = """
    [package]
    # info
    name='hello'
    age=89
    jobs='teacher'
    """
    # yaml_str = """
    # [package]
    # name = "rust_project"
    # version = "0.1.0"
    # authors = ["ovge <73331192+qisor@users.noreply.github.com>"]
    # edition = "2018"
    # """

    tml = toml.loads(yaml_str)
    print(tml)
    rtml = rtoml.loads(yaml_str)
    print(rtml)
    with open("a.toml", "w") as f:
        toml.dump(tml, f)

    print("*" * 72)
    with open("./Cargo.toml") as f:
        aa = toml.load(f)
    print(aa)


def main2():
    s = """{"results":[{"location":{"id":"WS0E9D8WN298","name":"广州","country":"CN","path":"广州,广州,广东,中国",
    "timezone":"Asia/Shanghai","timezone_offset":"+08:00"},"now":{"text":"阴","code":"9","temperature":"30"},
    "last_update":"2021-01-20T11:51:01+08:00"}]} """
    # with open("./test.json") as fj:
    #     json_str = json.load(fj)
    json_str = json.loads(s)
    json.dump(json_str, open('test.json', 'w', encoding='utf8'), ensure_ascii=False)
    # tmp = json.loads(fj.read())
    print(json_str)
    with open("t.toml", 'w', encoding='utf8') as f:
        toml.dump(json_str, f)
    with open("t.yaml", 'w', encoding='utf8') as f1:
        yaml.dump(json_str, f1, allow_unicode=True)


if __name__ == "__main__":
    # main()
    main2()
