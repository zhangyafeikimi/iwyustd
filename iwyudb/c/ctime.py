#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "time.h": [
        # https://en.cppreference.com/w/c/header/time.html
        "NULL",
        "CLOCKS_PER_SEC",
        "TIME_UTC",
        #
        "clock_t",
        "size_t",
        "time_t",
        #
        "timespec",
        "tm",
        #
        "clock",
        "difftime",
        "mktime",
        "timegm",
        "time",
        "timespec_get",
        "timespec_getres",
        "asctime",
        "ctime",
        "gmtime",
        "gmtime_r",
        "localtime",
        "localtime_r",
        "strftime",
        #
        "TIME_MONOTONIC",
        "TIME_ACTIVE",
        #
        "TIME_THREAD_ACTIVE",
        #
        "errno_t",
        "rsize_t",
        #
        "asctime_s",
        "ctime_s",
        "gmtime_s",
        "localtime_s",
    ]
    + [
        "CLOCK_REALTIME",
        "CLOCK_REALTIME_ALARM",
        "CLOCK_REALTIME_COARSE",
        "CLOCK_TAI",
        "CLOCK_MONOTONIC",
        "CLOCK_MONOTONIC_COARSE",
        "CLOCK_MONOTONIC_RAW",
        "CLOCK_BOOTTIME",
        "CLOCK_BOOTTIME_ALARM",
        "CLOCK_PROCESS_CPUTIME_ID",
        "CLOCK_THREAD_CPUTIME_ID",
        "CLOCK_MONOTONIC_RAW_APPROX",
        "CLOCK_UPTIME_RAW",
        "CLOCK_UPTIME_RAW_APPROX",
        "clock_gettime",
        "clock_settime",
        "clock_getres",
        "clock_gettime_nsec_np",
    ],
    "ctime": [
        # https://en.cppreference.com/w/cpp/header/ctime.html
        "std::size_t",
        "std::clock_t",
        "std::time_t",
        #
        "std::timespec",
        "std::tm",
        #
        "std::clock",
        "std::difftime",
        "std::mktime",
        "std::time",
        "std::timespec_get",
        "std::asctime",
        "std::ctime",
        "std::gmtime",
        "std::localtime",
        "std::strftime",
    ],
}


HEADER_2_SYMBOLS["ctime"] = HEADER_2_SYMBOLS["time.h"] + HEADER_2_SYMBOLS["ctime"]
