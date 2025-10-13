#! /usr/bin/env python3
#


__all__ = [
    "HEADER_2_SYMBOLS",
]


HEADER_2_SYMBOLS = {
    "sys/mman.h": [
        # https://pubs.opengroup.org/onlinepubs/007904875/basedefs/sys/mman.h.html
        "PROT_READ",
        "PROT_WRITE",
        "PROT_EXEC",
        "PROT_NONE",
        "MAP_SHARED",
        "MAP_PRIVATE",
        "MAP_FIXED",
        "MS_ASYNC",
        "MS_SYNC",
        "MS_INVALIDATE",
        "MCL_CURRENT",
        "MCL_FUTURE",
        "POSIX_MADV_NORMAL",
        "POSIX_MADV_SEQUENTIAL",
        "POSIX_MADV_RANDOM",
        "POSIX_MADV_WILLNEED",
        "POSIX_MADV_DONTNEED",
        "POSIX_TYPED_MEM_ALLOCATE",
        "POSIX_TYPED_MEM_ALLOCATE_CONTIG",
        "POSIX_TYPED_MEM_MAP_ALLOCATABLE",
        "mode_t",
        "off_t",
        "size_t",
        "posix_typed_mem_info",
        "mlock",
        "mlockall",
        "mmap",
        "mprotect",
        "msync",
        "munlock",
        "munlockall",
        "munmap",
        "posix_madvise",
        "posix_mem_offset",
        "posix_typed_mem_get_info",
        "posix_typed_mem_open",
        "shm_open",
        "shm_unlink",
    ],
}
