def _parse_ticker(currency):
    ticker = {
        "SYMBOL": currency[0],
        "BID":currency[1], 
        "BID_SIZE": currency[2], 
        "ASK": currency[3], 
        "ASK_SIZE": currency[4], 
        "DAILY_CHANGE": currency[5], 
        "DAILY_CHANGE_RELATIVE": currency[6], 
        "LAST_PRICE": currency[7], 
        "VOLUME": currency[8], 
        "HIGH": currency[9], 
        "LOW": currency[10]
    }
    return ticker
def get_tickers(currencies):
    return [_parse_ticker(currency) for currency in currencies]