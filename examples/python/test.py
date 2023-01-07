# import os
# import subprocess
#


class Colors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    INFO = '\033[92m'
    END = '\033[0m'


# a = [14, 25, 73, 42, 51]
#
# b = sorted(a)
# c = sorted(a, reverse=True)
# print(a)
# print(b)
# print(c)
#
# print(os.environ.get("PATH"))
#
# all_env = os.environ.get("PATH")
# if "git" in all_env.lower():
#     print("yes")
#
# env = all_env.split(";")
# print(env)
# git = [git for git in env if "Git" in git][0]
# print(git)
# # git_path = git.replace("\\", "/")
# cmd_path = os.path.join(git, "..\\usr\\bin")
# print(cmd_path)
# if os.path.exists(cmd_path):
#     print("exist path")
# a = subprocess.check_output("ls", shell=True, cwd=f"{cmd_path}")
# print(a.decode("utf8"))
#
# print(subprocess.getstatusoutput('git --version'))
# print(subprocess.getstatusoutput('node -v'))
import os.path
import threading

project_path = "C:/Users/dsg/DevEcoStudioProjects/MyApplication"
pages = 'entry/build/default/intermediates/assets/default/ets/pages'
node_modules_path = 'entry/build/default/intermediates/assets/default/node_modules'


def get_parent_path(x, y=1):
    """
    获取指定目录的父目录
    :param x: 目录
    :param y: 向上多少层级，默认当前目录的父目录即一级
    :return: 目标目录
    """
    _tmp = x
    for _ in range(y):
        _tmp = os.path.dirname(_tmp)
    return _tmp


class SingleExp:
    _instance = None
    rlock = threading.RLock()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        with cls.rlock:
            cls._instance = object.__new__(cls)
        return cls._instance

    # def __str__(self):
    #     return f"{self.name},{self.age}"

    def __repr__(self):
        return f"{self.__class__}"


# test = get_parent_path(project_path, 2)
# print(test)
#
# s = SingleExp("abc", 19)
# print(s, id(s))
# s2 = SingleExp("def", 119)
# print(s2, id(s2))
# s3 = SingleExp("dfg", 199)
# print(s3, id(s3))
strs = [
    "cool",
    "egg",
    "foo",
    "paper",
    "tooools",
    "aba",
    "baa",
    "aaaa",
    "aaaaabbbbbcccccdddddeeeee"
]
str2 = [
    "fool",
    "add",
    "bar",
    "title",
    "tppppls",
    "baa",
    "aba",
    "aaaa",
    "pppppqqqqqrrrrrsssssttttt"
]


def isIsomorphic(s: str, t: str) -> bool:
    print("*" * 72)
    len_s = len(set(s))
    len_t = len(set(t))
    if s > t:
        s, t = t, s
    if len_s != len_t:
        print(False)
        return False
    for i in set(s):
        s_count = s.count(i)
        if s_count == 1:
            continue
        for index in range(s_count - 1):
            start_index = s.find(i, index)
            second_index = s.rfind(i)
            if t[start_index] == t[second_index]:
                continue
            else:
                print(False)
                return False
    print(True)
    return True


if __name__ == '__main__':
    [isIsomorphic(strs[i], str2[i]) for i in range(len(strs))]
