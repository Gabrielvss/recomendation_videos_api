from run_backend import search_db

from flask import Flask, jsonify
import json
import os
import time

app = Flask(__name__)

def get_predictions(update=False):
    videos = []
    new_videos_json = "database.json"
    if not os.path.exists(new_videos_json):
        search_db()
    if update: search_db() 

    #pegando os vídeos do arquivo json
    with open(new_videos_json, 'r') as data_file:
        if data_file is None: search_db()
        for line in data_file:
            line_json = json.loads(line)
            #tempo da extração até a consulta
            line_json["update_time"] = time.time() - line_json["update_time"]
            videos.append(line_json)
   
    videos = sorted(videos, key= lambda x: x['score'], reverse=True)

    return jsonify({"videos":videos})

@app.route('/', methods=['GET'])
def main_page():
   
    videos = get_predictions(update=False)

    return videos, 200

@app.route('/update', methods=['GET'])
def update_data():
   
    videos = get_predictions(update=True)

    return videos, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)