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

## services_list

Test:

    tests/test_services_list.py

The tests validate:

- normalization and summary of systemd service information
- dynamic discovery of newly added services without code changes
- filtering of non-service blocks

At milestone closure, the complete development test suite returned:

    6 passed

## services_list Hermes End-to-End Validation

A fresh Hermes session successfully discovered and executed:

    mcp__lf1__services_list

The production result was obtained through the authenticated Streamable HTTP
MCP path.

Validated path:

    Hermes
      -> authenticated MCP
      -> services_list
      -> LF1 systemd

## LibreNMS network_devices_list

Automated tests verify device normalization, status summaries, rejection of
invalid device payloads, and that the LibreNMS token is absent from returned
results.

At that historical milestone, the development suite passed 9 tests.

Real end-to-end validation confirmed:

- LibreNMS API access with the dedicated credential
- production MCP environment loading
- Hermes discovery and execution of `network_devices_list`
- successful device inventory retrieval

Validated path:

    Hermes VM -> LF1 MCP -> LibreNMS API -> network inventory -> Hermes

## Latest Owner-Reported Milestone

The approved private baseline recorded 36 passing tests and production validation of `network_device_status`. Those newer source files and tests are not present in this public snapshot, so that 36-test result is historical evidence, not a result reproduced from this checkout. Historical Hermes end-to-end validations above remain unchanged.
