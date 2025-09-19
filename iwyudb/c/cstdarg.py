#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "stdarg.h": [
        # https://en.cppreference.com/w/c/header/stdarg.html
        "va_list",
        #
        "va_arg",
        "va_copy",
        "va_end",
        "va_start",
    ],
    "cstdarg": [
        # https://en.cppreference.com/w/cpp/header/cstdarg.html
        "std::va_list",
    ],
}


HEADER_2_SYMBOLS["cstdarg"] = HEADER_2_SYMBOLS["stdarg.h"] + HEADER_2_SYMBOLS["cstdarg"]
