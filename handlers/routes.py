def configure_routes(app):
    
    @app.route('/')
    def home():
        return 'Hello World', 200
    
    @app.route('/beta', methods=["GET"])
    def beta_faang():
        # Write your code below ...
        pass