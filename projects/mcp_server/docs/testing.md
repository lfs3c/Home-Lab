# Testing

## Milestone 1 verified checks

- local stdio initialization, discovery and tool execution passed
- Streamable HTTP initialization, discovery and tool execution passed
- request without token returned HTTP 401
- request with invalid token returned HTTP 401
- valid Bearer token initialized an MCP session and called tools successfully
- Hermes VM connected remotely, discovered the tools and invoked `system_health`
- the frozen Hermes Control API was not used for the end-to-end MCP validation

Exact runtime health values and credentials are intentionally not stored in this repository.
