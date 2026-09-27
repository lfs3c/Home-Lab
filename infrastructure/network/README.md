# Home Lab Network

![Pi-hole](https://img.shields.io/badge/Pi--hole-DNS%20Filtering-96060C?logo=pi-hole&logoColor=white) ![UFW](https://img.shields.io/badge/UFW-Firewall-28A745?logo=ubuntu&logoColor=white) ![HAProxy](https://img.shields.io/badge/HAProxy-Routing-106DA9) ![SNMP](https://img.shields.io/badge/SNMP-Monitoring-5E5E5E)

This directory documents the network infrastructure that supports the Home Lab.

## Verified LF1 Connectivity

LF1 uses a wired Ethernet connection as its primary Home Lab network interface. Its wireless interface is currently inactive.

The host also maintains multiple software bridges created by Docker for isolated container networking.

## DNS

LF1 provides local DNS through the Pi-hole service hosted on the server. External and gateway DNS resolvers are configured as fallback paths.

Exact resolver addresses and private network addressing are intentionally excluded from this public documentation.

## VLANs

No VLAN interfaces are currently configured directly on LF1.

This statement describes only the verified LF1 host configuration and does not imply that VLANs are absent elsewhere in the network.

## Network Supporting Services

Verified network-related components on LF1 include:

- Pi-hole for DNS
- HAProxy for proxying and routing selected services
- Twingate Connector for private remote access
- ddclient for dynamic DNS updates
- SNMP for monitoring and infrastructure visibility
- Docker bridge networks for container workloads

## Host Firewall

LF1 uses UFW.

The verified baseline is:

- firewall enabled
- incoming traffic denied by default
- outgoing traffic allowed by default
- routed traffic denied by default
- firewall logging enabled

Individual firewall rules, exact source networks, private addresses, and exposed port mappings are intentionally excluded from this public overview.

## Physical Switching

The current LF1 inventory did not provide enough information to document the physical switch model, port assignments, or switch configuration.

Switch documentation will be added only after the physical device and its current configuration are verified.

## Public Repository Safety

This repository intentionally excludes private IP addresses, MAC addresses, SSIDs, public endpoint details, credentials, tokens, and other network information that is unnecessary for understanding the architecture.
