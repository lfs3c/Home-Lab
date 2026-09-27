# 🧩 Item 7 — Systemd Service Hardening (systemd-analyze security)

## 🔐 Objective
Reduce the attack surface of critical systemd services using native sandboxing directives.  
Target: **measurable security improvement** without breaking SSH, networking, or automation.

---

## ⚙️ Hardened Services (Before → After)

| Service | Before | After | Δ | Status |
|----------|--------|-------|----|--------|
| ssh.service | 9.6 UNSAFE | 8.4 EXPOSED | −1.2 | ✅ Functional |
| cron.service | 9.6 UNSAFE | 7.0 MEDIUM | −2.6 | ✅ Functional |
| NetworkManager.service | 7.8 EXPOSED | 5.9 MEDIUM | −1.9 | ✅ Functional |
| fail2ban.service | 9.6 UNSAFE | 5.5 MEDIUM | −4.1 | ✅ Functional |

**Average improvement:** ≈ 27% → Secure Home-Server Baseline 🏠🔒

---

## 🧠 Methodology

1. **Baseline assessment:**
```
   sudo systemd-analyze security --no-pager > ~/server_hardening/reports/security_report_initial.txt
```
2. **Apply hardening overrides to each critical service in:**
```
  /etc/systemd/system/<service>.d/override.conf
```

3. **Re-evaluate and compare results:**
```
  sudo systemd-analyze security <service>
```

4. **Document all results in:**
```
  server_hardening_tracker.xlsx → sheet "Item 7 – systemd services"
```

## 🔧 Example Override Configuration
```
[Service]
PrivateTmp=yes
ProtectSystem=full
ProtectHome=read-only
ProtectKernelTunables=yes
ProtectKernelModules=yes
ProtectControlGroups=yes
ProtectProc=invisible
LockPersonality=yes
ProtectClock=yes
ProtectHostname=yes
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
CapabilityBoundingSet=CAP_NET_BIND_SERVICE CAP_SETUID CAP_SETGID
```

**Adjust per service — for example:**
```
ProtectHome=no for SSH
add AF_NETLINK for NetworkManager or fail2ban
```

## 📊 Artifacts and Evidence
- server_hardening_tracker.xlsx — sheet Item 7 – systemd services
- Embedded Before vs After bar chart (exposure level comparison)

Screenshots of:
- systemd-analyze security --no-pager
- final status line of each service (e.g. fail2ban.service: 5.5 MEDIUM)
- spreadsheet chart view

## 👤 Author
- Leandro Correia de Freitas
- Cybersecurity Student · Home Lab Builder
