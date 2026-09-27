# MCP Server for Home Lab

**Status:** Planning / In Development

## Purpose

This project will provide a self-hosted MCP server for controlled administration and observation of the Home Lab.

The intended design exposes explicit, authorized tools rather than unrestricted shell or generic HTTP access.

## Design Principles

- Explicit tools and capabilities
- Least privilege
- Input validation
- Authorization checks
- Audit logging
- Secrets kept outside the repository
- Staged development and review before production changes

## Intended Architecture

```text
Hermes VM
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

## Documentation Scope

This document describes design intent only. It does not claim that the MCP server is currently deployed or that specific LF1 services are already integrated. Live service documentation will be added only after the environment is verified.
