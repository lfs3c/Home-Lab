import os
import secrets

from mcp.server.auth.provider import AccessToken, TokenVerifier


MCP_HOST = os.environ.get("LF1_MCP_HOST", "127.0.0.1")
MCP_PORT = int(os.environ.get("LF1_MCP_PORT", "8000"))
RESOURCE_URL = os.environ.get(
    "LF1_MCP_RESOURCE_URL", f"http://{MCP_HOST}:{MCP_PORT}/mcp"
)
REQUIRED_SCOPE = "lf1:read"


class LF1TokenVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        expected_token = os.environ.get("LF1_MCP_TOKEN")

        if not expected_token:
            return None

        if not secrets.compare_digest(token, expected_token):
            return None

        return AccessToken(
            token=token,
            client_id="authorized-mcp-client",
            scopes=[REQUIRED_SCOPE],
            resource=RESOURCE_URL,
            subject="authorized-mcp-client",
        )
