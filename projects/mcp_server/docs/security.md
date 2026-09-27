# Security

## Current controls

- least privilege and read-only tools first
- explicit MCP capabilities; no generic shell or arbitrary command execution
- Bearer-token authentication with constant-time secret comparison
- credentials supplied through the runtime environment and stored outside Git
- host firewall restricts access to the MCP TCP port
- authenticated tokens scoped to `lf1:read`
- token resource validation enabled

## Network boundary

The Hermes VM reaches LF1 through a NAT boundary. Multiple clients can appear with the same translated source address, so source-IP filtering is only one security layer. Bearer authentication provides an independent authentication layer.

## Future privileged capabilities

Write, administrative or destructive tools require separate threat analysis, authorization design, validation and stronger testing before exposure.
