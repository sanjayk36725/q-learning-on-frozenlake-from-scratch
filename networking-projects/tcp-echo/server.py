"""A simple, threaded TCP echo server bound to localhost for safe practice."""

from __future__ import annotations

import argparse
import socket
import threading


BUFFER_SIZE = 4096


def handle_client(connection: socket.socket, address: tuple[str, int]) -> None:
    print(f"Client connected: {address[0]}:{address[1]}")
    with connection:
        while True:
            data = connection.recv(BUFFER_SIZE)
            if not data:
                break
            print(f"Received {len(data)} bytes: {data!r}")
            connection.sendall(data)
    print(f"Client disconnected: {address[0]}:{address[1]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Localhost-only TCP echo server.")
    parser.add_argument("--port", type=int, default=5000, help="TCP port (default: 5000)")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")

    # Keep the example local-only; it does not listen on external network interfaces.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", args.port))
        server.listen()
        print(f"TCP echo server listening on 127.0.0.1:{args.port}")
        print("Press Ctrl+C to stop.")
        try:
            while True:
                connection, address = server.accept()
                threading.Thread(
                    target=handle_client,
                    args=(connection, address),
                    daemon=True,
                ).start()
        except KeyboardInterrupt:
            print("\nStopping server.")


if __name__ == "__main__":
    main()
