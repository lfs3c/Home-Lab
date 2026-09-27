# MCP Server for Home Lab

![Status](https://img.shields.io/badge/Status-In%20Development-orange) ![MCP](https://img.shields.io/badge/MCP-Server-6C63FF) ![LF1](https://img.shields.io/badge/Host-LF1-A81D33?logo=debian&logoColor=white) ![Security](https://img.shields.io/badge/Security-Least%20Privilege-28A745)

**Status:** In Development on LF1

## Purpose

The MCP Server is the developing LF1-hosted interface that will allow Hermes to interact with the Home Lab through explicit, controlled MCP tools.

It is being developed alongside the existing Hermes Control API. The Control API remains the verified baseline while MCP capabilities are implemented and validated.

## Architecture

```text
Hermes VM (LaptopU)
        |
        | MCP
        v
MCP Server (LF1)
        |
        +-- explicit tools
        +-- authorization
        +-- validation
        +-- audit logging
        |
        v
Home Lab
```

## Design Principles

- explicit tools and capabilities
- least privilege
- input validation
- authorization checks
- audit logging
- secrets kept outside the repository
- staged development and independent review before production promotion

## Development Documentation

As implementation progresses, this directory can grow with verified documentation such as:

```text
mcp_server/
├── README.md
├── architecture.md
├── capabilities.md
├── security.md
├── testing.md
└── changelog.md
```

Files should be added when there is real implementation or verified design material to document; empty placeholder files are intentionally avoided.

## Current Boundary

This README records the project and its intended architecture. It does not claim that unfinished MCP tools, integrations, or privileged actions are already available.
