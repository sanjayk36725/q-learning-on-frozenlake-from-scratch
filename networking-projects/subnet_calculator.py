"""Beginner-friendly IPv4 CIDR subnet calculator using only Python's standard library."""

from __future__ import annotations

import argparse
import ipaddress
import sys


def calculate_subnet(cidr: str) -> dict[str, str | int | bool]:
    """Return common subnet details for an IPv4 address/prefix."""
    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as exc:
        raise ValueError(f"Invalid address or CIDR prefix: {exc}") from exc

    if not isinstance(network, ipaddress.IPv4Network):
        raise ValueError("This calculator currently supports IPv4 only.")

    prefix = network.prefixlen
    if prefix <= 30:
        first_host = network.network_address + 1
        last_host = network.broadcast_address - 1
        usable_hosts = network.num_addresses - 2
    elif prefix == 31:
        # RFC 3021 point-to-point /31 networks use both addresses.
        first_host = network.network_address
        last_host = network.broadcast_address
        usable_hosts = 2
    else:  # /32 represents one individual IPv4 address.
        first_host = network.network_address
        last_host = network.network_address
        usable_hosts = 1

    input_ip = cidr.split("/", 1)[0].strip()
    return {
        "Input address": input_ip,
        "Network address": str(network.network_address),
        "CIDR prefix": f"/{prefix}",
        "Subnet mask": str(network.netmask),
        "Wildcard mask": str(network.hostmask),
        "Broadcast address": str(network.broadcast_address),
        "First usable address": str(first_host),
        "Last usable address": str(last_host),
        "Total addresses": network.num_addresses,
        "Usable host addresses": usable_hosts,
        "Private/reserved classification": "Private" if ipaddress.ip_address(input_ip).is_private else "Not private",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate IPv4 network details from an address in CIDR notation."
    )
    parser.add_argument(
        "cidr",
        nargs="?",
        help="IPv4 address/prefix, for example 192.168.1.10/24",
    )
    args = parser.parse_args()

    cidr = args.cidr or input("Enter IPv4 address/CIDR (example 192.168.1.10/24): ").strip()
    try:
        details = calculate_subnet(cidr)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print("\nIPv4 Subnet Details")
    print("-" * 34)
    for label, value in details.items():
        print(f"{label:<28} {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
