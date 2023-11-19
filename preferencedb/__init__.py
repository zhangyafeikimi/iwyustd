#! /usr/bin/env python3
#


__all__ = [
    "SYMBOL_2_PREFERRED_SYMBOLS",
]


SYMBOL_2_PREFERRED_SYMBOLS = {
    "std::iostream": [
        "std::istream",
        "std::ostream",
    ],
    "std::wiostream": [
        "std::wistream",
        "std::wostream",
    ],
    "std::stringstream": [
        "std::istringstream",
        "std::ostringstream",
    ],
    "std::wstringstream": [
        "std::wistringstream",
        "std::wostringstream",
    ],
    "std::fstream": [
        "std::ifstream",
        "std::ofstream",
    ],
    "std::wfstream": [
        "std::wifstream",
        "std::wofstream",
    ],
    "NULL": [
        "nullptr",
    ],
}
