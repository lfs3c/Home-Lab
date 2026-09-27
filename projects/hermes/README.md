# Hermes

![Hermes](https://img.shields.io/badge/Hermes-Home%20Lab%20Admin-6C63FF) ![VM](https://img.shields.io/badge/VM-LaptopU-E95420?logo=ubuntu&logoColor=white) ![Security](https://img.shields.io/badge/Design-Least%20Privilege-28A745)

Hermes is the Home Lab administration assistant project.

## Architecture

Hermes spans more than one Home Lab node:

- **Hermes VM** — runs on LaptopU.
- **Hermes Control API** — runs on LF1 and is the current administration interface.
- **MCP Server** — is being developed on LF1 as the next controlled interface for Hermes.

```text
LaptopU
└── Hermes VM
      |
      +---------------------+
      |                     |
      v                     v
LF1: Hermes Control API   LF1: MCP Server
      |                     |
      +----------+----------+
                 |
                 v
              Home Lab
```

The Control API remains the verified baseline while MCP development progresses.

## Security Principles

- least privilege
- explicit capabilities
- authorization before privileged actions
- input validation
- auditability
- secrets kept outside the repository
- staged testing and review before production changes

Implementation-specific documentation is maintained in the corresponding project directories.
