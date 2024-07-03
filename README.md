# Profila SSI

## Startup Instructions

### Prism (aka Identus) Agent

1. Start a Prism Agent (https://github.com/hyperledger-labs/open-enterprise-agent) with the following settings:

    -   Create the file `infrastructure/local/.env-tenant` in Prism and add the folling content. Take note of the `ADMIN_TOKEN` value. 

        ```
        ADMIN_TOKEN=my-admin-token
        API_KEY_ENABLED=true
        API_KEY_AUTO_PROVISIONING=false
        DEFAULT_WALLET_ENABLED=false
        AGENT_VERSION=1.37.0
        PRISM_NODE_VERSION=2.3.0
        PORT=8080
        NETWORK=identus
        VAULT_DEV_ROOT_TOKEN_ID=root
        PG_PORT=5434

        ```
2. Start Prism Agent with the following command:
    -   ```bash
        ./infrastructure/local/run.sh -n agent -b -e ./infrastructure/local/.env-tenant -p 8080 -d "$(ip addr show $(ip route show default | awk '/default/ {print $5}') | grep 'inet ' | awk '{print $2}' | cut -d/ -f1)"
        ````
        

### Prism API

1. Create a .env file (see .env-example)

2. Start the API by running `docker-compose up`
