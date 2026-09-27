# Backup Infrastructure

![BorgBackup](https://img.shields.io/badge/BorgBackup-1.2.4-00A86B?logo=linux&logoColor=white) ![Backup](https://img.shields.io/badge/Backup-Manual-blue) ![Storage](https://img.shields.io/badge/Storage-External%20ext4-555555?logo=linux&logoColor=white)

LF1 uses BorgBackup for manual backups to dedicated external storage.

## Current State

- BorgBackup 1.2.4 is installed on LF1.
- Backups are currently initiated manually.
- A dedicated ext4 backup disk is configured through `/etc/fstab`.
- The backup storage is separate from the LF1 system disk and PhotoPrism data disk.
- No Borg systemd service, Borg timer, or Borg cron job is currently configured.

The external backup disk may be disconnected when it is not in use, so its mount is not expected to remain active continuously.

## Documentation Policy

Backup automation, schedules, retention policies, repository paths, and restore procedures will be documented only after they are implemented and verified.

Exact disk UUIDs, repository paths, encryption material, credentials, and other sensitive operational details are intentionally excluded from this public repository.
