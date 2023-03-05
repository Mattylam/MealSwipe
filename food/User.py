class User:
    def __init__(self, username):
        self.username = username
        self.file_path = "user.txt"
        # Check if user already exists
        if self.is_user_created():
            raise ValueError("User already exists!")
        # Add user to file
        with open(self.file_path, "a") as f:
            f.write(self.username + "\n")

    def is_user_created(self):
        # Check if user exists in file
        with open(self.file_path, "r") as f:
            users = f.read().splitlines()
        return self.username in users

# Create a new user
user1 = User("alice")

# Try to create a user with the same username
try:
    user2 = User("alice")
except ValueError as e:
    print(str(e))  # "User already exists!"

# Check if a user exists
user3 = User("bob")
print(user1.is_user_created())  # True
print(user2.is_user_created())  # True
print(user3.is_user_created())  # True
print(User("dave").is_user_created())  # False



