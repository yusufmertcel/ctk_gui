import pymongo
import json

path_db = "mongodb://localhost:27017/"

class DataBase():
    def __init__(self, db_name) -> None:
        self.client, self.db = self.connect_db(path_db, db_name)

        self.users_col = self.create_collection("users")
        self.images_col = self.create_collection("images")

        
    def connect_db(self, connection_str, db_name):
        client = pymongo.MongoClient(connection_str)
        if db_name in client.list_database_names():
            print("The database exists")
        db = client[db_name]
        return client, db

    def create_collection(self, collec_name):
        if collec_name in self.db.list_collection_names():
            print("The collection already exists.")
        return self.db[collec_name]
    
    def add_user(self, user):
        return self.users_col.insert_one(user)
    
    def add_many_user(self, users):
        return self.users_col.insert_many(users)
    
    def add_users_with_file(self, file_path):
        with open(file_path) as fh:
            mock_data = json.load(fh)
        return self.add_many_user(self.users_col, mock_data)

    def find_user(self, username):
        if username is None:
            query = {}
        else:
            query = {"username": username}
        result = self.users_col.find_one(query, {"username":1, "password":1, "name": 1})
        if result is not None:
            return (result["username"], result["password"], result["name"])
        return None, None, None

""" inst_db = DataBase("mydatabase")
doc = inst_db.users_col.find()
for x in doc:
    print(list(x.values())[0]) """