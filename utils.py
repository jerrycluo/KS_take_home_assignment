import yfinance as yf
from datetime import date as dt, timedelta as delta
import statsmodels.api as sm

def calculate_beta(symbol,yrs=3,slope=True):
    #formulas & methods: https://www.benzinga.com/money/how-to-calculate-beta
    #defaults to using slope formula on 3 years of closing data
    
    if(slope):
        return linear_regression(symbol,yrs)
    else:
        return variance_formula(symbol,yrs)

def variance_formula(symbol,yrs):
    # using variance formula

    #Get pd Series data for daily Stock closind data over previous # of years (default 3)
    T = yf.Ticker
    individual_close = T(symbol).history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']
    market_close = T('^GSPC').history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']

    #Apply Variance-Covariance Formula
    beta = individual_close.cov(market_close) / market_close.var()
    return beta

def linear_regression(symbol,yrs):
    # using linear regression

    #Get pd Series data for daily Stock closind data over previous # of years (default 3)
    T = yf.Ticker
    individual_close = T(symbol).history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']
    market_close = T('^GSPC').history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']

    #Dropping first row with NaN as percentage change
    individual_pct_change = individual_close.pct_change().iloc[1:]
    market_pct_change = market_close.pct_change().iloc[1:]

    #create model
    X = sm.add_constant(market_pct_change)
    model = sm.OLS(individual_pct_change, X)
    results = model.fit()
    beta = results.params[1]
    return beta