#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "dlfcn.h": [
        # https://pubs.opengroup.org/onlinepubs/7908799/xsh/dlfcn.h.html
        "RTLD_LAZY",
        "RTLD_NOW",
        "RTLD_GLOBAL",
        "RTLD_LOCAL",
        "dlopen",
        "dlsym",
        "dlclose",
        "dlerror",
    ],
}
