"""Read-only storage observability for LF1."""

from __future__ import annotations

import json
import subprocess
from typing import Any


LSBLK_COMMAND = [
    "lsblk",
    "-J",
    "-b",
    "-o",
    "NAME,TYPE,SIZE,FSTYPE,LABEL,UUID,MOUNTPOINTS,MODEL",
]

DF_COMMAND = [
    "df",
    "-B1",
    "-P",
    "-T",
]


def _run_command(command: list[str]) -> str:
    """Run one fixed read-only storage command."""

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=5,
        check=False,
    )

    if result.returncode != 0:
        error = result.stderr.strip() or "command failed"
        raise RuntimeError(error)

    return result.stdout


def _read_lsblk() -> list[dict[str, Any]]:
    raw = _run_command(LSBLK_COMMAND)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid lsblk JSON") from exc

    devices = data.get("blockdevices")

    if not isinstance(devices, list):
        raise RuntimeError("lsblk response missing blockdevices")

    return devices


def _read_df() -> dict[str, dict[str, Any]]:
    raw = _run_command(DF_COMMAND)
    lines = raw.splitlines()

    usage: dict[str, dict[str, Any]] = {}

    for line in lines[1:]:
        fields = line.split()

        if len(fields) < 7:
            continue

        source, filesystem = fields[0], fields[1]

        if not source.startswith("/dev/"):
            continue

        try:
            size_bytes = int(fields[2])
            used_bytes = int(fields[3])
            available_bytes = int(fields[4])
            usage_percent = int(fields[5].rstrip("%"))
        except ValueError:
            continue

        mountpoint = " ".join(fields[6:])

        usage[source] = {
            "filesystem": filesystem,
            "mountpoint": mountpoint,
            "size_bytes": size_bytes,
            "used_bytes": used_bytes,
            "available_bytes": available_bytes,
            "usage_percent": usage_percent,
        }

    return usage


def _normalize_partition(
    partition: dict[str, Any],
    usage: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    name = partition.get("name")
    source = f"/dev/{name}" if name else None

    mountpoints = [
        mountpoint
        for mountpoint in (partition.get("mountpoints") or [])
        if mountpoint
    ]

    usage_data = usage.get(source or "")

    result: dict[str, Any] = {
        "name": name,
        "type": partition.get("type"),
        "filesystem": partition.get("fstype"),
        "label": partition.get("label"),
        "uuid": partition.get("uuid"),
        "size_bytes": partition.get("size"),
        "mountpoints": mountpoints,
    }

    if usage_data:
        result["usage"] = usage_data
    else:
        result["usage"] = None

    return result


def get_storage_list() -> dict[str, Any]:
    """Return normalized read-only storage information for LF1."""

    devices = _read_lsblk()
    usage = _read_df()

    disks: list[dict[str, Any]] = []

    for device in devices:
        if device.get("type") != "disk":
            continue

        partitions = [
            _normalize_partition(partition, usage)
            for partition in (device.get("children") or [])
        ]

        disks.append(
            {
                "name": device.get("name"),
                "model": device.get("model"),
                "size_bytes": device.get("size"),
                "partitions": partitions,
            }
        )

    disks.sort(key=lambda disk: disk.get("name") or "")

    mounted_filesystems = sum(
        1
        for disk in disks
        for partition in disk["partitions"]
        if partition["usage"] is not None
    )

    return {
        "host": "lf1",
        "source": "local",
        "read_only": True,
        "summary": {
            "disks": len(disks),
            "mounted_filesystems": mounted_filesystems,
        },
        "disks": disks,
    }
