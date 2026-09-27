# Home Lab

Hands-on documentation for a self-hosted infrastructure and cybersecurity lab.

This repository documents the infrastructure, security, self-hosted services, administration projects, and selected study material that contribute directly to the Home Lab. Personal desktop applications and unrelated personal projects are intentionally outside its scope.

## Repository Structure

- `infrastructure/` — physical and logical lab nodes, networking, access, and backup infrastructure.
- `services/` — verified self-hosted services.
- `security/` — hardening, auditing, and host-protection material.
- `projects/` — software and administration projects built for the lab.
- `studies/` — selected academic and technical study material.
- `legacy/` — historical implementations retained for reference.
- `docs/` — general lab documentation.

## Infrastructure

- [LF1](infrastructure/lf1/) — primary Home Lab server running Debian 12.
- [LaptopU](infrastructure/laptopu/) — Ubuntu workstation for development, virtualization, cybersecurity labs, local AI, and Home Lab administration.
- [Raspberry Pi 3](infrastructure/raspberry_pi_3/) — hardware node with no services currently documented.
- [Raspberry Pi 4](infrastructure/raspberry_pi_4/) — hardware node with no services currently documented.
- [Network](infrastructure/network/) — verified Home Lab network overview.
- [Access](infrastructure/access/) — supporting private-access and routing components.
- [Backup](infrastructure/backup/) — LF1 manual BorgBackup workflow and dedicated backup storage.

A public hardware summary is available in [docs/hardware.md](docs/hardware.md).

## Services

### Automation

- [n8n](services/automation/n8n/)

### Communication

- [Matrix / Synapse](services/communication/matrix_synapse/)

### Dashboard

- [Heimdall](services/dashboard/heimdall/)

### Documentation

- [Wiki.js](services/documentation/wikijs/)

### Infrastructure Management

- [NetBox](services/infrastructure/netbox/)
- [Portainer](services/management/portainer/)

### Media and Personal Cloud

- [Audiobookshelf](services/media/audiobookshelf/)
- [Jellyfin](services/media/jellyfin/)
- [Navidrome](services/media/navidrome/)
- [PhotoPrism](services/media/photoprism/)

### Monitoring

- [LibreNMS](services/monitoring/librenms/)
- [Zabbix](services/monitoring/zabbix/)

### Network

- [Pi-hole](services/network/pihole/)

Services are listed as current only after their live state has been verified. Supporting databases, caches, and similar dependencies are documented with the services that use them rather than treated automatically as independent Home Lab projects.

## Security

Security material is organized under [security/](security/).

Current areas include:

- Lynis auditing
- systemd security analysis
- hardening notes
- host-protection components

Historical security experiments are retained under `legacy/` when they no longer represent the current environment.

## Hermes and Administration Projects

- [Hermes](projects/hermes/) — Home Lab administration assistant architecture spanning the Hermes VM on LaptopU and controlled interfaces on LF1.
- [Hermes Control API](projects/hermes_control_api/) — active LF1-hosted control interface and current verified baseline.
- [MCP Server](projects/mcp_server/) — LF1-hosted MCP interface currently in development.

The Control API remains the verified baseline while MCP capabilities are developed and validated.

## Studies

Python coursework and exercises are preserved under [studies/python/](studies/python/) with filenames normalized to snake_case.

Study material is included selectively when it contributes to the technical history or skills represented by the lab.

## Legacy

Older implementations remain under [legacy/](legacy/) for historical and learning context.

Legacy content must not be interpreted as the current production state of the Home Lab. This includes the historical Raspberry Pi PhotoPrism deployment; the current PhotoPrism service is hosted on LF1.

## Documentation Principles

- Document verified current state rather than assumptions.
- Keep infrastructure and service documentation separate where practical.
- Treat dependencies as part of the service that uses them unless they have an independent Home Lab role.
- Keep personal projects and ordinary desktop applications outside the Home-Lab repository.
- Add implementation documentation as projects evolve instead of creating empty placeholder files.

## Public Repository Safety

Operational secrets, credentials, tokens, exact private addressing, SSIDs, MAC addresses, serial numbers, private repository paths, and other unnecessary sensitive infrastructure details are intentionally excluded from this public repository.

## License

CC0-1.0 unless otherwise specified.
