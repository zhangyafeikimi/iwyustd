#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "sched.h": [
        # https://pubs.opengroup.org/onlinepubs/7908799/xsh/sched.h.html
        "sched_param",
        "SCHED_FIFO",
        "SCHED_RR",
        "SCHED_OTHER",
        "sched_get_priority_max",
        "sched_get_priority_min",
        "sched_getparam",
        "sched_getscheduler",
        "sched_rr_get_interval",
        "sched_setparam",
        "sched_setscheduler",
        "sched_yield",
    ],
}
