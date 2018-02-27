# coding=utf-8


from util.colors import colorize2
from .gdb import Gdb


def green(text):
    """Wrapper for colorize(text, 'green')"""
    return colorize2(text, "green")


def red(text):
    """Wrapper for colorize(text, 'red')"""
    return colorize2(text, "red")


def yellow(text):
    """Wrapper for colorize(text, 'yellow')"""
    return colorize2(text, "yellow")


def blue(text):
    """Wrapper for colorize(text, 'blue')"""
    return colorize2(text, "blue")


class Pwndbg(Gdb):
    def __init__(self, prog, until=None):
        prompt = "\002pwndbg> \001"  # red("\001pwndbg> \002")
        procname = "pwndbg"
        super(Pwndbg, self).__init__(prog, until, prompt, procname)
