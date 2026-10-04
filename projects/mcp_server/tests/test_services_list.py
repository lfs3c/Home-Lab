from lf1_mcp.tools.services_list import build_services_list


SAMPLE = """Id=docker.service
Description=Docker Application Container Engine
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled

Id=certbot.service
Description=Certbot
LoadState=loaded
ActiveState=failed
SubState=failed
UnitFileState=static

Id=example.service
Description=Example Service
LoadState=loaded
ActiveState=inactive
SubState=dead
UnitFileState=disabled
"""


def test_services_list_normalizes_and_summarizes_services():
    result = build_services_list(SAMPLE)

    assert result["host"] == "lf1"
    assert result["source"] == "systemd"
    assert result["read_only"] is True

    assert result["summary"] == {
        "total": 3,
        "active": 1,
        "inactive": 1,
        "failed": 1,
    }

    assert [service["name"] for service in result["services"]] == [
        "certbot.service",
        "docker.service",
        "example.service",
    ]

    docker = next(
        service
        for service in result["services"]
        if service["name"] == "docker.service"
    )

    assert docker == {
        "name": "docker.service",
        "description": "Docker Application Container Engine",
        "load_state": "loaded",
        "active_state": "active",
        "sub_state": "running",
        "enabled_state": "enabled",
    }


def test_services_list_discovers_new_service_without_code_change():
    expanded = SAMPLE + """
Id=future-home-lab.service
Description=Future Home Lab Service
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled
"""

    result = build_services_list(expanded)

    names = [
        service["name"]
        for service in result["services"]
    ]

    assert "future-home-lab.service" in names
    assert result["summary"]["total"] == 4
    assert result["summary"]["active"] == 2


def test_services_list_ignores_non_service_blocks():
    expanded = SAMPLE + """
Id=example.timer
Description=Example Timer
LoadState=loaded
ActiveState=active
SubState=waiting
UnitFileState=enabled
"""

    result = build_services_list(expanded)

    names = [
        service["name"]
        for service in result["services"]
    ]

    assert "example.timer" not in names
    assert result["summary"]["total"] == 3
