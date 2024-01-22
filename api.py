import json
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
{'id': 1, 'name':'Harry'},
{'id': 2, 'name':'Zach'},
{'id': 3, 'name':'Walter'}
]

nextUserId = 4

# GET users
@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(users)

# GET user by user ID
@app.route('/users/<int:id>', methods=['GET'])
def get_users_by_id(id: int):
 user = get_user(id)
 if user is None:
   return jsonify({ 'error': 'User does not exist'}), 404
 return jsonify(user)
def get_user(id):
#Generator Expression which returns the user with 
# a requested ID or simply None:
 return next((u for u in users if u['id'] == id), None)

def user_is_valid(user):
    for key in user.keys():
        if key != 'name':
            return False
        return True

#POST a new user
@app.route("/users", methods=["POST"])
def create_user():
    global nextUserId
    user = json.loads(request.data)
    if not user_is_valid(user):
        return jsonify({ 'error': 'Invalid user properties.' }), 400
    user["id"]=nextUserId
    nextUserId += 1
    users.append(user)
    
    return "", 201, { 'location': f'/user/{user["id"]}' }

#DELETE a user by user ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id: int):
 global users
 user = get_user(id)
 if user is None:
   return jsonify({ 'error': 'User does not exist.' }), 404
 user = [u for u in users if u['id'] != id]
 return jsonify(user), 200

#SERVER
if __name__ == "__main__":
    app.run(port=5000)