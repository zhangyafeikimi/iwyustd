#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "sys/un.h": [
        # https://pubs.opengroup.org/onlinepubs/007908799/xns/sysun.h.html
        "sockaddr_un",
        "sa_family_t",
    ],
}
