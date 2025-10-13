#! /usr/bin/env python3
#


import re
import types
from typing import Dict, List, Set

from iwyudb.c import arpa_inet
from iwyudb.c import cassert
from iwyudb.c import cctypes
from iwyudb.c import cerrno
from iwyudb.c import cinttypes
from iwyudb.c import climit
from iwyudb.c import clocale
from iwyudb.c import cmath
from iwyudb.c import csignal
from iwyudb.c import cstdarg
from iwyudb.c import cstddef
from iwyudb.c import cstdint
from iwyudb.c import cstdio
from iwyudb.c import cstdlib
from iwyudb.c import cstring
from iwyudb.c import ctime
from iwyudb.c import cwchar
from iwyudb.c import dlfcn
from iwyudb.c import fcntl
from iwyudb.c import libgen
from iwyudb.c import net_inet_in
from iwyudb.c import netdb
from iwyudb.c import poll
from iwyudb.c import pthread
from iwyudb.c import sched
from iwyudb.c import strings
from iwyudb.c import sys_mman
from iwyudb.c import sys_socket
from iwyudb.c import sys_stat
from iwyudb.c import sys_time
from iwyudb.c import sys_types
from iwyudb.c import sys_uio
from iwyudb.c import sys_un
from iwyudb.c import ucontext
from iwyudb.c import unistd

from iwyudb import any
from iwyudb import algorithm
from iwyudb import chrono
from iwyudb import codecvt
from iwyudb import concurrent
from iwyudb import container
from iwyudb import exception
from iwyudb import filesystem
from iwyudb import functional
from iwyudb import initializer_list
from iwyudb import io
from iwyudb import iomanip
from iwyudb import iterator
from iwyudb import limits
from iwyudb import locale
from iwyudb import memory
from iwyudb import numeric
from iwyudb import random
from iwyudb import regex
from iwyudb import stdexcept
from iwyudb import string
from iwyudb import system_error
from iwyudb import tuple
from iwyudb import type_traits
from iwyudb import typeindex
from iwyudb import typeinfo
from iwyudb import utility
from iwyudb import variant


__all__ = [
    "SYMBOL_2_HEADERS",
    "PREFIX_2_HEADERS",
    "HEADER_SET",
    "SYMBOL_PATTERN",
    "PREFIX_PATTERN",
]


RE_COMPILE_TYPE = type(re.compile("Hello World"))


def build_header_2_symbols(key: str) -> Dict[str, List[str]]:
    table = {}
    for _, module in globals().items():
        if isinstance(module, types.ModuleType):
            if hasattr(module, key):
                table.update(getattr(module, key))
    return table


def build_symbol_2_headers(header_2_symbols: Dict[str, List[str]]) -> Dict[str, Set[str]]:
    table: Dict[str, Set[str]] = {}
    for header, symbols in header_2_symbols.items():
        for symbol in symbols:
            if symbol in table:
                headers = table[symbol]
                headers.add(header)
            else:
                table[symbol] = set([header])
    return table


def build_symbol_pattern(symbols: Set[str]) -> RE_COMPILE_TYPE:
    c_symbols = [symbol for symbol in symbols if not symbol.startswith("std::")]
    return re.compile(r"\b(" + "|".join(c_symbols) + r"|std(::[A-Za-z][A-Za-z_0-9]+)+)\b")


def build_prefix_pattern(prefixes: Set[str]) -> RE_COMPILE_TYPE:
    return re.compile(r"^\b(" + "|".join(prefixes) + r")\b")


HEADER_2_SYMBOLS = build_header_2_symbols("HEADER_2_SYMBOLS")
HEADER_2_PREFIXES = build_header_2_symbols("HEADER_2_PREFIXES")
SYMBOL_2_HEADERS = build_symbol_2_headers(HEADER_2_SYMBOLS)
PREFIX_2_HEADERS = build_symbol_2_headers(HEADER_2_PREFIXES)
HEADER_SET = set(HEADER_2_SYMBOLS.keys()) | set(HEADER_2_PREFIXES.keys())
SYMBOL_PATTERN = build_symbol_pattern(SYMBOL_2_HEADERS.keys())
PREFIX_PATTERN = build_prefix_pattern(PREFIX_2_HEADERS.keys())
