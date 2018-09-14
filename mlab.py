import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds237932.mlab.com:37932/trasua

host = "ds237932.mlab.com"
port = 37932
db_name = "trasua"
user_name = "admin"
password = "Thu,1999"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())