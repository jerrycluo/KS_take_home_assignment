import yfinance as yf
from datetime import date as dt, timedelta as delta
import statsmodels.api as sm

def calculate_beta(symbol,yrs=7,slope=True):
    #formulas & methods: https://www.benzinga.com/money/how-to-calculate-beta
    #defaults to using slope formula on 7 years of daily closing data
    
    if(slope):
        return linear_regression(symbol,yrs)
    else:
        return variance_formula(symbol,yrs)

def linear_regression(symbol,yrs):
    # using linear regression, more intuitively gets beta from parameter 
    # linear regression assumptions should be met. 

    #Get pd Series data for daily Stock closind data over previous # of years (default 3)
    T = yf.Ticker
    individual_close = T(symbol).history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']
    market_close = T('^GSPC').history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']

    return fit_model(individual_close,market_close)

def fit_model(individual_close,market_close):
    #fits model for beta parameter
    
    #Dropping first row with NaN as percentage change
    individual_pct_change = individual_close.pct_change().iloc[1:]
    market_pct_change = market_close.pct_change().iloc[1:]

    #create model
    X = sm.add_constant(market_pct_change)
    model = sm.OLS(individual_pct_change, X)
    results = model.fit()
    beta = results.params.iloc[1]
    return beta


def variance_formula(symbol,yrs):
    # using variance formula, requires larger dataset and linear regression assumptions 
    # will not be used for FAANG stock calculations 

    #Get pd Series data for daily stock closing data over previous # of years (default 3)
    T = yf.Ticker
    individual_close = T(symbol).history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']
    market_close = T('^GSPC').history(start=dt.today()-delta(days=yrs*365), end=dt.today())['Close']

    #Apply Variance-Covariance Formula
    beta = individual_close.cov(market_close) / market_close.var()
    return beta


