from flask import Flask
import json
import requests
from services import ticker_service

app = Flask(__name__)

@app.route("/tickers")
def get_tickers():
    url = 'https://api-pub.bitfinex.com/v2/tickers?symbols=ALL'
    req = requests.get(url)
    tickers = ticker_service.get_tickers(req.json())
    return json.dumps(tickers)


@app.route("/other")
def other_test():
    return {"message": 'I am another end point'}


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)