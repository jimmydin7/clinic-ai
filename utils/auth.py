#goody json db controller

import json
import os

class DBController:
    def __init__(self, db_path="instance/db.json"):
        self.db_path = db_path

        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, "w") as f:
                json.dump({"users": []}, f)

    def _load_db(self):
        with open(self.db_path, "r") as f:
            return json.load(f)

    def _save_db(self, data):
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_user(self, username, password):
        data = self._load_db()

        if any(u["username"] == username for u in data["users"]):
            return False 
        

        data["users"].append({"username": username, "password": password})
        self._save_db(data)
        return True

    def remove_user(self, username):
        data = self._load_db()
        new_users = [u for u in data["users"] if u["username"] != username]
        if len(new_users) == len(data["users"]):
            return False
        


        data["users"] = new_users
        self._save_db(data)
        return True

    def user_exists(self, username):
        data = self._load_db()
        return any(u["username"] == username for u in data["users"])

    def validate_user(self, username, password):
        data = self._load_db()
        return any(u["username"] == username and u["password"] == password for u in data["users"])

    def list_users(self):
        data = self._load_db()
        return [u["username"] for u in data["users"]]
