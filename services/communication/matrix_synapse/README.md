# Matrix / Synapse on Debian 12 with Docker and HAProxy

![Debian](https://img.shields.io/badge/Debian-12%20Bookworm-A81D33?logo=debian&logoColor=white)
![Matrix](https://img.shields.io/badge/Matrix-Synapse-0DBD8B?logo=matrix&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![HAProxy](https://img.shields.io/badge/HAProxy-Reverse%20Proxy-106DA9)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-DNS-F38020?logo=cloudflare&logoColor=white)
![Security](https://img.shields.io/badge/Security-Hardened-28A745?logo=security&logoColor=green)

## Overview

This document provides a **complete, end-to-end technical record** of a self-hosted **Matrix / Synapse** deployment running on a **Debian 12** server.

The goal of this project is **secure messaging**, **clean public exposure**, and **predictable maintenance**.

This public version was written to match the real installation logic used in my homelab, but with sanitized values and reusable placeholders.

---

## Project Goal

This deployment was designed to:

- host a private Matrix homeserver
- expose the service publicly without exposing unnecessary ports
- keep administration separated from public access
- use a clean domain structure from the beginning
- keep the stack maintainable with Docker and reverse proxying

---

## Why I Configured It This Way

This setup uses a conservative approach.

- `Synapse` stays behind a reverse proxy
- only `80` and `443` are exposed publicly
- `PostgreSQL` stays internal only
- administrative access does not need to be published to the Internet
- federation works through `443`, so there is no need to expose `8448`

This keeps the attack surface smaller and makes troubleshooting easier.

---

## Target Architecture

- OS: `Debian 12`
- Homeserver software: `Matrix Synapse`
- Deployment method: `Docker Compose`
- Reverse proxy: `HAProxy`
- Database: `PostgreSQL`
- DNS: `Cloudflare` or equivalent DNS provider
- Admin access: private remote access only

Recommended public naming:

- Matrix `server_name`: `example.com`
- Public Synapse hostname: `matrix.example.com`

This gives cleaner Matrix IDs:

```text
@user:example.com
```

Instead of:

```text
@user:matrix.example.com
```

---

## Service Layout

```text
Element / other Matrix client
  -> https://example.com/.well-known/matrix/client
  -> https://matrix.example.com
  -> HAProxy :443
  -> Synapse :8008 (loopback only)
  -> PostgreSQL :5432 (internal only)

Federation
  -> https://example.com/.well-known/matrix/server
  -> matrix.example.com:443
  -> HAProxy :443
  -> Synapse :8008
```

---

## Public Ports and Why

### Public

- `80/tcp`
  - used for HTTP to HTTPS redirect
  - useful for certificate issuance and renewal
- `443/tcp`
  - used by Matrix clients
  - used by Matrix federation
  - used for `.well-known` discovery

### Internal Only

- `8008/tcp`
  - Synapse listener
  - should stay bound to `127.0.0.1` only
- `5432/tcp`
  - PostgreSQL
  - should never be exposed publicly

### Not Needed Publicly

- `8448/tcp`
  - not required if federation is delegated correctly through `443`

---

## DNS and Domain Design

Recommended records:

- `A example.com -> YOUR_PUBLIC_IP`
- `A matrix.example.com -> YOUR_PUBLIC_IP`

If you use Cloudflare:

- `example.com` may be `Proxied` or `DNS only`, depending on your website setup
- `matrix.example.com` should stay `DNS only` for simpler and more predictable Matrix federation

### Why this matters

Matrix is sensitive to reverse proxy behavior, TLS handling, and long-lived connections.

For a stable setup, it is usually better to keep the actual homeserver hostname direct and simple.

---

## .well-known Delegation

If your Matrix `server_name` is `example.com`, you should publish these files on:

```text
https://example.com/.well-known/matrix/server
https://example.com/.well-known/matrix/client
```

### `/.well-known/matrix/server`

```json
{
  "m.server": "matrix.example.com:443"
}
```

### `/.well-known/matrix/client`

```json
{
  "m.homeserver": {
    "base_url": "https://matrix.example.com"
  }
}
```

Important:

- `/.well-known/matrix/client` should return `Access-Control-Allow-Origin: *`
- use a valid public TLS certificate
- do not depend on `8448` when this delegation is already in place

---

## Docker Deployment

This project uses Docker Compose for the Matrix stack itself.

The reverse proxy can stay on the host, which makes it easier to:

- reuse existing TLS handling
- control public ports centrally
- keep Synapse published only on loopback

Example file:

- [**docker-compose.yml.example**](setup_files/docker-compose.yml.example)

### Folder layout

Suggested local layout:

```text
/opt/matrix-synapse/
├── docker-compose.yml
├── data/
│   ├── synapse/
│   └── postgres/
└── homeserver.yaml
```

### Generate the initial Synapse config

According to the official Synapse Docker image workflow, generate a base config before starting the service normally:

```bash
mkdir -p /opt/matrix-synapse/data/synapse
cd /opt/matrix-synapse

docker run -it --rm \
  -v ./data/synapse:/data \
  -e SYNAPSE_SERVER_NAME=example.com \
  -e SYNAPSE_REPORT_STATS=no \
  matrixdotorg/synapse:latest generate
```

After that:

1. review the generated `homeserver.yaml`
2. replace the database section to use PostgreSQL
3. set `public_baseurl`
4. confirm the listener stays on `8008`
5. disable open registration

Reusable example:

- [**homeserver.yaml.example**](setup_files/homeserver.yaml.example)

### Start the stack

```bash
cd /opt/matrix-synapse
docker compose up -d
docker compose ps
docker compose logs -f synapse
```

---

## Docker Compose Notes

In this design:

- `Synapse` is published only on `127.0.0.1:8008`
- `PostgreSQL` is not published at all
- `HAProxy` is the only component exposed on `80` and `443`

This is intentional.

Even when the service is containerized, I still prefer to keep public ingress centralized in one reverse proxy.

---

## Example Docker Compose

The example compose file included here follows this pattern:

- official `matrixdotorg/synapse` image
- dedicated `postgres` container
- bind mount for Synapse data
- bind mount for PostgreSQL data
- loopback-only published Synapse port

If you want to reuse it:

1. copy `docker-compose.yml.example` to `docker-compose.yml`
2. replace all placeholder values
3. make sure `homeserver.yaml` matches your chosen domain
4. start the containers

---

## HAProxy Reverse Proxy

This project uses `HAProxy` as the public entry point.

Example file:

- [**haproxy.cfg.example**](setup_files/haproxy.cfg.example)

### What HAProxy does here

- listens on `80`
- redirects plain HTTP to HTTPS
- listens on `443`
- routes Matrix requests to `127.0.0.1:8008`
- optionally serves the `.well-known` responses on the root domain
- denies unrelated paths by default

### Why HAProxy was a good fit here

- simple and fast reverse proxy
- works well for host-based routing
- keeps public port ownership in one place
- makes it easy to separate public TLS from the application container

---

## TLS

Use a valid public certificate for:

- `matrix.example.com`
- `example.com` if it also serves `.well-known`

If `HAProxy` terminates TLS, prepare a PEM bundle for each certificate as needed by your HAProxy layout.

Placeholder example:

```bash
cat fullchain.pem privkey.pem > /etc/haproxy/certs/matrix.example.com.pem
```

Adapt paths and certificate handling to your own environment.

---

## Creating the First Admin User

To create the first user after Synapse is running:

```bash
docker exec -it synapse \
  register_new_matrix_user http://localhost:8008 \
  -c /data/homeserver.yaml
```

If your `registration_shared_secret` is stored in an additional config file, include that file as well.

Example logic:

```bash
docker exec -it synapse \
  register_new_matrix_user http://localhost:8008 \
  -c /data/homeserver.yaml \
  -c /data/conf.d/20-postgres-and-security.yaml
```

---

## Validation Commands

Useful checks after deployment:

```bash
curl -i http://127.0.0.1:8008/_matrix/client/versions
curl -i https://matrix.example.com/_matrix/client/versions
curl -i https://example.com/.well-known/matrix/server
curl -i https://example.com/.well-known/matrix/client
docker compose ps
docker compose logs --tail=100 synapse
docker compose logs --tail=100 postgres
```

---

## Security Notes

Recommended baseline:

- keep `enable_registration: false`
- do not expose `8008`, `8448`, or `5432`
- use strong unique secrets
- back up signing keys and database
- keep Docker images updated carefully
- protect the server with firewall rules
- keep administrative access private

Files and data that should be backed up:

- `homeserver.yaml`
- signing keys
- `registration_shared_secret`
- `macaroon_secret_key`
- PostgreSQL data
- uploaded media

---

## Placeholders To Replace

Before reusing this project, replace:

- `example.com`
- `matrix.example.com`
- `YOUR_PUBLIC_IP`
- `YOUR_ADMIN_USER`
- `YOUR_STRONG_PASSWORD`
- local file paths
- certificate paths

This public version intentionally avoids real domains, credentials, internal IPs, and private infrastructure details.

---

## Included Files

- [**docker-compose.yml.example**](setup_files/docker-compose.yml.example)
- [**homeserver.yaml.example**](setup_files/homeserver.yaml.example)
- [**haproxy.cfg.example**](setup_files/haproxy.cfg.example)

---

## Official References

Official documentation consulted:

- Synapse installation: <https://element-hq.github.io/synapse/latest/setup/installation.html>
- Synapse sample config note: <https://element-hq.github.io/synapse/latest/usage/configuration/homeserver_sample_config.html>
- Official Docker image: <https://hub.docker.com/r/matrixdotorg/synapse>

---

## Conclusion

This project is a practical Matrix / Synapse deployment focused on a clean domain design, low public exposure, and maintainable operation.

The main idea is simple: keep Synapse private behind `HAProxy`, expose only what Matrix actually needs, and document the full flow clearly enough to reproduce it later.
