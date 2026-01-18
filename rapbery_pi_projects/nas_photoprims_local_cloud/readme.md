# NAS + Samba + PhotoPrism

## Overview

This document provides a **complete, end‑to‑end technical record** of the creation of a self‑hosted **NAS with Samba and PhotoPrism**, deployed on a **Raspberry Pi 4** (4 GB RAM).

The goal of this documentation is **reproducibility** and **clarity**. Every step listed here was executed during the project. No assumptions, shortcuts, or undocumented changes were made.

---

## Hardware Used

### Raspberry Pi 4 (NAS Core)
- Model: Raspberry Pi 4 Model B
- RAM: 4 GB
- Storage:
  - microSD (64 GB) — operating system only
  - External HDD (2 TB) — all data and services
- Network: Wi‑Fi only (Ethernet disabled)

---

## Operating System

- OS: Raspberry Pi OS Lite (64‑bit)
- Hostname: `pi4-nas`
- User: `USER`
- Timezone: `America/New_York`
- Locale: `en_US.UTF-8`
- Access mode: Headless (SSH)
