import os
from server import app
from models.User import User
from flask import Flask, request, jsonify

@app.route("/")
def home():
    return "API v1"

@app.route("/api/main", methods=["GET"])
def getlist():
    return jsonify({
        "name": "Tieso",
        "age": os.environ.get('TIMES', '3')
    })

@app.route("/api/main/<id>", methods=["GET"])
def select(id):
    return jsonify({
        "id": id,
        "name": "Tastico"
    })

@app.route("/api/main", methods=["POST"])
def create():
    try:
        new_user = User(request.json['name'], request.json['age'])

        new_user.name = "Onur"
        new_user.age = 35
        print(new_user.toJson())

    except Exception as e:
        print(e)
    return jsonify(new_user.toJson())

@app.route("/api/main/<id>", methods=["PUT"])
def update(id):
    return jsonify({
        "id": id,
        "name": request.json['name'],
        "age": request.json['age']
    })

@app.route("/api/main/<id>", methods=["DELETE"])
def delete(id):
    myobj = {
        "id": id
    }
    return jsonify(myobj)