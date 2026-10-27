"""Interactive TCP client for the localhost echo server."""

from __future__ import annotations

import argparse
import socket


def main() -> int:
    parser = argparse.ArgumentParser(description="Connect to the local TCP echo server.")
    parser.add_argument("--port", type=int, default=5000, help="TCP port (default: 5000)")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")

    try:
        with socket.create_connection(("127.0.0.1", args.port), timeout=5) as client:
            print(f"Connected to 127.0.0.1:{args.port}. Type /quit to exit.")
            while True:
                message = input("> ")
                if message.strip().lower() == "/quit":
                    break
                payload = message.encode("utf-8")
                client.sendall(payload)
                reply = client.recv(4096)
                if not reply:
                    print("Server closed the connection.")
                    break
                print("Echo:", reply.decode("utf-8", errors="replace"))
    except (ConnectionRefusedError, TimeoutError, OSError) as exc:
        print(f"Could not connect to the server: {exc}")
        print("Start server.py in another terminal first.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
