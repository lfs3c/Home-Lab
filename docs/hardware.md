# 🖥️ LF Home Lab — Hardware Overview

## 💻 Main Laptop — "LaptopU" (Ubuntu 24.04.3 LTS)
- **Model:** OMEN Gaming Laptop 17-db0xxx
- **CPU:** AMD Ryzen 7 8845HS (3.80 GHz, 8 cores, 16 threads)
- **GPU:** NVIDIA RTX 4070 Laptop GPU (8 GB VRAM)
- **RAM:** 32 GB (31.3 GB usable)
- **Storage:**
  - **SSD 1 (1 TB):** Windows 11
  - **SSD 2 (2 TB):** Ubuntu + shared storage + swap
- **Dual Boot:** Windows 11 ↔ Ubuntu 24.04 LTS (GRUB)
- **Main Purpose:** local AI/LLMs, development, testing, and virtualization

---

## 🖥️ Home Server — "<SERVER_HOSTNAME>"
- **Hardware:** Repurposed iMac
- **CPU:** Intel® Core™ i5 (~3.4 GHz, quad-core)
- **RAM:** 24 GB
- **GPU:** AMD Radeon
- **Disk:** 1 TB
- **OS:** Ubuntu 24.04 LTS (headless)
- **Main Purpose:** Docker services, automation, backups, scripts, and internal web tools

---

## 🧠 Other Devices
| Device | OS / Use | Notes |
|--------|-----------|-------|
| **Flipper Zero** | Custom firmware | Security testing and RF analysis |
| **Raspberry Pi 3B** | Raspberry Pi OS | Experiments / lightweight services |
| **Raspberry Pi 4B** | Raspberry Pi OS | NAS / personal cloud projects |

---

### 🔗 Network and Integration
- All systems are connected within a **secure private LAN**.
- Exact internal IP addresses, SSIDs, usernames, MAC addresses, serial numbers, and operational hostnames are intentionally omitted from this public repository.
- Local hostname resolution and Docker networks are used for service communication.
- Internal services are restricted by host and network firewalls.
- Shared storage volumes are used for backups and synchronization.
- Containers and services use isolated Docker networking as appropriate.
- Sensitive configuration (API keys, credentials, tokens, and private bindings) is supplied through environment variables or untracked configuration files and is never committed to this repository.
