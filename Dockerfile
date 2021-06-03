FROM python:3.9-buster

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./kindergartent ./
RUN chmod +x app.sh
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

EXPOSE 8000/tcp

ENTRYPOINT ./app.sh
