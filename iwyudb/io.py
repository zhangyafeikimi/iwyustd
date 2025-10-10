#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
    "HEADER_2_PREFIXES",
]


HEADER_2_SYMBOLS = {
    "fstream": [
        "std::basic_filebuf",
        "std::basic_fstream",
        "std::basic_ifstream",
        "std::basic_ofstream",
        "std::filebuf",
        "std::fstream",
        "std::ifstream",
        "std::ofstream",
        "std::wfilebuf",
        "std::wfstream",
        "std::wifstream",
        "std::wofstream",
    ],
    "ios": [
        "std::basic_ios",
        "std::boolalpha",
        "std::dec",
        "std::defaultfloat",
        "std::fixed",
        "std::fpos",
        "std::hex",
        "std::hexfloat",
        "std::internal",
        "std::io_errc",
        "std::ios",
        "std::ios_base",
        "std::iostream_category",
        "std::left",
        "std::make_error_code",
        "std::make_error_condition",
        "std::noboolalpha",
        "std::noshowbase",
        "std::noshowpoint",
        "std::noshowpos",
        "std::noskipws",
        "std::nounitbuf",
        "std::nouppercase",
        "std::oct",
        "std::right",
        "std::scientific",
        "std::showbase",
        "std::showpoint",
        "std::showpos",
        "std::skipws",
        "std::streamoff",
        "std::streamsize",
        "std::unitbuf",
        "std::uppercase",
        "std::wios",
    ],
    "iostream": [
        "std::cerr",
        "std::cin",
        "std::clog",
        "std::cout",
        "std::wcerr",
        "std::wcin",
        "std::wclog",
        "std::wcout",
    ],
    "istream": [
        "std::basic_iostream",
        "std::basic_istream",
        "std::iostream",
        "std::istream",
        "std::wiostream",
        "std::wistream",
        "std::ws",
    ],
    "ostream": [
        "std::basic_ostream",
        "std::emit_on_flush",
        "std::endl",
        "std::ends",
        "std::flush",
        "std::flush_emit",
        "std::noemit_on_flush",
        "std::ostream",
        "std::wostream",
    ],
    "sstream": [
        "std::basic_istringstream",
        "std::basic_ostringstream",
        "std::basic_stringbuf",
        "std::basic_stringstream",
        "std::istringstream",
        "std::ostringstream",
        "std::stringbuf",
        "std::stringstream",
        "std::wistringstream",
        "std::wostringstream",
        "std::wstringbuf",
        "std::wstringstream",
    ],
    "streambuf": [
        "std::basic_streambuf",
        "std::streambuf",
        "std::wstreambuf",
    ],
}


HEADER_2_PREFIXES = {
    "fstream": [
        "std::filebuf",
        "std::ifstream",
        "std::ofstream",
        "std::wfilebuf",
        "std::wifstream",
        "std::wofstream",
    ],
    "ios": [
        "std::io_errc",
        "std::ios",
        "std::ios_base",
        "std::wios",
    ],
    "iostream": [],
    "istream": [
        "std::iostream",
        "std::istream",
        "std::wiostream",
        "std::wistream",
    ],
    "ostream": [
        "std::ostream",
        "std::wostream",
    ],
    "sstream": [
        "std::istringstream",
        "std::ostringstream",
        "std::stringbuf",
        "std::stringstream",
        "std::wistringstream",
        "std::wostringstream",
        "std::wstringbuf",
        "std::wstringstream",
    ],
    "streambuf": [
        "std::streambuf",
        "std::wstreambuf",
    ],
}


# <iostream> includes <ios>, <streambuf>, <istream> and <ostream>.
HEADER_2_SYMBOLS["iostream"] += HEADER_2_SYMBOLS["ios"]
HEADER_2_SYMBOLS["iostream"] += HEADER_2_SYMBOLS["istream"]
HEADER_2_SYMBOLS["iostream"] += HEADER_2_SYMBOLS["ostream"]
HEADER_2_SYMBOLS["iostream"] += HEADER_2_SYMBOLS["streambuf"]
HEADER_2_PREFIXES["iostream"] += HEADER_2_PREFIXES["ios"]
HEADER_2_PREFIXES["iostream"] += HEADER_2_PREFIXES["istream"]
HEADER_2_PREFIXES["iostream"] += HEADER_2_PREFIXES["ostream"]
HEADER_2_PREFIXES["iostream"] += HEADER_2_PREFIXES["streambuf"]
