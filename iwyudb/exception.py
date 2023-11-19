#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
    "HEADER_2_PREFIXES",
]


HEADER_2_SYMBOLS = {
    "exception": [
        "std::current_exception",
        "std::get_terminate",
        "std::get_unexpected",
        "std::make_exception_ptr",
        "std::rethrow_exception",
        "std::rethrow_if_nested",
        "std::set_terminate",
        "std::set_unexpected",
        "std::terminate",
        "std::throw_with_nested",
        "std::uncaught_exception",
        "std::uncaught_exceptions",
        "std::unexpected",
    ],
}


HEADER_2_PREFIXES = {
    "exception": [
        "std::bad_exception",
        "std::exception",
        "std::exception_ptr",
        "std::nested_exception",
        "std::terminate_handler",
        "std::unexpected_handler",
    ],
}
