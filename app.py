from flask import Flask, request, make_response
from flask_cors import CORS
import json

def create_app():
    app = Flask(__name__)  
    CORS(app)
    return app


app = create_app()


@app.route("/api/v1/credit", methods=["POST"])
def post():
    body = json.loads(request.data)
    content = {"info":body,"result":evaluateValues(body['requiredAmount'])}
    response = make_response(content)
    response.headers["Content-Type"] = "application/json"
    return response



def evaluateValues(value):
    if value < 50000:
        return "Approved"
    elif value == 50000:
        return "Undecided"
    else:
        return "Declined"

