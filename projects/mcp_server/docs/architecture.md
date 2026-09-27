# Architecture

## Milestone 1 data path

Hermes VM → MCP Streamable HTTP + Bearer token → NAT boundary → LF1 host firewall → LF1 MCP Server → explicit read-only tools → authoritative LF1 host state.

The MCP server runs on LF1 and is kept online by systemd. Hermes is an MCP client running in a separate VM.

The first end-to-end milestone was completed when Hermes remotely discovered and called `system_health` through the authenticated MCP connection and received live LF1 data.

The Hermes Control API is frozen and is not part of this MCP request path.
