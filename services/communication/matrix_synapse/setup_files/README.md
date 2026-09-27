# Synapse Setup Files

## Overview

This folder contains the starter files used by the main Synapse project documentation.

These files are **templates**.

They are not ready to use exactly as they are.

Before starting the service, you must review them and replace the placeholder values with your own settings.

This guide was written for someone who may be using Docker, domains, reverse proxy, and Matrix for the first time.

---

## Before You Edit Anything

Before filling these files, you should know these values:

- your main domain
- your Matrix subdomain
- your server local IP address
- your public IP address
- whether ports `80` and `443` are already in use
- whether Docker and Docker Compose are already installed

If you do not know these yet, use the commands below.

### 1. Find your local IP address

Simplest command:

```bash
hostname -I
```

Typical result:

```text
192.168.1.50 172.17.0.1
```

How to read it:

- ignore `127.0.0.1`
- ignore Docker addresses like `172.x.x.x`
- the local server IP is usually something like:
  - `192.168.x.x`
  - `10.x.x.x`
  - `172.16.x.x` to `172.31.x.x`

In the example above, the local server IP would most likely be:

```text
192.168.1.50
```

More detailed command:

```bash
ip -brief addr
```

This is useful if the machine has more than one network interface.

### 2. Find your public IP address

```bash
curl ifconfig.me
```

This shows the public IP seen from the Internet.

This is usually the IP you point your domain to.

### 3. Check if ports `80` and `443` are already in use

```bash
sudo ss -tulpn | grep -E ':(80|443)\b'
```

If this command returns something, another service is already using one or both ports.

You must solve that before publishing Synapse on standard web ports.

### 4. Check if Docker Compose exists

```bash
docker compose version
```

If that works, Docker Compose is available.

If it does not, install Docker first before continuing.

---

## Files in This Folder

### `docker-compose.yml.example`

This file defines the containers used in the project.

In this case, it creates:

- one container for `PostgreSQL`
- one container for `Synapse`

What it controls:

- which images will be used
- container names
- environment variables
- volume mounts
- local port binding for Synapse
- restart behavior

Use this file when you want to start the Matrix stack with Docker Compose.

Recommended workflow:

```bash
cp docker-compose.yml.example docker-compose.yml
```

Then edit:

- database password
- timezone
- bind paths
- any values that should match your environment

For beginners:

- this file is what Docker Compose reads to start the containers
- you do not run the `.example` file directly forever
- usually you copy it, rename it, and then edit the real file

---

### `homeserver.yaml.example`

This file is the main Synapse configuration example.

It controls:

- your Matrix `server_name`
- the public URL used by clients
- the local listener port
- PostgreSQL connection settings
- registration behavior
- secret keys

This is one of the most important files in the project.

Use this file when you want to define how Synapse will behave.

Recommended workflow:

```bash
cp homeserver.yaml.example homeserver.yaml
```

Then replace:

- `example.com`
- `matrix.example.com`
- database password
- generated secrets

For beginners:

- this file controls how Synapse identifies itself
- if you choose the wrong `server_name`, changing it later is painful
- define the domain carefully before going live

---

### `haproxy.cfg.example`

This file is the reverse proxy example.

It shows how `HAProxy` can:

- listen on public `80`
- listen on public `443`
- redirect HTTP to HTTPS
- send Matrix traffic to Synapse
- serve `.well-known` responses
- block unrelated traffic by default

Use this file when you want to publish Synapse safely through a reverse proxy.

Recommended workflow:

```bash
cp haproxy.cfg.example /etc/haproxy/haproxy.cfg
```

Then replace:

- domain names
- certificate paths
- any custom routing rules used in your environment

Always test before reloading:

