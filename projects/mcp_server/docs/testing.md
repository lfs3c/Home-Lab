# Testing

## Testing Strategy

Testing depth is proportional to capability risk.

Read-only capabilities use focused unit and integration tests.

Privileged or state-changing capabilities require stronger security and failure-path testing before production promotion.

## system_health

Validated end-to-end:

    Hermes
      -> authenticated MCP
      -> system_health
      -> LF1 local Linux sources

Hermes successfully received real LF1 health information.

## containers_list Unit Test

Test:

    tests/test_containers_list.py

The test validates:

- normalization of Docker container data;
- deterministic name ordering;
- running count;
- stopped count;
- total count;
- output schema.

Current milestone result:

    1 passed

## Docker Proxy Integration

The development implementation was tested directly against:

    http://127.0.0.1:2375/containers/json?all=true

At milestone validation time it returned:

    28 total
    25 running
    3 stopped

The exact counts are runtime observations and are not assumed to remain constant.

## Docker Boundary Tests

Allowed:

    GET /_ping
    GET /containers/json?all=true

Blocked with HTTP 403:

    GET  /containers/<id>/logs
    GET  /containers/<id>/top
    GET  /containers/<id>/export
    GET  /images/json
    GET  /volumes
    GET  /networks
    POST /containers/<id>/stop
    POST /containers/<id>/restart

## Hermes End-to-End Validation

A fresh Hermes session successfully discovered:

    mcp__lf1__containers_list

Hermes reported:

    Total: 28
    Running: 25
    Stopped: 3

At validation time the non-running containers were:

    netdata
    website
    wikijs

The previous Hermes session did not discover the newly added tool until a fresh session was started.

Fresh-session discovery should therefore be considered when validating newly deployed MCP capabilities.
