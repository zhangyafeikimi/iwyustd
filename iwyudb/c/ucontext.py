#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "ucontext.h": [
        # https://pubs.opengroup.org/onlinepubs/7908799/xsh/ucontext.h.html
        "mcontext_t",
        "ucontext_t",
        "sigset_t",
        "stack_t",
        "getcontext",
        "setcontext",
        "makecontext",
        "swapcontext",
    ],
}
