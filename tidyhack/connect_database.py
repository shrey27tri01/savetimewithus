from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os 

CLIENT_ID = 'Enter Client ID here'
CLIENT_SECRET = 'Enter Client Secret here'


path = 'Enter Path here'
user = 'Enter Username here'
password = 'Enter Password here'

cloud_config= {
        'secure_connect_bundle': path,
}
auth_provider = PlainTextAuthProvider(CLIENT_ID,CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")