```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

For beginners:

- `HAProxy` is the service that receives traffic from the Internet first
- it decides what should go to Synapse
- it also helps keep Synapse itself off the public interface

---

## Which File Should Be Edited First

If you are starting from zero, this is the safest order:

1. edit `homeserver.yaml`
2. edit `docker-compose.yml`
3. edit `haproxy.cfg`
4. validate everything
5. start Synapse

Reason:

- `homeserver.yaml` defines the Matrix identity
- `docker-compose.yml` defines how Synapse runs
- `haproxy.cfg` defines how the outside world reaches the service

---

## What Each Placeholder Means

These are the most important placeholder values you will see.

### `example.com`

This is the main domain used as the Matrix identity.

Example:

```text
example.com
```

Real-world equivalent:

```text
mydomain.com
```

This value affects Matrix user IDs like:

```text
@alice:example.com
```

### `matrix.example.com`

This is the public hostname where Synapse is actually published.

Example:

```text
matrix.example.com
```

Real-world equivalent:

```text
matrix.mydomain.com
```

This is the hostname that clients and federation traffic will reach.

### `YOUR_PUBLIC_IP`

This is your public Internet IP.

This is usually the IP you place in your DNS `A` record.

### `127.0.0.1`

This means:

```text
the same machine
```

When used in this project, it means Synapse is only reachable locally on the server, not directly from the Internet.

### `REPLACE_WITH_A_STRONG_PASSWORD`

This means you must create a real password and replace the placeholder.

Do not leave placeholder values in production.

---

## Understanding Domains in a Simple Way

Many beginners confuse these values:

- machine hostname
- local IP
- public IP
- `server_name`
- public URL

They are not the same thing.

### Machine hostname

This is the Linux hostname of the machine.

Check it with:

```bash
hostnamectl
```

Example:

```text
server-lf1
```

This is local system identity only.

### Local IP

This is the private network address inside your house or lab.

Example:

```text
192.168.1.50
```

This is what your router uses for port forwarding.

### Public IP

This is the Internet-facing address given by your ISP.

Example:

```text
203.0.113.20
```

This is what your public DNS record points to.

### Matrix `server_name`

This is the permanent Matrix identity domain.

Example:

```text
example.com
```

This is what appears after the `:` in Matrix usernames.

### Public base URL

This is the actual HTTPS URL where Synapse is reached.

Example:

```text
https://matrix.example.com/
```

---

## Understanding the Ports

This project uses more than one port, and each one has a different purpose.

### Port `80`

This is standard HTTP.

In this project, it is used mainly for:

- redirecting users to HTTPS
- certificate validation in some setups
- simple public entry handling

### Port `443`

This is standard HTTPS.

It is the main public port for:

- Matrix clients
- Matrix federation
- secure access to the service

### Port `8008`

This is the Synapse application port.

In this project, Synapse listens here internally.

Important:

- this port should normally stay private
- it should not be exposed to the Internet
- the reverse proxy should connect to it locally

### Port `5432`

This is the PostgreSQL database port.

It is only for internal communication between Synapse and PostgreSQL.

This port should never be exposed publicly in this type of setup.

---

## How To Change the Synapse Port

If you want Synapse to use another internal port instead of `8008`, you must change it in more than one place.

Example:

You want to change Synapse from `8008` to `8010`.

### Step 1. Change it in `homeserver.yaml`

Find:

```yaml
port: 8008
```

Change to:

```yaml
port: 8010
```

### Step 2. Change it in `docker-compose.yml`

Find:

```yaml
ports:
  - "127.0.0.1:8008:8008"
```

Change to:

```yaml
ports:
  - "127.0.0.1:8010:8010"
