"""creates variable app, instance of Flask"""
from flask import Flask
from models import storage
from api.v1.views import app_views


# Create a Flask app
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


# Method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    import os

    # Get the host and port from environment variables or use default values
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))

    # Run the Flask server
    app.run(host=host, port=port, threaded=True)
