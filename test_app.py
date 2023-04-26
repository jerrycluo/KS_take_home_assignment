from flask import Flask
from handlers.routes import configure_routes
from utils import calculate_beta, fit_model
import pandas as pd
import numpy as np
import json
import yfinance as yf

FAANG_SYMBOLS = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

INDIVIDUAL_TEST = pd.Series([128.67999267578125,
 131.3000030517578,
 139.0,
 141.02000427246094,
 133.3699951171875,
 131.4600067138672,
 125.4000015258789,
 121.86000061035156,
 128.64999389648438,
 133.44000244140625])

MARKET_TEST = pd.Series([2878.47998046875,
 2863.389892578125,
 2939.510009765625,
 2912.429931640625,
 2830.7099609375,
 2842.739990234375,
 2868.43994140625,
 2848.419921875,
 2881.18994140625,
 2929.800048828125])


def test_home():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello World'
    assert response.status_code == 200

def test_beta_faang():
    # Write test code below ...
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/beta'

    response = client.get(url)
    betas = json.loads(response.get_data().decode('utf-8'))

    #tests output Flask app outputs 
    assert isinstance(betas,dict), 'wrong betas type: {}. Expects dict'.format(type(betas))
    for symbol,beta in betas.items():
        dec = 4
        assert isinstance(beta, float), 'wrong beta type: {}. Expects float'.format(type(beta))
        assert symbol in FAANG_SYMBOLS, '{} is not a FAANG symbol'.format(symbol)
        assert round(beta,dec) == round(calculate_beta(symbol),4), 'incorrect beta for {}'.format(symbol)
        assert beta > -1 and beta < 3, 'beta value {} out of valid range [-1,3]'.format(beta)

    #tests calculate_beta function 
    assert round(calculate_beta('META',yrs=5),4) == 1.2728, 'wrong beta for 5 year period'

    #tests fit_model subfunction on hardcoded individual and market closing data series
    actual = round(fit_model(INDIVIDUAL_TEST,MARKET_TEST),4)
    assert actual == 1.7528, 'incorrect beta for manual test. Expected: 1.7528, Actual: {}'.format(actual)

    assert response.status_code == 200
    print('All beta unit tests passed')

def validate_against_yfinance_beta():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/beta'

    response = client.get(url)
    betas = json.loads(response.get_data().decode('utf-8'))

    diff = {}
    for i in betas:
        diff[i] = abs(betas[i] - yf.Ticker(i).info['beta'])
                    
    print('difference between calculated beta and yahoo finance beta for each FAANG stock:')
    print(diff)

test_home()
test_beta_faang()
validate_against_yfinance_beta()
