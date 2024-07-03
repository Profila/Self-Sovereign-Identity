# Profila SSI

## Startup Instructions

### Identus Agent

1. Start a Identus Agent (https://github.com/hyperledger-labs/open-enterprise-agent) with the following settings:

    -   Create the file `infrastructure/local/.env-tenant` in Identus and add the folling content. Take note of the `ADMIN_TOKEN` value. 

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
2. Start Identus Agent with the following command:
    -   ```bash
        ./infrastructure/local/run.sh -n agent -b -e ./infrastructure/local/.env-tenant -p 8080 -d $(docker run --rm --net=host eclipse/che-ip)
        ````
        

### Identus SSI API

1. Create a .env file (see .env-example)

2. Start the API by running `docker-compose up`
