#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "locale.h": [
        # https://en.cppreference.com/w/c/header/locale.html
        "lconv",
        #
        "setlocale",
        "localeconv",
        #
        "NULL",
        "LC_ALL",
        "LC_COLLATE",
        "LC_CTYPE",
        "LC_MONETARY",
        "LC_NUMERIC",
        "LC_TIME",
    ]
    + [
        # https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/locale.h.html
        "lconv",
        "NULL",
        "LC_ALL",
        "LC_COLLATE",
        "LC_CTYPE",
        "LC_MESSAGES",
        "LC_MONETARY",
        "LC_NUMERIC",
        "LC_TIME",
        "LC_COLLATE_MASK",
        "LC_CTYPE_MASK",
        "LC_MESSAGES_MASK",
        "LC_MONETARY_MASK",
        "LC_NUMERIC_MASK",
        "LC_TIME_MASK",
        "LC_ALL_MASK",
        "LC_GLOBAL_LOCALE",
        "locale_t",
        "duplocale",
        "freelocale",
        "getlocalename_l",
        "localeconv",
        "newlocale",
        "setlocale",
        "uselocale",
    ],
    "clocale": [
        # https://en.cppreference.com/w/cpp/header/clocale.html
        "std::lconv",
        #
        "std::setlocale",
        "std::localeconv",
    ],
}


HEADER_2_SYMBOLS["clocale"] = HEADER_2_SYMBOLS["locale.h"] + HEADER_2_SYMBOLS["clocale"]
