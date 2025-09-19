#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "arpa/inet.h": [
        # https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/arpa_inet.h.html
        "in_port_t",
        "in_addr_t",
        "socklen_t",
        "in_addr",
        "INET_ADDRSTRLEN",
        "INET6_ADDRSTRLEN",
        "htonl",
        "htons",
        "ntohl",
        "ntohs",
        "uint32_t",
        "uint16_t",
        "inet_addr",
        "inet_ntoa",
        "inet_ntop",
        "inet_pton",
    ]
    + [
        "inet_aton",
        "inet_lnaof",
        "inet_makeaddr",
        "inet_netof",
        "inet_network",
    ],
}
