#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "codecvt": [
        # https://en.cppreference.com/w/cpp/header/codecvt.html
        "std::codecvt_mode",
        "std::consume_header",
        "std::generate_header",
        "std::little_endian",
    ],
}


HEADER_2_PREFIXES = {
    "codecvt": [
        # https://en.cppreference.com/w/cpp/header/codecvt.html
        "std::codecvt_utf8",
        "std::codecvt_utf16",
        "std::codecvt_utf8_utf16",
    ],
}
