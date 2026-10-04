"""Read-only LibreNMS network device observation."""

from __future__ import annotations

from typing import Any

import requests


def get_network_devices_list(
    *,
    base_url: str,
    token: str,
) -> dict[str, Any]:
    """Return a normalized read-only view of LibreNMS devices."""

    url = f"{base_url.rstrip('/')}/api/v0/devices"

    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    response.raise_for_status()

    payload = response.json()
    devices = payload.get("devices")

    if not isinstance(devices, list):
        raise ValueError("LibreNMS response contains an invalid devices payload")

    normalized_devices = []

    for device in devices:
        if not isinstance(device, dict):
            raise ValueError("LibreNMS response contains an invalid device entry")

        is_up = device.get("status") == 1

        normalized_devices.append(
            {
                "device_id": device.get("device_id"),
                "hostname": device.get("hostname"),
                "sys_name": device.get("sysName"),
                "os": device.get("os"),
                "status": "up" if is_up else "down",
                "disabled": device.get("disabled") == 1,
                "ignored": device.get("ignore") == 1,
            }
        )

    up = sum(
        1
        for device in normalized_devices
        if device["status"] == "up"
    )

    return {
        "summary": {
            "total": len(normalized_devices),
            "up": up,
            "down": len(normalized_devices) - up,
        },
        "devices": normalized_devices,
    }
