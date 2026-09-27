# Changelog

## 0.1.0 — Milestone 1

- created the LF1 MCP Server using the official Python MCP SDK
- implemented `ping` and read-only `system_health`
- validated stdio and Streamable HTTP transports
- configured persistent LF1 service operation and firewall restriction
- added Bearer-token authentication
- validated rejection of missing and invalid credentials
- completed authenticated Hermes VM → LF1 MCP → `system_health` end-to-end test
- froze the previous Hermes Control API as a reference/fallback rather than the active development path
