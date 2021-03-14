curl --request POST \
    --url https://${ASTRA_DB_ID}-${ASTRA_DB_REGION}.apps.astra.datastax.com/api/rest/v1/keyspaces/${ASTRA_DB_KEYSPACE}/tables/rest_example_products/rows \
    --header 'content-type: application/json' \
    --header "x-cassandra-token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --data '[{"columns":[{"name":"title","value":"Get milk"},{"name":"description","value":"get milk from nearby grocery store"},{"name":"author","value":"3"}}]'
