# Typically, the User Models are stored into its own file.
# In this case, we will go simple and put it here instead.

# This script can be hashed and such, but for this case we won't.

class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    # For debugging purposes
    def __str__(self):
        return f"User ID: {self.id}"

