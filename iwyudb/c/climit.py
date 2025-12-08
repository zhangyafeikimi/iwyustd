#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "limits.h": [
        # https://en.cppreference.com/w/c/header/limits.html
        # https://en.cppreference.com/w/cpp/header/climits.html
        "BITINT_MAXWIDTH",
        "BOOL_MAX",
        "BOOL_WIDTH",
        "CHAR_BIT",
        "CHAR_MAX",
        "CHAR_MIN",
        "CHAR_WIDTH",
        "INT_MAX",
        "INT_MIN",
        "INT_WIDTH",
        "LLONG_MAX",
        "LLONG_MIN",
        "LLONG_WIDTH",
        "LONG_MAX",
        "LONG_MIN",
        "LONG_WIDTH",
        "MB_LEN_MAX",
        "SCHAR_MAX",
        "SCHAR_MIN",
        "SCHAR_WIDTH",
        "SHRT_MAX",
        "SHRT_MIN",
        "SHRT_WIDTH",
        "UCHAR_MAX",
        "UCHAR_WIDTH",
        "UINT_MAX",
        "UINT_WIDTH",
        "ULLONG_MAX",
        "ULLONG_WIDTH",
        "ULONG_MAX",
        "ULONG_WIDTH",
        "USHRT_MAX",
        "USHRT_WIDTH",
    ] + [
        "PATH_MAX",
    ],
}


HEADER_2_SYMBOLS["climits"] = HEADER_2_SYMBOLS["limits.h"]
