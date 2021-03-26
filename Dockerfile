FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    cmake \
    build-essential \
    gcc \
    g++ 
RUN pip install -r requirements.txt
RUN python db_started.py

#docker build . -t name_container
#docker run -e PORT=80 -p 80:80 container_name
#Creating ⬢ ytrec1... done
#https://ytrec1.herokuapp.com/ | https://git.heroku.com/ytrec1.git

CMD python app.py

