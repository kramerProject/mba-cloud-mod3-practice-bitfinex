FROM alpine:3.17.0

FROM alpine:3.17.0

WORKDIR /app

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY ./src /app

CMD [ "python3", "main.py" ]