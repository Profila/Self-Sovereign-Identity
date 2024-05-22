# Profila SSI

## Startup Instructions

### Prism (aka Identus) Agent

1. Start a Prism Agent (https://github.com/hyperledger-labs/open-enterprise-agent) with the following settings (Tested with version 1.31.0):

    -   Create the file `infrastructure/local/.env-tenant` in Prism and add the folling content. Take note of the `ADMIN_TOKEN` value. 

        ```
        ADMIN_TOKEN=my-admin-token
        API_KEY_ENABLED=true
        API_KEY_AUTO_PROVISIONING=false
        DEFAULT_WALLET_ENABLED=false
        PRISM_AGENT_VERSION=1.18.0
        PRISM_NODE_VERSION=2.2.1
        PORT=8080
        NETWORK=prism
        VAULT_DEV_ROOT_TOKEN_ID=root
        PG_PORT=5434
        ```
2. Start Prism Agent with the following command:
    -   ```bash
        ./infrastructure/local/run.sh -n agent -b -e ./infrastructure/local/.env-tenant -p 8080 -d $(docker run --rm --net=host eclipse/che-ip)
        ````
        

### Prism API

1. Create a .env file (see .env-example)

2. Start the API by running `docker-compose up`
