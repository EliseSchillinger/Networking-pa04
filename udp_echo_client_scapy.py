#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
UDP echo with scapy instead of socket
"""
import time
import fake_time  # Use for time calcs
import sys
import statistics
from scapy.all import *

# https://scapy.readthedocs.io/en/latest/troubleshooting.html
conf.L3socket = L3RawSocket
# sometimes needed for default gateway, and
# always for localhost, and
# sometimes not for remote.


def parse_args() -> tuple[str, int, int, int]:
    """
    parses the 4 args:
    server_hostname, server_port, num_pings, timeout
    """
    pass #delete this and write (or copy from pa03)


def net_stats(
    num_pings: int, rtt_hist: list[float]
) -> tuple[float, float, float, float, float]:
    """
    Computes statistics for loss and timing.
    Mimicks the real ping's statistics.
    Check them out: `ping 127.0.0.1`
    See `man ping` for definitions.
    """
    pass #delete this and write (or copy from pa03)


def main() -> None:
    SERVER_HOSTNAME, SERVER_PORT, NUM_PINGS, TIMEOUT = parse_args()
    pass #delete this and write (or copy from pa03)


if __name__ == "__main__":
    main()
