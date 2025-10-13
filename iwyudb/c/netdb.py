#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "netdb.h": [
        # https://pubs.opengroup.org/onlinepubs/7908799/xns/netdb.h.html
        "in_port_t",
        "in_addr_t",
        "hostent",
        "netent",
        "uint32_t",
        "protoent",
        "servent",
        "IPPORT_RESERVED",
        "h_errno",
        "HOST_NOT_FOUND",
        "NO_DATA",
        "NO_RECOVERY",
        "TRY_AGAIN",
        "endhostent",
        "endnetent",
        "endprotoent",
        "endservent",
        "gethostbyaddr",
        "gethostbyname",
        "gethostent",
        "getnetbyaddr",
        "getnetbyname",
        "getnetent",
        "getprotobyname",
        "getprotobynumber",
        "getprotoent",
        "getservbyname",
        "getservbyport",
        "getservent",
        "sethostent",
        "setnetent",
        "setprotoent",
        "setservent",
    ]
    + [
        "gai_strerror",
    ],
}
