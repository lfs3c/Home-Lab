# Raspberry Pi 3B Blue Team Sensor

## Overview

This document provides a **technical record** of a lightweight **Blue Team sensor** built on a **Raspberry Pi 3 Model B**.

The sensor was created to receive and centralize logs from another host in the homelab environment using `rsyslog`.

The goal of this documentation is **clarity** and **reproducibility**. The project is intentionally simple and focused on visibility first, before adding more advanced detection or alerting components.

---

## Hardware Used

### Raspberry Pi 3 Model B

- Model: Raspberry Pi 3 Model B
- RAM: 1 GB
- Role: Passive log receiver
- Access mode: Headless
- Network: Wi-Fi only

---

## Operating System

- OS: `<distribution / release>`
- Hostname: `pi3-sensor`
- User: `<username>`
- Timezone: `<timezone>`
- Locale: `<locale>`
- Access mode: SSH

---

## Project Objective

This sensor was designed to provide a dedicated host for:

- receiving remote logs
- centralizing authentication events
- supporting manual log analysis
- creating a separated monitoring point inside the local network

Instead of starting with a full SIEM stack, this project focuses on establishing a stable logging pipeline on low-cost hardware.

---

## Architecture

### Hosts

- **Sensor / Receiver:** `Raspberry pi3-sensor` (`192.168.50.x`)
- **Log Source / Sender:** `Raspberry pi4-nas` (`192.168.50.x`)

### Log Transport

- Protocol: Syslog
- Port: `UDP 514`
- Service: `rsyslog`
- Network: Internal LAN

### Log Flow

```text
pi4-nas  --->  pi3-sensor
   syslog UDP 514
```

Logs received by the sensor are stored locally for later review and investigation.

Example log path:

```text
/var/log/remote/pi4-nas/syslog.log
```

---

## Main Components

The current sensor is based on the following components:

- `rsyslog` for remote log collection
- `UFW` for firewall restriction
- `Fail2Ban` for basic SSH protection
- `sysctl` hardening for network-related kernel settings

This setup keeps the system lightweight and easy to maintain on Raspberry Pi hardware.

---

## Security Design

This project follows a simple security model.

### Passive Monitoring

The sensor works only as a **passive receiver**.

It does not:

- inspect traffic inline
- forward production traffic
- interfere with the monitored host

### Firewall Exposure

Only the required services should remain exposed:

- `SSH` on port `22`
- `Syslog` on `UDP 514` from trusted internal hosts

### SSH Hardening

- root login disabled
- limited authentication attempts
- reduced attack surface

### Host Hardening

- minimal installed software
- no graphical interface
- network hardening with `sysctl`

---

## Detection Use

At the current stage, this project is used for **manual log analysis**.

Typical checks include:

- failed SSH logins
- authentication anomalies
- event timeline review

Example:

```bash
grep "Failed password" /var/log/remote/pi4-nas/syslog.log
```

This approach is simple, but already useful for visibility and investigation inside the homelab.

---

## Current Limitations

This project does not currently include:

- real-time alerting
- SIEM integration
- IDS or IPS components
- guaranteed delivery of logs, since syslog uses UDP
- automated parsing and enrichment

---

## Future Improvements

Possible next steps for this project:

- separate authentication and system logs more clearly
- create basic alert rules
- test integration with tools such as Wazuh, ELK, or Splunk
- move to encrypted log forwarding
- add dashboards for easier visualization

---

## Notes

Some values in this document were intentionally generalized for public posting.

Examples:

- usernames
- exact OS version
- local path variations
- internal IP addressing
- detailed firewall rules

These items can be replaced later if a more complete public version of the project is needed.

---

## Conclusion

This Raspberry Pi Blue Team sensor is a small but practical project focused on centralized logging, system visibility, and baseline hardening.

It is not meant to be a complete security monitoring platform, but it provides a solid starting point for future expansion into alerting, detection, and log analysis workflows.
	
