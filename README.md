# Profila SSI

## Startup Instructions

1. Start a Prism Agent with the following settings (Tested with version 1.31.0):

    -   Create the file `infrastructure/local/.env-issuer` in Prism and add the folling content. Take note of the `ADMIN_TOKEN` value. 

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
        ./infrastructure/local/run.sh -n agent -b -e ./infrastructure/local/.env-tenant -p 8080 -d "$(ip addr show $(ip route show default | awk '/default/ {print $5}') | grep 'inet ' | awk '{print $2}' | cut -d/ -f1)"
        ````
        


3. Create a .env file (see .env-example)

4. Start the API by running `docker-compose up`