from flask import Flask
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    serverdata = [
        {
            "players": 4,
            "chips": [
                {"color":"white2","amount":"100","value":1,"id":1},
                {"color":"green","amount":"100","value":5,"id":2},
                {"color":"red","amount":"100","value":10,"id":3},
                {"color":"blue","amount":"50","value":50,"id":4},
                {"color":"black","amount":"50","value":100,"id":5}
            ],
            "timePerPerson": 15,
        },
        {
            "players": 6,
            "chips": [
                {"color":"white2","amount":"100","value":1,"id":1},
                {"color":"green","amount":"100","value":5,"id":2},
                {"color":"red","amount":"100","value":10,"id":3},
                {"color":"blue","amount":"50","value":50,"id":4},
                {"color":"black","amount":"50","value":100,"id":5}
            ],
            "timePerPerson": 15,
        },
        {
            "players": 8,
            "chips": [
                {"color":"white2","amount":"100","value":1,"id":1},
                {"color":"green","amount":"100","value":5,"id":2},
                {"color":"red","amount":"100","value":10,"id":3},
                {"color":"blue","amount":"50","value":50,"id":4},
                {"color":"black","amount":"50","value":100,"id":5}
            ],
            "timePerPerson": 15,
        }
    ]

    return json.dumps(serverdata), 200

if __name__ == "__main__":
    app.run()