#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "assert.h": [
        # https://en.cppreference.com/w/c/header/assert.html
        # https://en.cppreference.com/w/cpp/header/cassert.html
        "assert",
    ],
}


HEADER_2_SYMBOLS["cassert"] = HEADER_2_SYMBOLS["assert.h"]
