#!/usr/bin/env bash
set -euo pipefail

# === Adjust to your environment ===
ISO_DIR="$HOME/Downloads/Debian13"
ISO_NAME="debian-13.1.0-amd64-netinst.iso"

# Debian official checksums
SHA_URL="https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/SHA512SUMS"
SIG_URL="https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/SHA512SUMS.sign"

# Debian CD Team signing key (current - Oct 16 2025)
DEBIAN_CD_KEY="DF9B9C49EAA9298432589D76DA87E80D6294BE9B"

echo "== step 0: go to ISO dir =="
cd "$ISO_DIR"

echo "== step 1: download checksum & signature =="
wget -q -O SHA512SUMS "$SHA_URL"
wget -q -O SHA512SUMS.sign "$SIG_URL"

echo "== step 2: import Debian CD signing key =="
gpg --keyserver keyring.debian.org --recv-keys "$DEBIAN_CD_KEY"

echo "== step 3: verify signature authenticity =="
gpg --verify SHA512SUMS.sign SHA512SUMS

echo "== step 4: verify ISO integrity (SHA512) =="
sha512sum -c SHA512SUMS 2>/dev/null | grep -E "^${ISO_NAME}: OK$" || {
  echo "ERROR: checksum not found or mismatch for ${ISO_NAME}"; exit 1;
}

echo "== all good =="
echo "Authenticity: Good signature"
echo "Integrity: ${ISO_NAME}: OK"
