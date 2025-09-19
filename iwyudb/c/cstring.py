#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "string.h": [
        # https://en.cppreference.com/w/c/header/string.html
        "NULL",
        #
        "size_t",
        #
        "memcpy",
        "memccpy",
        "memmove",
        "strcpy",
        "strncpy",
        "strdup",
        "strndup",
        "strcat",
        "strncat",
        "memcmp",
        "strcmp",
        "strcoll",
        "strncmp",
        "strxfrm",
        "memchr",
        "strchr",
        "strcspn",
        "strpbrk",
        "strrchr",
        "strspn",
        "strstr",
        "strtok",
        "memset",
        "memset_explicit",
        "strerror",
        "strlen",
        "strnlen",
        #
        "errno_t",
        "rsize_t",
        #
        "memcpy_s",
        "memmove_s",
        "strcpy_s",
        "strncpy_s",
        "strcat_s",
        "strncat_s",
        "strtok_s",
        "memset_s",
        "strerror_s",
        "strerrorlen_s",
        "strnlen_s",
    ]
    + [
        "strcasestr",
    ],
    "cstring": [
        # https://en.cppreference.com/w/cpp/header/cstring.html
        "std::size_t",
        #
        "std::memcpy",
        "std::memmove",
        "std::strcpy",
        "std::strncpy",
        "std::strcat",
        "std::strncat",
        "std::memcmp",
        "std::strcmp",
        "std::strcoll",
        "std::strncmp",
        "std::strxfrm",
        "std::memchr",
        "std::memchr",
        "std::strchr",
        "std::strcspn",
        "std::strpbrk",
        "std::strrchr",
        "std::strspn",
        "std::strstr",
        "std::strtok",
        "std::memset",
        "std::strerror",
        "std::strlen",
    ],
}


HEADER_2_SYMBOLS["cstring"] = HEADER_2_SYMBOLS["string.h"] + HEADER_2_SYMBOLS["cstring"]
