#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "signal.h": [
        # https://en.cppreference.com/w/c/header/signal.html
        "sig_atomic_t",
        #
        "signal",
        "raise",
        #
        "SIG_DFL",
        "SIG_ERR",
        "SIG_IGN",
        "SIGABRT",
        "SIGFPE",
        "SIGILL",
        "SIGINT",
        "SIGSEGV",
        "SIGTERM",
    ],
    "csignal": [
        # https://en.cppreference.com/w/cpp/header/csignal.html
        "std::sig_atomic_t",
        #
        "std::signal",
        "std::raise",
    ],
}


HEADER_2_SYMBOLS["csignal"] = HEADER_2_SYMBOLS["signal.h"] + HEADER_2_SYMBOLS["csignal"]
