from flask import Flask
from flask_restful import Resource, Api
from security import authenticate, identity
from flask_jwt import JWT, jwt_required

# For Authentication, we need 2 more script files.
# security.py and user.py
# Security - Auth
# User - Identity


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

api = Api(app) 
jwt = JWT(app, authenticate, identity)

puppies = []

class PuppyNames(Resource):

    def get(self, name):
        for puppy in puppies:
            if puppy['name'] == name:
                return puppy
        return {'name':None}, 404

    
    def post(self, name):
        add_pup = {'name':name}
        puppies.append(add_pup)

        return add_pup

    def delete(self, name):
        for index, puppy in enumerate(puppies):
            if puppy['name'] == name:
                del_pup = puppies.pop(index)
                return {'note':'delete success'}

class AllNames(Resource):

    # Apply with @jwt_required to have it be required to be authenticated.
    @jwt_required()
    def get(self):
        return {'puppies':puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__ == "__main__":
    app.run(debug=True)