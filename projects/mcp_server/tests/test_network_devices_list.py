from unittest.mock import Mock, patch


def _sample_librenms_response():
    return {
        "status": "ok",
        "devices": [
            {
                "device_id": 1,
                "hostname": "switch.example",
                "sysName": "switch-core",
                "os": "ios",
                "status": 1,
                "disabled": 0,
                "ignore": 0,
            },
            {
                "device_id": 2,
                "hostname": "server.example",
                "sysName": "server-lf1",
                "os": "linux",
                "status": 0,
                "disabled": 0,
                "ignore": 0,
            },
        ],
    }


def test_network_devices_list_normalizes_devices():
    from lf1_mcp.tools.network_devices_list import get_network_devices_list

    response = Mock()
    response.status_code = 200
    response.json.return_value = _sample_librenms_response()
    response.raise_for_status.return_value = None

    with patch(
        "lf1_mcp.tools.network_devices_list.requests.get",
        return_value=response,
    ) as mock_get:
        result = get_network_devices_list(
            base_url="https://librenms.example.invalid",
            token="test-token",
        )

    assert result["summary"] == {
        "total": 2,
        "up": 1,
        "down": 1,
    }

    assert result["devices"] == [
        {
            "device_id": 1,
            "hostname": "switch.example",
            "sys_name": "switch-core",
            "os": "ios",
            "status": "up",
            "disabled": False,
            "ignored": False,
        },
        {
            "device_id": 2,
            "hostname": "server.example",
            "sys_name": "server-lf1",
            "os": "linux",
            "status": "down",
            "disabled": False,
            "ignored": False,
        },
    ]

    mock_get.assert_called_once_with(
        "https://librenms.example.invalid/api/v0/devices",
        headers={"Authorization": "Bearer test-token"},
        timeout=10,
    )


def test_network_devices_list_does_not_return_token():
    from lf1_mcp.tools.network_devices_list import get_network_devices_list

    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "status": "ok",
        "devices": [],
    }
    response.raise_for_status.return_value = None

    secret = "super-secret-test-token"

    with patch(
        "lf1_mcp.tools.network_devices_list.requests.get",
        return_value=response,
    ):
        result = get_network_devices_list(
            base_url="https://librenms.example.invalid",
            token=secret,
        )

    assert secret not in repr(result)


def test_network_devices_list_rejects_invalid_devices_payload():
    from lf1_mcp.tools.network_devices_list import get_network_devices_list

    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "status": "ok",
        "devices": "not-a-list",
    }
    response.raise_for_status.return_value = None

    with patch(
        "lf1_mcp.tools.network_devices_list.requests.get",
        return_value=response,
    ):
        try:
            get_network_devices_list(
                base_url="https://librenms.example.invalid",
                token="test-token",
            )
        except ValueError:
            pass
        else:
            raise AssertionError("invalid devices payload must raise ValueError")
