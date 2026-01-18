# 🖥️ LF Home Lab — Hardware Overview

## 💻 Main Laptop — "LaptopU" (Ubuntu 24.04.3 LTS)
- **Model:** OMEN Gaming Laptop 17-db0xxx  
- **CPU:** AMD Ryzen 7 8845HS (3.80 GHz, 8 cores, 16 threads)  
- **GPU:** NVIDIA RTX 4070 Laptop GPU (8 GB VRAM)  
- **RAM:** 32 GB (31.3 GB usable)  
- **Storage:**
  - **SSD 1 (1 TB):** Windows 11 (C:)  
  - **SSD 2 (2 TB):** Ubuntu root (1.58 TB ext4) + Shared NTFS (244 GB) + Swap (31 GB)
- **Dual Boot:** Windows 11 Home 24H2 ↔ Ubuntu 24.04.3 LTS (GRUB)
- **Main Purpose:**  
  - AI generation (Stable Diffusion, ComfyUI)  
  - Local LLMs (Open WebUI + Ollama)  
  - Voice tools (Coqui TTS, RVC)  
  - Development and testing
  - Virtualizations (Virtual Machine Manager)  

---

## 🖥️ Home Server — "leandro-imac"
- **Hardware:** iMac (repurposed as server)  
- **CPU:** Intel® Core™ i5 (~3.4 GHz, quad-core)  
- **RAM:** 24 GB  
- **GPU:** AMD Radeon (native iMac GPU)  
- **Disk:** 1 TB HDD  
- **OS:** Ubuntu 24.04.1 LTS (headless)
- **Main Purpose:**  
  - n8n (automation)  
  - Docker containers (Portainer, Heimdall, etc.)  
  - Backups and scripts  
  - Internal web tools  

---

## 🧠 Other Devices
| Device | OS / Use | Notes |
|--------|-----------|-------|
| **Flipper Zero** | Custom firmware | Security testing and RF analysis |
| **Raspberry Pi 3B** | Raspberry Pi OS | Experiments / lightweight services |
| **Raspberry Pi 4B** | Raspberry Pi OS | NAS / Personal and Private Cloud service for images/videos |

---

### 🔗 Network and Integration
- All systems are connected within a **secure private LAN**.
- Local hostname resolution and Docker networks are used for service communication.
- **Main services** (AI tools, automation, TTS, etc.) are **accessible only within the internal network** — no external ports are exposed.
- The **firewall (UFW + router-level NAT)** restricts inbound connections from the internet.
- Shared storage volumes are mounted between machines for backups and synchronization.
- All containers and services are isolated using **Docker Bridge and Host networks**, depending on performance requirements.
- Sensitive configurations (API keys, credentials, IP bindings) are stored securely in **.env files** (not tracked in Git).
