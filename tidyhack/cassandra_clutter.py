from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


path = 'Enter Path here'
user = 'Enter Username here'
password = 'Enter Password here'

cloud_config = {
    'secure_connect_bundle': path,
}
auth_provider = PlainTextAuthProvider(username=user, password=password)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


row = session.execute("select * from task.task").one()
if row:
    print(row)
else:
    print("An error occurred.")
    print("try checking the credentials once.")
