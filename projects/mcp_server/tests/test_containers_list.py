from unittest.mock import patch

from lf1_mcp.tools.containers_list import get_containers_list


def test_get_containers_list_normalizes_and_summarizes():
    docker_response = [
        {
            "Names": ["/zabbix-server"],
            "Image": "zabbix/zabbix-server:latest",
            "State": "running",
            "Status": "Up 2 days",
        },
        {
            "Names": ["/wikijs"],
            "Image": "requarks/wiki:2",
            "State": "exited",
            "Status": "Exited (255) 2 days ago",
        },
    ]

    with patch(
        "lf1_mcp.tools.containers_list._fetch_containers",
        return_value=docker_response,
    ):
        result = get_containers_list()

    assert result["source"] == "docker"

    assert result["summary"] == {
        "total": 2,
        "running": 1,
        "stopped": 1,
    }

    assert result["containers"] == [
        {
            "name": "wikijs",
            "image": "requarks/wiki:2",
            "state": "exited",
            "status": "Exited (255) 2 days ago",
        },
        {
            "name": "zabbix-server",
            "image": "zabbix/zabbix-server:latest",
            "state": "running",
            "status": "Up 2 days",
        },
    ]
