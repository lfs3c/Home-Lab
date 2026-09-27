# Home Lab Hardware Overview

This document provides a public hardware overview of the primary Home Lab nodes. Exact serial numbers, MAC addresses, private addressing, and other unnecessary identifiers are intentionally excluded.

## LaptopU

- **Model:** HP OMEN Gaming Laptop 17-db0xxx
- **CPU:** AMD Ryzen 7 8845HS, 8 cores / 16 threads
- **GPU:** NVIDIA GeForce RTX 4070 Laptop GPU, 8 GB VRAM
- **RAM:** approximately 32 GB
- **Storage:**
  - approximately 2 TB NVMe SSD — Ubuntu
  - approximately 1 TB NVMe SSD — Windows
- **Operating system:** Ubuntu 24.04.5 LTS
- **Primary role:** development, virtualization, cybersecurity labs, local AI workloads, and Home Lab administration

Detailed documentation: [LaptopU](../infrastructure/laptopu/)

## LF1

- **Hardware platform:** Apple iMac14,2
- **CPU:** Intel Core i5-4570, 4 cores / 4 threads
- **Architecture:** x86_64
- **System storage:** approximately 1 TB
- **Additional storage:** dedicated PhotoPrism data storage and dedicated external backup storage
- **Operating system:** Debian GNU/Linux 12 (Bookworm)
- **Primary role:** self-hosted services, monitoring, automation, communication, network services, backups, and Home Lab administration

Detailed documentation: [LF1](../infrastructure/lf1/)

## Raspberry Pi 3

The Raspberry Pi 3 is part of the hardware inventory. No services are currently documented for this node.

Detailed documentation: [Raspberry Pi 3](../infrastructure/raspberry_pi_3/)

## Raspberry Pi 4

The Raspberry Pi 4 is part of the hardware inventory. No services are currently documented for this node.

Detailed documentation: [Raspberry Pi 4](../infrastructure/raspberry_pi_4/)

## Network and Integration

Home Lab systems use private networking, host firewalls, container networks, and controlled remote-access mechanisms as appropriate.

Detailed network documentation: [Home Lab Network](../infrastructure/network/)

Sensitive configuration such as credentials, tokens, exact private addressing, MAC addresses, and private bindings is intentionally excluded from this public repository.
