# 🖥️ Debian 12 Wi-Fi Setup on Apple iMac (Broadcom chipset)

![Legacy](https://img.shields.io/badge/Status-Legacy-lightgrey) ![Debian](https://img.shields.io/badge/Debian-12%20Bookworm-A81D33?logo=debian&logoColor=white) ![Network](https://img.shields.io/badge/Broadcom-Wi--Fi-555555)

> Apple hardware often uses Broadcom Wi-Fi chipsets which are not supported by Debian’s default installer.  
> This guide documents how I installed Debian 12 (Bookworm) on an Apple iMac, enabled Wi-Fi, and configured NetworkManager for persistent connectivity.  
> All SSIDs, passwords, and private IPs have been replaced with placeholders for security.

---

## ⚙️ 1. System summary

- **Hardware:** Apple iMac (Broadcom BCM43xx)
- **OS:** Debian 12 (Bookworm, minimal install)
- **Goal:** Enable Broadcom Wi-Fi (`brcmfmac`) and make it persistent
- **Network Manager:** `nmcli` (CLI tool for NetworkManager)

---

## ⚙️ 2. Prepare system and connect via Ethernet

```
# Check network interfaces
ip link

# Obtain IP via DHCP (Ethernet)
sudo dhclient -v enp4s0f0

# Test connectivity
ping -c 3 8.8.8.8
```

## 🧰 3. Fix APT sources and enable non-free rep

```
# Remove CD-ROM repo if present
sudo sed -i '/cdrom/d' /etc/apt/sources.list

# Add official Debian repositories (with non-free firmware)
sudo bash -c 'cat > /etc/apt/sources.list <<EOF
deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
deb http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
deb http://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware
EOF'

# Update packages
sudo apt update && sudo apt upgrade -y
```

## 📦 4. Install Broadcom firmware and NetworkManager

```
sudo apt install firmware-brcm80211 firmware-linux-nonfree network-manager -y
```

## 🚫 5. Blacklist conflicting Broadcom drivers

```
echo -e "blacklist bcma\nblacklist b43\nblacklist brcmsmac\nblacklist ssb" | sudo tee /etc/modprobe.d/broadcom-blacklist.conf
sudo update-initramfs -u
```

## 🔁 6. Load Broadcom Wi-Fi driver

```
sudo modprobe -r brcmfmac || true
sudo modprobe brcmfmac
dmesg | grep -i brcm
```
Expected line:
```
usbcore: registered new interface driver brcmfmac
```

## ⚙️ 7. Enable and start NetworkManager

```
sudo systemctl enable NetworkManager
sudo systemctl start NetworkManager
sudo systemctl status NetworkManager
```

## 🧹 8. Clean up old configurations (prevent conflict)

```
# Comment out manual entries in /etc/network/interfaces
sudo sed -i '/wlan0/d' /etc/network/interfaces
sudo rm -f /etc/network/interfaces.d/wlan0
```

## 📡 9. Scan and connect to Wi-Fi

```
# List networks
sudo nmcli device wifi list

# Connect to your network (replace placeholders)
sudo nmcli device wifi connect "<SSID>" password "<PASSWORD>" ifname wlp3s0

# Verify status
nmcli device status
```
Expected output:
```
wlp3s0  wifi  connected  <SSID>
```

## 🌐 10. Configure DNS and routing

```
sudo nmcli connection modify "<SSID>" ipv4.dns "8.8.8.8,1.1.1.1"
sudo nmcli connection modify "<SSID>" ipv4.never-default no
sudo nmcli connection up "<SSID>"

# Check DNS file
cat /etc/resolv.conf
```

## 🔧 11. Disable Ethernet autoconnect (optional)

```
# Find wired connection name
nmcli connection show

# Disable autoconnect (replace if needed)
sudo nmcli connection modify "Wired connection 1" connection.autoconnect no
```

## 🔁 12. Reboot and validate

```
sudo reboot
```
After reboot:
```
nmcli device status
ip route
ping -c 3 8.8.8.8
ping -c 3 google.com
```
✅ Expected:
```
wlp3s0  wifi  connected  <SSID>
```

## 🧩 Troubleshooting quick reference

| Problem                                | Cause                         | Fix                                                                                 |
| -------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------- |
| `Destination Host Unreachable`         | Wrong default route           | `sudo ip route del default && sudo ip route add default via <GATEWAY_IP> dev wlp3s0` |
| `Temporary failure in name resolution` | DNS missing                   | `sudo nmcli connection modify "<SSID>" ipv4.dns "8.8.8.8,1.1.1.1"`                  |
| `module bcma in use`                   | Legacy Broadcom module loaded | Blacklist `bcma`, `b43`, `brcmsmac`, then `sudo update-initramfs -u && reboot`      |

## 🧠 Lessons learned

- Apple devices use **Broadcom chips** that require **non-free firmware**.  
- Always check `ip route` and `resolv.conf` when debugging network issues.  
- NetworkManager (`nmcli`) simplifies Wi-Fi configuration on headless servers.  
- One active default route at a time avoids connection conflicts.

### 💬 Acknowledgment

Special thanks to the **Debian Support Team** on the official **IRC channel** (via the Debian IRL setup)  
for their guidance and troubleshooting assistance during the Broadcom Wi-Fi configuration process —  
especially to user **Sqrt{not}**, whose insights were crucial to resolving the issue.


## 🧱 Key commands cheat sheet

```
nmcli device status
nmcli device wifi list
sudo nmcli device wifi connect "<SSID>" password "<PASSWORD>"
sudo systemctl restart NetworkManager
ip route
cat /etc/resolv.conf
sudo modprobe brcmfmac
```

---

**Author:** Leandro Correia de Freitas  
**System:** Debian 12 (Bookworm) — iMac (Broadcom Wi-Fi)  
