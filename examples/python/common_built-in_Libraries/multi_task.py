# -*- code:utf-8 -*-
import os
import subprocess
import sys
import time

ENCODING = "gbk" if sys.platform == "win32" else "utf8"

print(sys.platform)


def run_cmd(cmd, func=None, func_args=(), func_kwargs=None, **kwargs):
    """
    run some command
    :param cmd: cmd Sequence
    :param func: require execute function
    :param func_args:  function params
    :param func_kwargs: function keyword params
    :param kwargs: other subprocess params
    :return:
    """
    if func is None:
        raise AttributeError(f"params func must be.")
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            encoding=ENCODING,
                            shell=False,
                            preexec_fn=None if sys.platform == "win32" else os.setsid,
                            **kwargs
                            )
    if func_kwargs is None:
        func_kwargs = {}
    try:
        func(*func_args, **func_kwargs)
    except TypeError as err:
        print(f"Error message is <{err}>.")
        raise AttributeError(f"{func} object is not callable.")

    out, err = proc.communicate(timeout=15)
    ret_code = proc.returncode
    print(out) if ret_code == 0 else ...
    print(err) if ret_code == 1 else ...


def func(arg, *args):
    print(f"params is {arg}, {args}")
    # print(f"params is {kwargs}")
    print("num 1")
    print("num 2")
    time.sleep(5)
    print("num 3")


def main():
    cmd = ['ping', '127.1', '-n', '10']
    func1 = 5
    run_cmd(cmd,
            func=func,
            func_args=(1, 2, 3,),
            # func_kwargs={'4': 5, '6': 7}
            )


if __name__ == "__main__":
    main()
