# Home Lab

Hands-on documentation for a self-hosted infrastructure and cybersecurity lab.

This repository focuses on infrastructure, security, self-hosted services, technical projects, and selected study material that contributes to the lab. Personal desktop applications and unrelated software are intentionally outside its scope.

## Repository Structure

- `infrastructure/` — physical and logical lab nodes.
- `services/` — documented self-hosted services.
- `security/` — hardening and auditing material.
- `projects/` — software and automation projects built for the lab.
- `studies/` — selected academic and technical study material.
- `legacy/` — historical implementations retained for reference.
- `docs/` — general lab documentation.

## Infrastructure

### LF1

LF1 is the primary home server. Its current service inventory will be documented only after the live environment has been verified.

### LaptopU

LaptopU is used for development, testing, virtualization, and local AI workloads. Detailed documentation will be added from verified system state.

### Raspberry Pi 3

The Raspberry Pi 3 is part of the lab hardware inventory. No services are currently documented for this node.

### Raspberry Pi 4

The Raspberry Pi 4 is part of the lab hardware inventory. No services are currently documented for this node.

## Documented Services

- [Matrix / Synapse](services/communication/matrix_synapse/) — existing Matrix/Synapse deployment documentation.

## Security

Existing hardening and auditing material is organized under `security/`, including Lynis and systemd security analysis.

Historical Raspberry Pi security experiments are retained under `legacy/` rather than presented as current deployments.

## Projects

- [MCP Server](projects/mcp_server/) — planned self-hosted MCP interface for controlled Home Lab administration and observation.

## Studies

Python coursework and exercises are preserved under [`studies/python/`](studies/python/) with filenames normalized to snake_case.

## Legacy

Older implementations remain available for historical and learning context. Content under `legacy/` should not be interpreted as the current production state of the Home Lab.

## Public Repository Safety

Operational secrets, credentials, exact private addressing, SSIDs, MAC addresses, serial numbers, and other sensitive infrastructure details are intentionally excluded from this public repository.

## License

CC0-1.0 unless otherwise specified.
