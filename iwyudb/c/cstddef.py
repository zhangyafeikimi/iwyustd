#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "stddef.h": [
        # https://en.cppreference.com/w/c/header/stddef.html
        "ptrdiff_t",
        "nullptr_t",
        "max_align_t",
        # "wchar_t",  # `wchar_t` is a fundamental type in C++, so remove it.
        "size_t",
        #
        "NULL",
        "unreachable",
        "offsetof",
        #
        "rsize_t",
    ],
    "cstddef": [
        # https://en.cppreference.com/w/cpp/header/cstddef.html
        "std::ptrdiff_t",
        "std::size_t",
        "std::max_align_t",
        "std::nullptr_t",
        #
        "std::byte",
        #
        "std::to_integer",
    ],
}


HEADER_2_SYMBOLS["cstddef"] = HEADER_2_SYMBOLS["stddef.h"] + HEADER_2_SYMBOLS["cstddef"]
