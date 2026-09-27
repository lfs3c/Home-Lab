# LaptopU

LaptopU is the primary Home Lab workstation for development, virtualization, cybersecurity labs, local AI workloads, and administration.

## Verified Platform

- Hardware: HP OMEN Gaming Laptop 17-db0xxx
- CPU: AMD Ryzen 7 8845HS
- CPU topology: 8 cores / 16 threads
- Memory: approximately 32 GB
- GPU: NVIDIA GeForce RTX 4070 Laptop GPU with 8 GB VRAM
- Operating system: Ubuntu 24.04.5 LTS
- Architecture: x86_64

## Storage

LaptopU uses separate physical NVMe storage for Linux and Windows:

- approximately 2 TB NVMe SSD for Ubuntu
- approximately 1 TB NVMe SSD containing Windows

This allows Linux/Home Lab work and Windows use to remain separated at the storage level.

## Virtualization

LaptopU uses KVM/QEMU through libvirt.

The current inventory includes several persistent virtual machines used for development, cybersecurity study, operating-system testing, and Home Lab work.

Two persistent libvirt networks are configured:

- `default`
- `Internal_network`

Exact private addressing and virtual interface identifiers are intentionally excluded.

## Hermes VM

The VM currently named `ubuntu_ai_agent` is the Hermes VM.

Verified allocation:

- 8 virtual CPUs
- 12 GiB memory
- persistent libvirt domain
- AppArmor security model
- connected through the libvirt `default` network
- autostart disabled

Hermes itself is documented under `projects/hermes/`. The Hermes Control API and developing MCP Server run on LF1.

## Home Lab Workstation Services

Verified active components relevant to the lab include:

- Docker
- libvirt
- Ollama
- HAProxy
- Twingate Connector
- SSH tunnel integration for Home Lab access
- auditd
- ClamAV
- Tor
- SMART monitoring

These are supporting workstation capabilities and are not automatically treated as independent Home Lab services.

## Docker Workloads

LaptopU also runs Docker workloads for development, study, design tooling, local AI interfaces, and personal projects.

A running container does not automatically make a project part of the Home-Lab repository. Personal projects and unrelated desktop applications are intentionally outside this repository's scope.

## Documentation Policy

This public documentation excludes credentials, tokens, MAC addresses, exact private addressing, personal application inventories, and other unnecessary operational details.
