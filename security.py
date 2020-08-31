# Note: File name could be anything.
# The data in here can be stored in a database but in this case, we won't.

# Import the User() class from the user.py
from user import User

# The list, the username_table and the userid_table mimics the Models of a database
users = [ 
    User(1, 'Jose', 'mypassword'),
    User(2, 'Mimi', 'passecret')
]

# Mapping to easily access this list's data
# This creates a dictionary out of the given data
username_table = {u.username: u for u in users}
# So that it's possible to do, for example, username_table['Jose']

# Builds a dictionary out of the list
userid_table = {u.id: u for u in users}

# Authenticates user
def authenticate(username, password):
    # Check if user exists
    # Better to do this:
    user = username_table.get(username, None)
    # Instead of username_table[username'] for Key grabbing purposes
    # If not found, return None

    if user and password == user.password:
        return user
    
# Solely based on the Flask-JWT Documentation
# Handles the identity of user
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


    