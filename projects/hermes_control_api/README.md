# Hermes Control API

![Status](https://img.shields.io/badge/Status-Active-28A745) ![LF1](https://img.shields.io/badge/Host-LF1-A81D33?logo=debian&logoColor=white) ![API](https://img.shields.io/badge/API-Controlled%20Capabilities-009688) ![Security](https://img.shields.io/badge/Security-Least%20Privilege-28A745)

**Status:** Active on LF1

The Hermes Control API is the current verified control interface between Hermes and LF1.

## Verified Current State

The API runs as a dedicated systemd service on LF1. The current implementation provides controlled capabilities rather than unrestricted shell access.

Currently documented read-only capabilities include:

- system health
- audit reading
- action discovery
- permission discovery

An administrative interface is also part of the current implementation.

## Role

The Control API is the production baseline for Hermes administration while the MCP Server is developed separately.

## Repository Safety

This public documentation intentionally excludes:

- private IP addresses and internal hostnames
- credentials, cookies, tokens, and secrets
- exact firewall rules
- database contents
- privileged implementation details that would unnecessarily expose the environment

Implementation details should be added here only after they are verified and safe to publish.
