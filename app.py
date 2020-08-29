from flask import Flask
from flask_restful import Resource, Api
# Main entry point is the Api
# Resource represents an abstract REST resource

app = Flask(__name__)
api = Api(app)

# In this example, we'll only be using a List to return data.
# But later on we'll be using a database.

# For now, we'll have puppies in a list of dictionaries.
# Example content: {'name':"Rufus"}
puppies = []

class PuppyNames(Resource):
# All functions/definitions need to have the same parameter.
# So if you'll have (self) as a parameter it must be applied to all.

    # Get the puppies
    def get(self, name):
        # Get all puppies
        for puppy in puppies:
            # In every dictionary, get the pair data.
            if puppy['name'] == name:
                return puppy

        # Only executes if it's empty
        # Returns a 404 HTTP Error Code
        return {'name':None}, 404

    # Add a puppy
    def post(self, name):
        # Create an instance of a dictionary, then append it into the list.
        add_pup = {'name':name}
        puppies.append(add_pup)

        return add_pup

    # Delete a puppy
    def delete(self, name):

        # Reads all puppies and numbers them
        for index, puppy in enumerate(puppies):
            # Then look for the puppy with the name given
            if puppy['name'] == name:
                # Out of the index of the puppy, delete/pop it.
                del_pup = puppies.pop(index)
                return {'note':'delete success'}

# This gets the list of ALL puppies
class AllNames(Resource):

    def get(self):
        # Simply returns every puppy
        return {'puppies':puppies}

# Register the resources.
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__ == "__main__":
    app.run(debug=True)