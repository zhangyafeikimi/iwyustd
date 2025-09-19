#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "ctype.h": [
        # https://en.cppreference.com/w/c/header/ctype.html
        "isalnum",
        "isalpha",
        "isblank",
        "iscntrl",
        "isdigit",
        "isgraph",
        "islower",
        "isprint",
        "ispunct",
        "isspace",
        "isupper",
        "isxdigit",
        "tolower",
        "toupper",
    ],
    "cctype": [
        # https://en.cppreference.com/w/cpp/header/cctype.html
        "std::isalnum",
        "std::isalpha",
        "std::isblank",
        "std::iscntrl",
        "std::isdigit",
        "std::isgraph",
        "std::islower",
        "std::isprint",
        "std::ispunct",
        "std::isspace",
        "std::isupper",
        "std::isxdigit",
        "std::tolower",
        "std::toupper",
    ],
}


HEADER_2_SYMBOLS["cctype"] = HEADER_2_SYMBOLS["ctype.h"] + HEADER_2_SYMBOLS["cctype"]
