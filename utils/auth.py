import json
import os
from datetime import datetime

class DBController:
    def __init__(self, db_path="instance/db.json"):
        self.db_path = db_path

        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, "w") as f:
                json.dump({"users": []}, f)

    def _load_db(self):
        try:
            with open(self.db_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {"users": []}
            self._save_db(data)
            return data


    def _save_db(self, data):
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_user(self, username, password, birthday=None, age=None):
        data = self._load_db()

        if any(u["username"] == username for u in data["users"]):
            return False 
        

        user_record = {"username": username, "password": password}
        if birthday is not None:
            user_record["birthday"] = birthday
        if age is not None:
            user_record["age"] = age
        
        user_record["test_results"] = []

        data["users"].append(user_record)
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

    def get_user(self, username):
        data = self._load_db()
        for user in data.get("users", []):
            if user.get("username") == username:
                if "test_results" not in user:
                    user["test_results"] = []
                    self._save_db(data)
                return user
        return None

    def save_test_result(self, username, test_type, test_data):
        data = self._load_db()
        
        for user in data["users"]:
            if user["username"] == username:
                if "test_results" not in user:
                    user["test_results"] = []
                
                test_result = {
                    "test_type": test_type,
                    "timestamp": datetime.now().isoformat(),
                    "data": test_data
                }
                
                user["test_results"].append(test_result)
                self._save_db(data)
                return True
        
        return False

    def get_user_test_results(self, username):
        user = self.get_user(username)
        if user and "test_results" in user:
            return user["test_results"]
        return []
