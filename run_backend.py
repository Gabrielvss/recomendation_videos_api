import recomendadiotn_utils  
from youtube_dl import YoutubeDL

import json


import time
queries =  ["machine+learning" , "data+science", "kaggle"]
new_videos = 'database.json'

def search_db():
    ydl = YoutubeDL({'ignoreerrors': True})

    with open(new_videos, 'w+') as output:
        for query in queries:
            for page in range(1,2):
                r = ydl.extract_info("ytsearchdate30:{}".format(query) , download=False)
                video_list = r['entries']
               
                for video in video_list:
                    if video is None: continue

                    p = recomendadiotn_utils.compute_prediction(video)    

                      
                    video_id = video.get('webpage_url', '')                  
                    data_front = {'title':video['title'], 'video_id':video_id }
                    data_front['score'] = float(p)
                    data_front['update_time'] = time.time()

                    output.write(f'{json.dumps(data_front)}\n')
                  


    return True
                       




    

        