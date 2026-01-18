### Initial System Setup

### First Boot

System update:
```bash
sudo apt update && sudo apt full-upgrade -y
sudo reboot
```

### SSH

SSH enabled:
```bash
sudo systemctl enable ssh --now
```

SSH hardening (`/etc/ssh/sshd_config`):
```conf
PermitRootLogin no
PasswordAuthentication yes
X11Forwarding no
UseDNS no
MaxAuthTries 3
```

Restart SSH:
```bash
sudo systemctl restart ssh
```

---

## Network Configuration

- Interface: `wlan0`
- Static IP: `192.168.1.221/24`
- Gateway: `192.168.1.1`
- DNS: `1.1.1.1`, `8.8.8.8`

Configured using NetworkManager:
```bash
sudo nmcli connection modify "SSID_NAME" \
  ipv4.method manual \
  ipv4.addresses 192.168.1.221/24 \
  ipv4.gateway 192.168.1.1 \
  ipv4.dns "1.1.1.1 8.8.8.8"

sudo nmcli connection down "SSID_NAME"
sudo nmcli connection up "SSID_NAME"
```

Ethernet disabled:
```bash
sudo nmcli device set eth0 managed no
sudo ip link set eth0 down
```

---

## External HDD Preparation

### Disk Identification
```bash
lsblk
```

### Format (EXT4)
```bash
sudo mkfs.ext4 /dev/sda1
```

### Mount Point
```bash
sudo mkdir -p /srv/nas
sudo mount /dev/sda1 /srv/nas
```

### Persistent Mount (`/etc/fstab`)
```fstab
UUID=<DISK_UUID>  /srv/nas  ext4  defaults,noatime  0  2
```

Test:
```bash
sudo mount -a
```

---

## NAS Directory Structure

Created on the HDD:
```text
/srv/nas
├── library        # Samba shared files
├── photoprism     # PhotoPrism storage + database
├── compose        # Docker Compose stacks
├── backups        # Backups
└── swap            # Swapfile
```

Permissions:
```bash
sudo chown -R User:User /srv/nas
sudo chmod -R 775 /srv/nas
```

---

## Swap Configuration (8 GB on HDD)

```bash
sudo fallocate -l 8G /srv/nas/swap/swapfile
sudo chmod 600 /srv/nas/swap/swapfile
sudo mkswap /srv/nas/swap/swapfile
sudo swapon /srv/nas/swap/swapfile
```

Persist swap:
```fstab
/srv/nas/swap/swapfile none swap sw 0 0
```

Swappiness:
```conf
vm.swappiness = 10
```

---

## Docker Installation

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker User
newgrp docker
sudo apt install -y docker-compose-plugin
```

Verification:
```bash
docker run hello-world
docker compose version
```

---

## Samba (NAS)

### Installation
```bash
sudo apt install -y samba samba-common-bin
```

### Samba User
```bash
sudo smbpasswd -a User
sudo smbpasswd -e User
```

### Samba Configuration (`/etc/samba/smb.conf`)

```ini
[global]
   workgroup = WORKGROUP
   server string = pi4-nas
   security = user
   map to guest = never
   unix charset = UTF-8

[NAS]
   path = /srv/nas/library
   browseable = yes
   writable = yes
   read only = no
   valid users = User
   create mask = 0664
   directory mask = 0775
   force user = User
   force group = User
```

Validation:
```bash
testparm
sudo systemctl restart smbd nmbd
```

Access:
```text
smb://pi4-nas/NAS
```

---

## PhotoPrism Deployment

### Directory Layout
```text
/srv/nas/photoprism
├── db
└── storage

/srv/nas/compose/photoprism
├── docker-compose.yml
└── .env
```

### Docker Compose Design

- PhotoPrism
- MariaDB
- All persistent data mapped to HDD
- No writes to SD card

### Start Stack
```bash
cd /srv/nas/compose/photoprism
docker compose up -d
```

Access:
```text
http://pi4-nas:2342
```

---

## PhotoPrism Configuration Notes

- Initial admin user renamed to `User`
- Single Super Admin user
- Facial recognition enabled gradually
- Indexing performed in small batches

Disabled for Raspberry Pi stability:
- RAW processing
- Dynamic previews
- Heavy background tasks

---

## Indexing Workflow

1. Copy photos to `/srv/nas/library`
2. Trigger indexing
3. Review faces and metadata
4. Repeat gradually

This avoids excessive CPU, RAM, and swap usage.

---

## Backup Strategy

Critical directories:
```text
/srv/nas/photoprism
/srv/nas/compose/photoprism
```

Original photos (`/srv/nas/library`) are backed up separately.

---

## Final Result

- Fully functional NAS
- Stable Samba file sharing
- PhotoPrism running on Docker
- No SD card wear
- Portable and reproducible architecture

---

## Status

This system is **production‑stable** for home use. You need to create a frequent back up routine, just in case comething goes wrong with it, so you don't loose your files/images

