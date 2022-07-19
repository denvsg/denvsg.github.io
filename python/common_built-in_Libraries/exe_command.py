#!/usr/bin/env python3
# -*- coding:utf8 -*-
import os
import re
import subprocess
import sys


def exec_command(cmd, log_path='run.log', **kwargs):
    """
    执行命令，并获取命令的输出
    :param cmd: shell 命令
    :param log_path: 日志存放文件
    :param kwargs: 其他 subprocess.Popen 关键字参数
    :return: None
    """
    useful_info_pattern = re.compile(r'\[\d+/\d+\].+')
    is_log_filter = kwargs.pop('log_filter', False)

    with open(log_path, 'at', encoding='utf-8') as log_file:
        process = subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   encoding='utf-8',
                                   **kwargs)
        for line in iter(process.stdout.readline, ''):
            if is_log_filter:
                info = re.findall(useful_info_pattern, line)
                if len(info):
                    print_info(info[0])
            else:
                print_info(line)
            log_file.write(line)

    process.wait()
    ret_code = process.returncode

    if ret_code != 0:
        if is_log_filter:
            get_failed_log(log_path)

        raise OHOSException('Please check build log in {}'.format(log_path))


def get_failed_log(log_path):
    """
    获取执行失败的日志
    :param log_path: 日志文件
    :return: None
    """
    with open(log_path, 'rt', encoding='utf-8') as log_file:
        data = log_file.read()
    failed_pattern = re.compile(
        r'(\[\d+/\d+\].*?)(?=\[\d+/\d+\]|'
        'ninja: build stopped)', re.DOTALL)
    failed_log = failed_pattern.findall(data)
    for log in failed_log:
        if 'FAILED:' in log:
            print_error(log)

    failed_pattern = re.compile(r'(ninja: error:.*?)\n', re.DOTALL)
    failed_log = failed_pattern.findall(data)
    for log in failed_log:
        print_error(log)

    error_log = os.path.join(os.path.dirname(log_path), 'error.log')
    if os.path.isfile(error_log):
        with open(error_log, 'rt', encoding='utf-8') as log_file:
            print_error(log_file.read())


class OHOSException(Exception):
    ...


class Colors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    INFO = '\033[92m'
    END = '\033[0m'


def print_info(msg):
    """
    输出 info 级别日志
    :param msg: 输出的内容
    :return: None
    """
    level = 'info'
    for line in str(msg).splitlines():
        sys.stdout.write(message(level, line))
        sys.stdout.flush()


def print_warning(msg):
    """
    输出 warning 级别日志
    :param msg: 输出的内容
    :return: None
    """
    level = 'warning'
    for line in str(msg).splitlines():
        sys.stderr.write(message(level, line))
        sys.stderr.flush()


def print_error(msg):
    """
    输出 error 级别日志
    :param msg: 输出的内容
    :return: None
    """
    level = 'error'
    for line in str(msg).splitlines():
        sys.stderr.write(message(level, line))
        sys.stderr.flush()


def print_debug(msg):
    """
    输出 debug 级别日志
    :param msg: 输出的内容
    :return: None
    """
    level = 'debug'
    for line in str(msg).splitlines():
        sys.stderr.write(message(level, line))
        sys.stderr.flush()


def message(level, msg):
    """
    输出内容格式化
    :param level: 输出级别
    :param msg: 内容
    :return: None
    """
    if isinstance(msg, str) and not msg.endswith('\n'):
        msg += '\n'
    if level == 'error':
        msg = msg.replace('error:', f'{Colors.ERROR}error{Colors.END}:')
        return f'{Colors.ERROR}[Compile {level.upper()}]{Colors.END} {msg}'
    elif level == 'info':
        return f'[Compile {level.upper()}] {msg}'
    else:
        return f'{Colors.WARNING}[Compile {level.upper()}]{Colors.END} {msg}'


if __name__ == "__main__":
    # path="Z:/home/gnproject/simple_build/out"
    # exec_command('ninja', cwd=path)

    # exec_command('ninja')

    exec_command('ping 127.0.0.1')