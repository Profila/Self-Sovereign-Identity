# Profila SSI

## Startup Instructions

### Identus Agent

1. cd to ./identus/scripts/

    Define the following environment variables in a .env file:

    ```bash
        ADMIN_TOKEN=changethis
        API_KEY_ENABLED=true
        API_KEY_AUTO_PROVISIONING=true
        DEFAULT_WALLET_ENABLED=false
        AGENT_VERSION=1.37.0
        PRISM_NODE_VERSION=2.3.0
        PORT=8080
        NETWORK=identus
        VAULT_DEV_ROOT_TOKEN_ID=changethis
        PG_PORT=5434

        PGA_DEFAULT_EMAIL=changethis@mail.com
        PGA_DEFAULT_PASSWORD=changethis
    ````

2. Start Identus Agent with the following command (While in ./identus/scripts/):
    ```bash
        ./run.sh -n agent -b -e ./.env -p 8080 -d $(docker run --rm --net=host eclipse/che-ip)
    ````
        

### Identus SSI API

1. cd to the root of the repo.

2. Create a .env file (see .env-example)

3. Start the API by running `docker compose up -d`
