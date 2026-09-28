# Security

## Security Model

The LF1 MCP Server follows these principles:

1. least privilege;
2. read-only capabilities first;
3. explicit tools instead of generic execution;
4. separate authentication and network controls;
5. dedicated service identities;
6. secrets outside source control;
7. restricted boundaries around privileged subsystems.

## MCP Service Account

Production runs as:

    User=lf1-mcp
    Group=lf1-mcp

Validated effective supplementary groups:

    Groups: 993

The MCP service therefore does not inherit the human administrator's Docker or sudo-related groups.

Systemd currently enforces:

    NoNewPrivileges=yes

Additional systemd sandboxing can be introduced incrementally after compatibility testing.

## Authentication

Hermes authenticates to the MCP server using a Bearer token.

The token is stored outside the repository in:

    /etc/lf1-mcp/credentials.env

The credential file is root-owned and must never be committed to Git.

## Docker Security Boundary

The MCP service cannot directly access:

    /var/run/docker.sock

Docker observation passes through a restricted Docker Socket Proxy.

The proxy:

- binds only to 127.0.0.1:2375;
- permits container listing;
- blocks mutating POST operations;
- blocks container logs;
- blocks container filesystem export;
- blocks archive access;
- blocks process listing through top;
- blocks images;
- blocks volumes;
- blocks networks.

The following boundary tests have been validated:

    GET  /_ping                         allowed
    GET  /containers/json?all=true     allowed

    GET  /containers/<id>/logs         blocked
    GET  /containers/<id>/top          blocked
    GET  /containers/<id>/export       blocked
    GET  /images/json                   blocked
    GET  /volumes                       blocked
    GET  /networks                      blocked

    POST /containers/<id>/stop         blocked
    POST /containers/<id>/restart      blocked

Blocked requests returned HTTP 403 during validation.

## Explicit Capability Rule

Hermes is not given:

- arbitrary shell execution;
- arbitrary Docker API access;
- arbitrary URLs;
- arbitrary HTTP methods;
- arbitrary operating-system commands;
- direct Docker socket access;
- privilege escalation capabilities.

Each future administrative capability must receive its own security design and review.
