# Step 1 — Verify Debian 13 ISO (authenticity & integrity)

## Objective
Verify the ISO is authentic (GPG signature) and intact (SHA512) before installing on the home server.

## Commands (see `verify_commands.sh`)
1) Download `SHA512SUMS` and `SHA512SUMS.sign`
2) Import Debian CD signing key
3) Verify signature → expect “Good signature”
4) Verify checksum → expect “...: OK”

## Expected Output

gpg: Good signature from "Debian CD signing key debian-cd@lists.debian.org
> Note: “not certified with a trusted signature” is normal if the key isn’t locally owner-trusted.


debian-13.1.0-amd64-netinst.iso: OK

## References
- Debian — Verify CD/ISO: https://www.debian.org/CD/verify
- Debian CD (amd64): https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/
