class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}"