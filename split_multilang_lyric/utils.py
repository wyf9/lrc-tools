# coding: utf-8
from sys import argv
from time import perf_counter as __perf_counter

from colorama import Fore, Style


def getargv(key: int, default: str | None = None):
    try:
        return argv[key]
    except IndexError:
        return default


def perf_counter():
    '''
    获取一个性能计数器, 执行返回函数来结束计时, 并返回保留两位小数的毫秒值
    - copied from sleepy utils.py 😋
    '''
    start = __perf_counter()
    return lambda: round((__perf_counter() - start)*1000, 2)


def log(*content):
    print(f'{Fore.GREEN}{" ".join(str(c) for c in content)}{Style.RESET_ALL}')


def debug(*content):
    print(f'{Fore.BLUE}{" ".join(str(c) for c in content)}{Style.RESET_ALL}')


def warn(*content):
    print(f'{Fore.YELLOW}{" ".join(str(c) for c in content)}{Style.RESET_ALL}')


def error(*content):
    print(f'{Fore.RED}{" ".join(str(c) for c in content)}{Style.RESET_ALL}')
