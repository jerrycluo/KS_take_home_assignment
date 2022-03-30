import os
from flask import Flask
from handlers.routes import configure_routes

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

configure_routes(app)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)