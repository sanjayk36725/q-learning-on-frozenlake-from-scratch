# Networking Projects Lab

Small, runnable projects for practicing Connectivity & Networking fundamentals. These examples live in a separate folder so they do not change the FrozenLake reinforcement-learning implementation.

## Projects

| Project | Concepts | How to run |
|---|---|---|
| [OSI Packet Journey](osi-packet-journey.html) | OSI 7 layers, encapsulation/decapsulation, PDUs, protocols | Open the HTML file in a browser |
| [IPv4 Subnet Calculator](subnet_calculator.py) | CIDR, subnet masks, network/broadcast addresses, usable hosts | `python subnet_calculator.py 192.168.1.10/24` |
| [DNS Lookup Tool](dns_lookup.py) | DNS name resolution, IPv4/IPv6 records, reverse lookup | `python dns_lookup.py example.com` |
| [TCP Echo Socket Demo](tcp-echo/README.md) | TCP sockets, client/server, ports, data exchange | Run server and client in two terminals |

## Requirements

- Python 3.10 or later for the Python examples
- The OSI visualizer needs a modern browser
- The Python projects use only the standard library; no pip packages are needed

## Suggested learning order

1. Explore the OSI visualizer and follow a request through encapsulation and decapsulation.
2. Run the subnet calculator with `192.168.1.10/24`, `10.0.0.1/8`, and `192.168.1.1/30`.
3. Resolve a hostname with the DNS tool, then try reverse lookup with an IP address.
4. Run the TCP echo server and client in separate terminals. Observe how the client sends bytes and the server replies.

## Safety

The TCP demo binds to **127.0.0.1 (localhost)** only, so it is intended for practice on your own machine. The DNS tool performs ordinary system name resolution. These labs are educational examples, not production network services.
