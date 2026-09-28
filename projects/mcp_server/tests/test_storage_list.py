"""Tests for LF1 storage observability."""

import json

from lf1_mcp.tools import storage_list


LSBLK_SAMPLE = json.dumps(
    {
        "blockdevices": [
            {
                "name": "sda",
                "type": "disk",
                "size": 1000000000000,
                "fstype": None,
                "label": None,
                "uuid": None,
                "mountpoints": [None],
                "model": "SYSTEM DISK",
                "children": [
                    {
                        "name": "sda1",
                        "type": "part",
                        "size": 900000000000,
                        "fstype": "ext4",
                        "label": None,
                        "uuid": "root-uuid",
                        "mountpoints": ["/"],
                        "model": None,
                    },
                    {
                        "name": "sda2",
                        "type": "part",
                        "size": 1000000000,
                        "fstype": "swap",
                        "label": None,
                        "uuid": "swap-uuid",
                        "mountpoints": ["[SWAP]"],
                        "model": None,
                    },
                ],
            },
            {
                "name": "sdb",
                "type": "disk",
                "size": 2000000000000,
                "fstype": None,
                "label": None,
                "uuid": None,
                "mountpoints": [None],
                "model": "DATA DISK",
                "children": [
                    {
                        "name": "sdb1",
                        "type": "part",
                        "size": 2000000000000,
                        "fstype": "ext4",
                        "label": "data",
                        "uuid": "data-uuid",
                        "mountpoints": ["/srv/data"],
                        "model": None,
                    }
                ],
            },
        ]
    }
)

DF_SAMPLE = """Filesystem Type 1-blocks Used Available Capacity Mounted on
/dev/sda1 ext4 900000000000 90000000000 810000000000 10% /
/dev/sdb1 ext4 2000000000000 500000000000 1500000000000 25% /srv/data
tmpfs tmpfs 1000000 1000 999000 1% /run
"""


def test_storage_list_normalizes_disks_and_usage(monkeypatch):
    def fake_run(command):
        if command == storage_list.LSBLK_COMMAND:
            return LSBLK_SAMPLE

        if command == storage_list.DF_COMMAND:
            return DF_SAMPLE

        raise AssertionError(f"unexpected command: {command}")

    monkeypatch.setattr(storage_list, "_run_command", fake_run)

    result = storage_list.get_storage_list()

    assert result["host"] == "lf1"
    assert result["source"] == "local"
    assert result["read_only"] is True

    assert result["summary"]["disks"] == 2
    assert result["summary"]["mounted_filesystems"] == 2

    assert result["disks"][0]["name"] == "sda"
    assert result["disks"][0]["model"] == "SYSTEM DISK"

    root = result["disks"][0]["partitions"][0]

    assert root["filesystem"] == "ext4"
    assert root["usage"]["mountpoint"] == "/"
    assert root["usage"]["usage_percent"] == 10

    swap = result["disks"][0]["partitions"][1]

    assert swap["filesystem"] == "swap"
    assert swap["usage"] is None

    data = result["disks"][1]["partitions"][0]

    assert data["usage"]["mountpoint"] == "/srv/data"
    assert data["usage"]["usage_percent"] == 25


def test_storage_list_discovers_new_disk_without_code_change(monkeypatch):
    data = json.loads(LSBLK_SAMPLE)

    data["blockdevices"].append(
        {
            "name": "sdc",
            "type": "disk",
            "size": 4000000000000,
            "fstype": None,
            "label": None,
            "uuid": None,
            "mountpoints": [None],
            "model": "FUTURE DISK",
            "children": [],
        }
    )

    def fake_run(command):
        if command == storage_list.LSBLK_COMMAND:
            return json.dumps(data)

        if command == storage_list.DF_COMMAND:
            return DF_SAMPLE

        raise AssertionError(f"unexpected command: {command}")

    monkeypatch.setattr(storage_list, "_run_command", fake_run)

    result = storage_list.get_storage_list()

    assert result["summary"]["disks"] == 3
    assert result["disks"][2]["name"] == "sdc"
    assert result["disks"][2]["model"] == "FUTURE DISK"
