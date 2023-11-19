#! /usr/bin/env python3
#


import re
import sys
from typing import List, Tuple


###################################################################
__all__ = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "purple",
    "cyan",
    "white",
    "remove_line_continuation",
    "canonicalize",
    "Highlighter",
]


###################################################################
BOLD_BLACK = "\033[1;30m"
BOLD_RED = "\033[1;31m"
BOLD_GREEN = "\033[1;32m"
BOLD_YELLOW = "\033[1;33m"
BOLD_BLUE = "\033[1;34m"
BOLD_PURPLE = "\033[1;35m"
BOLD_CYAN = "\033[1;36m"
BOLD_WHITE = "\033[1;37m"
RESET = "\033[0m"


def black(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_BLACK, s, RESET)
    else:
        return s


def red(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_RED, s, RESET)
    else:
        return s


def green(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_GREEN, s, RESET)
    else:
        return s


def yellow(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_YELLOW, s, RESET)
    else:
        return s


def blue(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_BLUE, s, RESET)
    else:
        return s


def purple(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_PURPLE, s, RESET)
    else:
        return s


def cyan(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_CYAN, s, RESET)
    else:
        return s


def white(s: str, f=sys.stdout) -> str:
    if f.isatty():
        return "{}{}{}".format(BOLD_WHITE, s, RESET)
    else:
        return s


###################################################################
LF = ord("\n")
LINE_CONTINUATION_PATTERN = re.compile(rb"\\[ \t]*(\r\n|\n)")


def remove_line_continuation(s: bytes) -> bytes:
    return LINE_CONTINUATION_PATTERN.sub(b"", s)


def canonicalize(s: bytes) -> bytes:
    s = s.replace(b"\r\n", b"\n")
    if len(s) == 0 or s[-1] != LF:
        s = s + b"\n\n"
    else:
        s = s + b"\n"
    return s


###################################################################
class Highlighter(object):
    _content: bytes
    _lineno: int
    _lineno_2_offset_content: List[Tuple[int, bytes]]
    _offset_2_lineno: List[int]

    def __init__(self, content: bytes):
        self._content = canonicalize(content)
        self._lineno = 0
        self._lineno_2_offset_content = []
        self._offset_2_lineno = []

        offset = 0
        while True:
            i = self._content.find(b"\n", offset)
            if i != -1:
                new_offset = i + 1
                self._lineno_2_offset_content.append((offset, self._content[offset:new_offset]))
                for _ in range(offset, new_offset):
                    self._offset_2_lineno.append(self._lineno)
                self._lineno += 1
                offset = new_offset
            else:
                for _ in range(offset, len(self._content)):
                    self._offset_2_lineno.append(self._lineno)
                break

        assert self._lineno == len(self._lineno_2_offset_content)
        assert offset == len(self._content) == len(self._offset_2_lineno)

    def highlight(
        self,
        begin_offset: int,
        end_offset: int,
        before_lines: int = 3,
        after_lines: int = 3,
        color: str = "red",
    ) -> str:
        assert begin_offset <= end_offset
        assert 0 <= begin_offset < len(self._offset_2_lineno), begin_offset
        assert 0 <= end_offset < len(self._offset_2_lineno), end_offset
        assert before_lines >= 0, before_lines
        assert after_lines >= 0, after_lines

        if color == "black":
            color_func = black
        elif color == "red":
            color_func = red
        elif color == "green":
            color_func = green
        elif color == "yellow":
            color_func = yellow
        elif color == "blue":
            color_func = blue
        elif color == "purple":
            color_func = purple
        elif color == "cyan":
            color_func = cyan
        elif color == "white":
            color_func = white
        else:
            color_func = red

        begin_lineno = self._offset_2_lineno[begin_offset]
        end_lineno = self._offset_2_lineno[end_offset]
        content = ""
        for i in range(max(begin_lineno - before_lines, 0), begin_lineno):
            _, _content = self._lineno_2_offset_content[i]
            content += "%5d   " % (i + 1)
            content += _content.decode()
        for i in range(begin_lineno, end_lineno + 1):
            _offset, _content = self._lineno_2_offset_content[i]
            b_in_line = _offset <= begin_offset < _offset + len(_content)
            e_in_line = _offset <= end_offset < _offset + len(_content)
            content += "%5d   " % (i + 1)
            if b_in_line and not e_in_line:
                content += _content[0 : begin_offset - _offset].decode()
                content += color_func(_content[begin_offset - _offset :].decode())
            elif not b_in_line and e_in_line:
                content += color_func(_content[0 : end_offset - _offset].decode())
                content += _content[end_offset - _offset :].decode()
            elif b_in_line and e_in_line:
                content += _content[0 : begin_offset - _offset].decode()
                content += color_func(_content[begin_offset - _offset : end_offset - _offset].decode())
                content += _content[end_offset - _offset :].decode()
            else:
                content += color_func(_content.decode())
        for i in range(end_lineno + 1, min(end_lineno + after_lines + 1, self._lineno - 1)):
            _, _content = self._lineno_2_offset_content[i]
            content += "%5d   " % (i + 1)
            content += _content.decode()
        return content
