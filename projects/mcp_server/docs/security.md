# Security

## Security Model

The LF1 MCP Server follows these principles:

1. least privilege
2. read-only capabilities first
3. explicit tools instead of generic execution
4. separate authentication and network controls
5. dedicated service identities
6. secrets outside source control
7. restricted boundaries around privileged subsystems

## MCP Service Account

Production runs under the dedicated `lf1-mcp` service identity.

The MCP service does not inherit the human administrator's Docker or sudo-related groups.

Systemd currently enforces:

    NoNewPrivileges=yes

Additional systemd sandboxing can be introduced incrementally after compatibility testing.

## Authentication

Hermes authenticates to the MCP server using a Bearer token.

The token is stored in a root-owned system credential file outside the repository. The exact credential value is never committed to Git.

Public documentation intentionally omits exact LAN addresses, ports, personal development paths, and credential values.

## Docker Security Boundary

The MCP service cannot directly access the Docker socket.

Docker observation passes through a restricted localhost-only Docker Socket Proxy.

The proxy permits the required container-listing operation and blocks tested sensitive/state-changing operations including logs, filesystem export, archive access, process listing, images, volumes, networks, stop, and restart.

Blocked requests returned HTTP 403 during validation.

## Storage Capability Boundary

`storage_list` is read-only.

The production `lf1-mcp` service account can read the required storage metadata without additional groups, sudo permissions, or a privileged proxy.

The implementation executes only fixed command argument lists for `lsblk` and `df`.

Hermes cannot provide executable names, command-line arguments, device names, mount points, or shell expressions. No `shell=True` execution is used.

Storage observability therefore does not add a generic command-execution capability to the MCP server.

## Explicit Capability Rule

Hermes is not given arbitrary shell execution, arbitrary Docker API access, arbitrary URLs or HTTP methods, arbitrary operating-system commands, direct Docker socket access, or privilege-escalation capabilities.

Each future administrative capability must receive its own security design and review.
