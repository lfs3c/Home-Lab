# initial_audit_lynis (Debian Server) — **Sanitized for Public GitHub**

> **Source:** First Lynis security scan after fresh setup  
> **Date of audit:** 2025-10-18 (America/New_York)  
> **Tool:** Lynis 3.0.8  
> **Command used:** `sudo lynis audit system`

---

## 🔒 Redaction & Privacy Notes

This public copy intentionally **removes or obfuscates** sensitive data:

- Hostname → `<redacted_hostname>`
- IP addresses / DNS resolvers → `<redacted_ip>`
- SSID / Wi-Fi identifiers → `<redacted_ssid>`
- Usernames / emails / MAC addresses / serials → redacted if present
- Paths that may reveal personal structure are kept when generic and expected on Debian systems

> If you fork or reuse, **double-check** no secrets are exposed in pasted logs or screenshots.

---

## 🧾 TL;DR (Quick Summary)

- **Hardening Index:** **65**
- **Tests Performed:** 249
- **Plugins Enabled:** 1 (`debian`)
- **Warnings:** **1** (`systemd-timesyncd` not recently synchronized)
- **Suggestions:** **48** (password policy, SSH hardening, partitions for `/home`, `/tmp`, `/var`, disable unused protocols/drivers, enable accounting/audit/file-integrity, etc.)
- **Firewall:** Present
- **Malware Scanner:** Not installed (suggest installing e.g., `rkhunter`, `chkrootkit`, or OSSEC/Wazuh)

---

## 📌 Reproduce Locally

```bash
# Update lynis definitions (optional) and run a full audit
sudo apt update
sudo apt install -y lynis
sudo lynis audit system | tee ~/lynis_initial_audit_$(date +%F).log
```

## 🗂️ Full Report (sanitized)

[**Initial report**](initial_audit_lynis.txt)

## ✅ Next Steps (from findings)

> **Living document:** As I apply hardening changes, I will **update this same folder** (adding dates and notes under each item).  
> Periodically, I will **re-run Lynis** and commit a **new sanitized audit report** to track progress over time.

- **Apply SSH hardening** (parameters suggested by Lynis).
- Consider **separate partitions** for `/home`, `/tmp`, `/var`.
- Enable **process/accounting & audit** (`acct`, `sysstat`, `auditd`).
- Add a **file integrity** tool (AIDE / rkhunter / chkrootkit / Wazuh).
- Review **iptables** for unused rules; disable **unused protocols** (`dccp` / `sctp` / `rds` / `tipc`) and **USB/FireWire storage** if not needed.
- Set **password policy** (rounds / age / `umask`) and **GRUB password**.
- Ensure **time sync** is healthy (`systemd-timesyncd`).

> I will re-run Lynis after significant changes and commit a **new sanitized report** for comparison.

---

### 🛠️ How I’ll Track Progress

- Each item above will get a dated sub-entry like:
  - `2025-10-18 — Applied XYZ (command/summary) — Result: OK/needs review`
- If an item spans multiple steps, I’ll add nested bullets with short commands or config paths changed.

---

### 🔁 Re-run Audit (for history)

```bash
# Save a dated log of the new audit
sudo lynis audit system | tee ~/lynis_audit_$(date +%F).log
```

New reports will be sanitized (redacting hostnames, IPs, SSIDs, and other identifiers) before publishing.
