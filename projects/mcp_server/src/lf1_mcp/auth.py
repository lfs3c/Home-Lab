import os
import secrets

from mcp.server.auth.provider import AccessToken, TokenVerifier


RESOURCE_URL = "http://192.168.50.18:8000/mcp"
REQUIRED_SCOPE = "lf1:read"


class HermesTokenVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        expected_token = os.environ.get("LF1_MCP_TOKEN")

        if not expected_token:
            return None

        if not secrets.compare_digest(token, expected_token):
            return None

        return AccessToken(
            token=token,
            client_id="hermes",
            scopes=[REQUIRED_SCOPE],
            resource=RESOURCE_URL,
            subject="hermes-agent",
        )
