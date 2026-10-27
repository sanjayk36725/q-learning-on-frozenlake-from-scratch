# TCP Echo Client/Server

A small Python socket lab for learning the TCP connection model, ports, client/server roles, byte streams, and `sendall`/`recv`.

## Run it

Open two terminals from the repository root.

**Terminal 1 — start the server**

```bash
python networking-projects/tcp-echo/server.py
```

**Terminal 2 — start the client**

```bash
python networking-projects/tcp-echo/client.py
```

Type a message in the client; the server receives the bytes and sends them back. Type `/quit` to close the client. Press Ctrl+C in the server terminal to stop the server.

## What to observe

1. The server binds to TCP port 5000 on `127.0.0.1`.
2. The client connects using a TCP socket.
3. `sendall()` writes the message bytes to the TCP stream.
4. `recv()` reads the response bytes.
5. TCP provides an ordered byte stream; it does not preserve message boundaries by itself.

This educational server intentionally binds to localhost only. It is not a production server and is not reachable by other machines on the network.
