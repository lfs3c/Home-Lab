import os
import shutil
import socket
from pathlib import Path


def _read_uptime_seconds() -> float:
    with Path("/proc/uptime").open("r", encoding="utf-8") as file:
        return float(file.read().split()[0])


def _read_memory() -> dict[str, int]:
    values: dict[str, int] = {}

    with Path("/proc/meminfo").open("r", encoding="utf-8") as file:
        for line in file:
            key, value = line.split(":", 1)
            fields = value.strip().split()

            if fields:
                values[key] = int(fields[0]) * 1024

    total = values["MemTotal"]
    available = values["MemAvailable"]

    return {
        "total_bytes": total,
        "available_bytes": available,
        "used_bytes": total - available,
    }


def get_system_health() -> dict:
    load_1, load_5, load_15 = os.getloadavg()
    memory = _read_memory()
    disk = shutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "uptime_seconds": _read_uptime_seconds(),
        "load_average": {
            "1_minute": load_1,
            "5_minutes": load_5,
            "15_minutes": load_15,
        },
        "memory": memory,
        "root_filesystem": {
            "total_bytes": disk.total,
            "used_bytes": disk.used,
            "free_bytes": disk.free,
        },
    }
