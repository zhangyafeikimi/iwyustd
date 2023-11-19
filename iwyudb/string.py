#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
    "HEADER_2_PREFIXES",
]


HEADER_2_SYMBOLS = {
    "string": [
        "std::basic_string",
        "std::char_traits",
        "std::getline",
        "std::pmr::basic_string",
        "std::pmr::string",
        "std::pmr::u16string",
        "std::pmr::u32string",
        "std::pmr::u8string",
        "std::pmr::wstring",
        "std::stod",
        "std::stof",
        "std::stoi",
        "std::stol",
        "std::stold",
        "std::stoll",
        "std::stoul",
        "std::stoull",
        "std::string",
        "std::to_string",
        "std::to_wstring",
        "std::u16string",
        "std::u32string",
        "std::u8string",
        "std::wstring",
    ],
    "string_view": [
        "std::basic_string_view",
        "std::string_view",
        "std::u16string_view",
        "std::u32string_view",
        "std::u8string_view",
        "std::wstring_view",
    ],
}


HEADER_2_PREFIXES = {
    "string": [
        "std::pmr::string",
        "std::pmr::u16string",
        "std::pmr::u32string",
        "std::pmr::u8string",
        "std::pmr::wstring",
        "std::string",
        "std::u16string",
        "std::u32string",
        "std::u8string",
        "std::wstring",
    ],
    "string_view": [
        "std::string_view",
        "std::u16string_view",
        "std::u32string_view",
        "std::u8string_view",
        "std::wstring_view",
    ],
}
