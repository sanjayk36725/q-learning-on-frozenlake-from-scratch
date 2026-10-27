"""Resolve DNS names and optionally perform a reverse lookup using the standard library."""

from __future__ import annotations

import argparse
import ipaddress
import socket
import sys


def lookup_host(hostname: str) -> list[tuple[str, str]]:
    """Return unique (IP version, address) pairs for a hostname."""
    results: set[tuple[str, str]] = set()
    for family, _socktype, _proto, _canonname, sockaddr in socket.getaddrinfo(
        hostname, None, type=socket.SOCK_STREAM
    ):
        address = sockaddr[0]
        version = "IPv6" if family == socket.AF_INET6 else "IPv4"
        results.add((version, address))
    return sorted(results, key=lambda item: (item[0], item[1]))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Look up hostname IP addresses or perform a reverse DNS lookup."
    )
    parser.add_argument("target", help="A hostname (example.com) or IPv4/IPv6 address")
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Treat target as an IP address and ask for its reverse DNS name",
    )
    args = parser.parse_args()

    try:
        if args.reverse:
            address = str(ipaddress.ip_address(args.target))
            hostname, aliases, _addresses = socket.gethostbyaddr(address)
            print(f"IP address: {address}")
            print(f"Canonical hostname: {hostname}")
            if aliases:
                print("Aliases: " + ", ".join(aliases))
        else:
            answers = lookup_host(args.target)
            if not answers:
                print(f"No addresses returned for {args.target}")
                return 1
            print(f"DNS/system resolver results for {args.target}:")
            for version, address in answers:
                print(f"  {version:<4} {address}")
            print("\nNote: results depend on your operating system's configured resolver.")
    except (socket.gaierror, socket.herror, ValueError) as exc:
        print(f"Lookup failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
