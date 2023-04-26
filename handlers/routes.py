from utils import calculate_beta

def configure_routes(app):
    
    FAANG_SYMBOLS = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    #FAANG ticker symbols hardcoded
    
    @app.route('/')
    def home():
        return 'Hello World', 200
    
    @app.route('/beta', methods=["GET"])
    def beta_faang():
        
        # {symbol:beta} dict comprehension
        betas = {symbol:calculate_beta(symbol) for symbol in FAANG_SYMBOLS}
        return betas
   
