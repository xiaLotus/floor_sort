from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允許跨域請求，如果前端和後端在同一個域下，可以省略

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "K11-3F": {
            "name": "K11-3F",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "K11-3F-2",
                "south": "K11-3F-3"
            }
        },
        "K11-4F": {
            "name": "K11-4F",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "K11-4F 2",
                "south": "K11-4F 3"
            }
        },
        "K11-5F": {
            "name": "K11-5F",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "k11-5f-2",
                "south": "k11-5f-3"
            }
        },
        "K11-10F": {
            "name": "K11-10F",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "K11-10F-1",
                "south": "K11-10F-2"
            }
        },
        "K21-9F": {
            "name": "K11-10F",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "K11-10F-1",
                "south": "K11-10F-2"
            }
        },
        "其他": {
            "name": "其他",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "其他-1",
                "south": "其他-2"
            }
        },
        "suixiu": {
            "name": "suixiu",
            "type": "room",
            "description": "This is a room",
            "exits": {
                "north": "suixiu-1",
                "south": "suixiu-2"
            }
        },
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
