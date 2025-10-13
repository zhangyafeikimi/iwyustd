#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "sys/uio.h": [
        # https://pubs.opengroup.org/onlinepubs/007908799/xsh/sysuio.h.html
        "iovec",
        "readv",
        "writev",
    ],
}
