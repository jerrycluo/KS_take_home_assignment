
FAANG_SYMBOLS = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
#FAANG ticker symbols hard-coded

def configure_routes(app):

    @app.route('/')
    def home():
        return 'Hello World', 200
    
    @app.route('/beta', methods=["GET"])
    def beta_faang():
        # Write your code below ...
        # returns {symbol:beta} dict
        betas = {symbol:calculate_beta(symbol) for symbol in FAANG_SYMBOLS}
        return betas
