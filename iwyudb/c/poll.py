#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "poll.h": [
        # https://pubs.opengroup.org/onlinepubs/7908799/xsh/poll.h.html
        "pollfd",
        "nfds_t",
        "POLLIN",
        "POLLRDNORM",
        "POLLRDBAND",
        "POLLPRI",
        "POLLOUT",
        "POLLWRNORM",
        "POLLWRBAND",
        "POLLERR",
        "POLLHUP",
        "POLLNVAL",
        "poll",
    ],
}
