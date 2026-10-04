"""Read-only systemd service observability for LF1."""

from __future__ import annotations

import subprocess
from typing import Any


SYSTEMCTL_COMMAND = [
    "systemctl",
    "show",
    "--type=service",
    "--all",
    "--no-pager",
    "--property=Id",
    "--property=Description",
    "--property=LoadState",
    "--property=ActiveState",
    "--property=SubState",
    "--property=UnitFileState",
]


def _run_systemctl() -> str:
    result = subprocess.run(
        SYSTEMCTL_COMMAND,
        capture_output=True,
        text=True,
        timeout=5,
        check=False,
    )

    if result.returncode != 0:
        error = result.stderr.strip() or "systemctl query failed"
        raise RuntimeError(error)

    return result.stdout


def _parse_blocks(output: str) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []

    for raw_block in output.split("\n\n"):
        raw_block = raw_block.strip()

        if not raw_block:
            continue

        values: dict[str, str] = {}

        for line in raw_block.splitlines():
            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            values[key] = value

        if values.get("Id", "").endswith(".service"):
            blocks.append(values)

    return blocks


def _normalize_service(values: dict[str, str]) -> dict[str, Any]:
    return {
        "name": values.get("Id") or None,
        "description": values.get("Description") or None,
        "load_state": values.get("LoadState") or None,
        "active_state": values.get("ActiveState") or None,
        "sub_state": values.get("SubState") or None,
        "enabled_state": values.get("UnitFileState") or None,
    }


def build_services_list(output: str) -> dict[str, Any]:
    services = [
        _normalize_service(values)
        for values in _parse_blocks(output)
    ]

    services.sort(key=lambda service: service["name"] or "")

    active = sum(
        service["active_state"] == "active"
        for service in services
    )

    inactive = sum(
        service["active_state"] == "inactive"
        for service in services
    )

    failed = sum(
        service["active_state"] == "failed"
        for service in services
    )

    return {
        "host": "lf1",
        "source": "systemd",
        "read_only": True,
        "summary": {
            "total": len(services),
            "active": active,
            "inactive": inactive,
            "failed": failed,
        },
        "services": services,
    }


def get_services_list() -> dict[str, Any]:
    """Return normalized read-only systemd service information."""
    return build_services_list(_run_systemctl())
