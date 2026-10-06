![Status](https://img.shields.io/badge/Status-Active%20Development-28A745) ![MCP](https://img.shields.io/badge/MCP-Server-6C63FF) ![LF1](https://img.shields.io/badge/Host-LF1-A81D33?logo=debian&logoColor=white) ![Security](https://img.shields.io/badge/Security-Least%20Privilege-28A745) ![Observability](https://img.shields.io/badge/Observability-LibreNMS-0099CC)

# MCP Server - LF1

Security-focused MCP server that provides ChatGPT and other explicitly authorized MCP clients with controlled access to the LF1 Home Lab through explicit, least-privilege capabilities.

## Overview

MCP Server - LF1 exposes narrow, purpose-built capabilities for observing and administering a self-hosted Home Lab without giving AI clients unrestricted shell or infrastructure access.

ChatGPT is the primary MCP client, while the server remains compatible with other explicitly authorized MCP clients.

Current capabilities focus on read-only observability across Linux, Docker, systemd, storage, and LibreNMS.

Current end-to-end path:

    Authorized MCP client
        |
        | MCP Streamable HTTP + Bearer authentication
        v
    MCP Server - LF1
        |
        +-- Linux host observability
        +-- Docker container observability
        +-- systemd service observability
        +-- storage observability
        +-- LibreNMS network observability

Exact LAN addresses, external access details, personal development paths, and credentials are intentionally omitted from public documentation.

## Current MCP Tools

### ping

Confirms that MCP Server - LF1 is responding.

### system_health

Returns read-only host information from authoritative local Linux sources, including hostname, uptime, load averages, memory usage, and root filesystem usage.

### containers_list

Returns a read-only Docker container inventory with container name, image, state, status, and summary counts.

The MCP process does not have direct access to the Docker socket. Docker information is obtained through a restricted local socket proxy.

### storage_list

Returns normalized read-only storage information, including physical disks, partitions, filesystem types, mount points, capacity, available space, and usage.

New disks attached to LF1 are discovered dynamically and do not require source-code changes.

### services_list

Returns read-only systemd service observability with normalized service information and summary counts.

Service discovery comes from systemd rather than a hard-coded inventory. The capability does not expose arbitrary `systemctl` execution or generic shell access.

### network_devices_list

Returns a normalized read-only view of network devices known by LibreNMS, including device identity, operating system, status, disabled/ignored state, and summary counts.

### network_device_status

Provides normalized, read-only network device health through the LibreNMS integration, including availability, outages, interfaces, sensors, alerts, and source metadata when available.

LibreNMS credentials remain outside the repository, and MCP clients receive normalized capability output rather than generic LibreNMS API access.

## Security Principles

- least privilege
- read-only first
- explicit MCP capabilities
- no generic shell execution
- no arbitrary command execution
- dedicated MCP service identity
- secrets outside the repository
- network restriction plus application authentication
- restricted intermediaries for privileged subsystems
- human authorization for administrative capabilities

Write capabilities are developed and reviewed separately from the production read-only interface.

## Runtime

MCP Server - LF1 runs as a dedicated systemd service under a restricted service identity. Development and production environments are separated.

Deployment-specific addresses, credentials, and private filesystem locations are intentionally excluded from this public documentation.

## Documentation

Detailed architecture, security, testing, operations, LibreNMS integration, and project history are maintained under `docs/`.

Development milestones and implementation history belong in the roadmap and changelog rather than the public project status.

## Deployment Assets

Deployment assets for restricted supporting components are stored under `deploy/`.

## Runtime Configuration

Runtime configuration is supplied through environment variables and deployment-specific configuration outside source control. Authentication tokens, monitoring credentials, and other secrets must remain outside Git.
