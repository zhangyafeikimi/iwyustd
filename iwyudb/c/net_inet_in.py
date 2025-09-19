#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "netinet/in.h": [
        # https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/netinet_in.h.html
        "in_port_t",
        "in_addr_t",
        "sa_family_t",
        "uint8_t",
        "uint32_t",
        "in_addr",
        "sockaddr_in",
        "in6_addr",
        "sockaddr_in6",
        "in6addr_any",
        "IN6ADDR_ANY_INIT",
        "in6addr_loopback",
        "IN6ADDR_LOOPBACK_INIT",
        "ipv6_mreq",
        "IPPROTO_IP",
        "IPPROTO_IPV6",
        "IPPROTO_ICMP",
        "IPPROTO_RAW",
        "IPPROTO_TCP",
        "IPPROTO_UDP",
        "INADDR_ANY",
        "INADDR_BROADCAST",
        "INET_ADDRSTRLEN",
        "htonl",
        "htons",
        "ntohl",
        "ntohs",
        "INET6_ADDRSTRLEN",
        "IPV6_JOIN_GROUP",
        "IPV6_LEAVE_GROUP",
        "IPV6_MULTICAST_HOPS",
        "IPV6_MULTICAST_IF",
        "IPV6_MULTICAST_LOOP",
        "IPV6_UNICAST_HOPS",
        "IPV6_V6ONLY",
        "IN6_IS_ADDR_UNSPECIFIED",
        "IN6_IS_ADDR_LOOPBACK",
        "IN6_IS_ADDR_MULTICAST",
        "IN6_IS_ADDR_LINKLOCAL",
        "IN6_IS_ADDR_SITELOCAL",
        "IN6_IS_ADDR_V4MAPPED",
        "IN6_IS_ADDR_V4COMPAT",
        "IN6_IS_ADDR_MC_NODELOCAL",
        "IN6_IS_ADDR_MC_LINKLOCAL",
        "IN6_IS_ADDR_MC_SITELOCAL",
        "IN6_IS_ADDR_MC_ORGLOCAL",
        "IN6_IS_ADDR_MC_GLOBAL",
    ],
}
