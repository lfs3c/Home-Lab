import os
import secrets

from mcp.server.auth.provider import AccessToken, TokenVerifier


REQUIRED_SCOPE = "lf1:read"


def resource_url() -> str:
    return os.environ.get("LF1_MCP_RESOURCE_URL", "http://127.0.0.1:8000/mcp")


class HermesTokenVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        expected_token = os.environ.get("LF1_MCP_TOKEN")
        if not expected_token:
            return None
        if not secrets.compare_digest(token, expected_token):
            return None
        return AccessToken(token=token, client_id="hermes", scopes=[REQUIRED_SCOPE], resource=resource_url(), subject="hermes-agent")
