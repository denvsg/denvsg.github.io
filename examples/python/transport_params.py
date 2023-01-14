def func1(**kwargs):
    a = kwargs.pop("cmd", False)
    print("func1", a)
    print(kwargs)


def func2(arg1, arg2, *args, x=1, y=2, z=3, **kwargs):
    # locals().pop("kwargs", None)
    # n = locals()
    # n.pop("kwargs", None)
    n = {k: v for k, v in locals().items() if k not in ("args", "kwargs")}
    print("func n :", n)
    b = kwargs.pop("use", True)
    print("func2 b =", b)
    print(kwargs)
    kwargs["func2_123"] = 456789
    kwargs.update(n)
    print("params is:", kwargs)
    print("\nfunc1 start ", "*" * 72)
    func1(**kwargs)


def func3(arg1, arg2, *args, **kwargs):
    c = kwargs.get("pos1", (10, 56))
    print("func3_1", c)
    print(kwargs)

    c = kwargs.pop("pos1", (12, 78))
    print("func3", c)
    kwargs["func3_123"] = 456  # add argument
    print("params is:", kwargs)
    print("\nfunc2 start ", "*" * 72)
    func2(1, 2, 3, 4, **kwargs)


def main():
    params = {"cmd": "hello,cmd", "use": "use python", "pos1": (123, 678), "config": "yaml"}
    func3(1, 2, 3, "pms", **params)


if __name__ == "__main__":
    main()
