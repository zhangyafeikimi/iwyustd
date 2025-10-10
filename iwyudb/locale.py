#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "locale": [
        # https://en.cppreference.com/w/cpp/header/locale.html
        "std::use_facet",
        "std::has_facet",
        "std::isspace",
        "std::isprint",
        "std::iscntrl",
        "std::isupper",
        "std::islower",
        "std::isalpha",
        "std::isdigit",
        "std::ispunct",
        "std::isxdigit",
        "std::isalnum",
        "std::isgraph",
        "std::toupper",
        "std::tolower",
    ],
}


HEADER_2_PREFIXES = {
    "locale": [
        # https://en.cppreference.com/w/cpp/header/locale.html
        "std::locale",
        "std::wstring_convert",
        "std::wbuffer_convert",
        "std::ctype_base",
        "std::ctype",
        "std::ctype_byname",
        "std::codecvt_base",
        "std::codecvt",
        "std::codecvt_byname",
        "std::num_get",
        "std::num_put",
        "std::numpunct",
        "std::numpunct_byname",
        "std::collate",
        "std::collate_byname",
        "std::time_base" "time_get" "time_get_byname",
        "std::time_put",
        "std::time_put_byname",
        "std::money_base",
        "std::money_get",
        "std::money_put",
        "std::moneypunct",
        "std::moneypunct_byname",
        "std::messages_base",
        "std::messages",
        "std::messages_byname",
    ],
}
