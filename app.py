from flask import Flask
from flask_restful import Resource, Api
# Main entry point is the Api
# Resource represents an abstract REST resource

app = Flask(__name__)

api = Api(app)

# Create a resource
class HelloWorld(Resource):
    # This is where you specify GET, POST, etc.
    def get(self):
        # Returned in JSON
        return {'hello':'world'}

# Note that HelloWorld =/= HelloWorld()
# So in this case it's not creating an instance of the class HelloWorld
# It is simply directly passing in the class itself
api.add_resource(HelloWorld, '/')
# api.add_resource(<class_resource>, <route>)


if __name__ == "__main__":
    app.run(debug=True)