```

### Step 3. Change it in `haproxy.cfg`

Find:

```haproxy
server synapse_local 127.0.0.1:8008 check
```

Change to:

```haproxy
server synapse_local 127.0.0.1:8010 check
```

### Step 4. Restart the service

After saving the changes:

```bash
docker compose down
docker compose up -d
sudo systemctl reload haproxy
```

### Important note

If you change the port in only one file, the service will break.

All related files must match.

---

## How To Change the Public Ports

Most people should keep:

- `80` for HTTP
- `443` for HTTPS

That is the standard setup, and it is the easiest one for Matrix clients and federation.

For beginners, this is the recommended rule:

- do not change public `80`
- do not change public `443`
- only change the internal Synapse port if you really need to

### Can I use different public ports?

Technically, yes.

But for Matrix, that usually creates unnecessary complexity.

If you publish the homeserver on a non-standard public port, you may need extra changes and can create problems for federation and discovery.

For beginners, the best approach is:

- keep public `80`
- keep public `443`
- only change the internal Synapse port if needed

---

## How To Change the Domain Names

You must replace placeholder domains in all example files.

Default placeholders used here:

- `example.com`
- `matrix.example.com`

Replace them with your own values.

### Where to change them

In `homeserver.yaml`:

- `server_name`
- `public_baseurl`

In `haproxy.cfg`:

- `hdr(host) -i example.com`
- `hdr(host) -i matrix.example.com`
- JSON responses inside `.well-known`
- certificate file names and paths

If you forget one of these places, login or federation may fail.

### Example

Before:

```text
example.com
matrix.example.com
```

After:

```text
mydomain.com
matrix.mydomain.com
```

---

## How To Generate Strong Secrets

Some values must not stay as placeholders.

For example:

- `macaroon_secret_key`
- `registration_shared_secret`
- database password

Generate strong values like this:

```bash
openssl rand -hex 32
```

Use a password manager or another secure place to store them.

Do not publish real secrets to GitHub.

---

## Basic Validation Before Starting

Before starting the stack, review these points:

- domains are correct
- passwords were replaced
- secrets were generated
- certificate paths are correct
- reverse proxy points to the same Synapse port used in the config
- PostgreSQL settings match between files

Useful checks:

```bash
docker compose config
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

If you want to edit files in a simple terminal editor:

```bash
nano docker-compose.yml
nano homeserver.yaml
```

Basic `nano` usage:

- type normally to edit
- `Ctrl + O` to save
- press `Enter` to confirm
- `Ctrl + X` to exit

---

## Basic Validation After Starting

After the containers are running, test:

```bash
curl -i http://127.0.0.1:8008/_matrix/client/versions
curl -i https://matrix.example.com/_matrix/client/versions
curl -i https://example.com/.well-known/matrix/server
curl -i https://example.com/.well-known/matrix/client
```

If you changed the internal Synapse port, replace `8008` in the local test command.

To see whether the containers are running:

```bash
docker compose ps
```

To read logs:

```bash
docker compose logs --tail=100 synapse
docker compose logs --tail=100 postgres
```

---

## Common Beginner Mistakes

- forgetting to replace `example.com`
- exposing `8008` publicly
- leaving weak placeholder passwords
- changing a port in only one file
- forgetting to update `.well-known`
- using wrong certificate paths
- not validating HAProxy before reload
- confusing public IP with local IP
- using the machine hostname as if it were the public domain
- forgetting to open or forward `80` and `443` on the router

---

## Router and Port Forwarding

If your server is inside your home network, your router usually needs port forwarding.

Typical rule:

- external `80/tcp` -> local server IP port `80`
- external `443/tcp` -> local server IP port `443`

Example:

```text
80/tcp  -> 192.168.1.50:80
443/tcp -> 192.168.1.50:443
```

This is why finding the correct local IP matters.

If the router points to the wrong local IP, the service will not work from outside.

---

## What a Total Beginner Should Do First

If this is your first time, follow this order:

1. find your local IP with `hostname -I`
2. find your public IP with `curl ifconfig.me`
3. decide your real domain names
4. copy the `.example` files into working files
5. replace all placeholders
6. validate Docker Compose
7. validate HAProxy
8. start the containers
9. test local Synapse response
10. test the public URLs

---

## Final Advice

If this is your first Synapse deployment, do not try to customize everything at once.

Start with:

- standard ports
- one domain pattern
- one reverse proxy
- one working config

After the service is stable, then improve or customize it.
