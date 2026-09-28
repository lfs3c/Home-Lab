# Testing

## Testing Strategy

Testing depth is proportional to capability risk.

Read-only capabilities use focused unit and integration tests. Privileged or state-changing capabilities require stronger security and failure-path testing before production promotion.

## system_health

Validated end-to-end:

    Hermes
      -> authenticated MCP
      -> system_health
      -> LF1 local Linux sources

Hermes successfully received real LF1 health information.

## containers_list

The unit test validates normalization, deterministic ordering, running/stopped/total counts, and output schema.

The implementation was also tested against the restricted Docker proxy. Runtime container counts are observations and are not assumed to remain constant.

Boundary validation confirmed the required container-listing operation was allowed while tested sensitive and state-changing operations returned HTTP 403.

A fresh Hermes session successfully discovered and executed:

    mcp__lf1__containers_list

Fresh-session discovery should be considered when validating newly deployed MCP capabilities.

## Storage Observability

The `storage_list` milestone was validated at multiple layers.

Unit tests verify normalized disk/filesystem output and that a newly discovered physical disk is returned without requiring a source-code change.

Development validation confirmed:

- all current unit tests passed after storage implementation
- physical disks are discovered dynamically
- pseudo filesystems such as tmpfs are excluded from filesystem usage
- swap is represented without filesystem usage
- `lf1-mcp` can read both `lsblk` and `df` without additional privileges

Production validation confirmed:

- `storage_list` imports and executes under the dedicated `lf1-mcp` account
- `NoNewPrivileges` remains enabled
- the MCP service remains restricted to its intended network binding

Fresh-session Hermes end-to-end validation confirmed discovery and execution of:

    mcp__lf1__storage_list

The validation used only the LF1 MCP server and did not use the Hermes Control API.

Observed filesystem usage values are runtime observations, not configuration constants.
