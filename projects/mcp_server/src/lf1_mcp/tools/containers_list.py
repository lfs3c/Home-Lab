import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DOCKER_PROXY_URL = "http://127.0.0.1:2375"
DOCKER_CONTAINERS_PATH = "/containers/json?all=true"
REQUEST_TIMEOUT_SECONDS = 3


class ContainersListError(RuntimeError):
    """Raised when container state cannot be safely retrieved."""


def _fetch_containers() -> list[dict]:
    request = Request(
        f"{DOCKER_PROXY_URL}{DOCKER_CONTAINERS_PATH}",
        method="GET",
        headers={
            "Accept": "application/json",
        },
    )

    try:
        with urlopen(
            request,
            timeout=REQUEST_TIMEOUT_SECONDS,
        ) as response:
            if response.status != 200:
                raise ContainersListError(
                    f"Docker proxy returned HTTP {response.status}"
                )

            payload = response.read()

    except HTTPError as exc:
        raise ContainersListError(
            f"Docker proxy returned HTTP {exc.code}"
        ) from exc

    except URLError as exc:
        raise ContainersListError(
            "Docker proxy is unavailable"
        ) from exc

    except TimeoutError as exc:
        raise ContainersListError(
            "Docker proxy request timed out"
        ) from exc

    try:
        data = json.loads(payload)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ContainersListError(
            "Docker proxy returned invalid JSON"
        ) from exc

    if not isinstance(data, list):
        raise ContainersListError(
            "Docker proxy returned an unexpected response"
        )

    return data


def _normalize_container(container: dict) -> dict:
    raw_names = container.get("Names", [])

    names = [
        name.lstrip("/")
        for name in raw_names
        if isinstance(name, str)
    ]

    name = names[0] if names else "unknown"

    return {
        "name": name,
        "image": str(container.get("Image", "")),
        "state": str(container.get("State", "unknown")),
        "status": str(container.get("Status", "")),
    }


def get_containers_list() -> dict:
    raw_containers = _fetch_containers()

    containers = [
        _normalize_container(container)
        for container in raw_containers
        if isinstance(container, dict)
    ]

    containers.sort(
        key=lambda container: container["name"].lower()
    )

    running = sum(
        container["state"] == "running"
        for container in containers
    )

    stopped = len(containers) - running

    return {
        "source": "docker",
        "summary": {
            "total": len(containers),
            "running": running,
            "stopped": stopped,
        },
        "containers": containers,
    }
