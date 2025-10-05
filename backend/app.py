from app import create_app
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# from routes import routes, logged_out_tokens

# from auth_social import auth_social_bp
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)


# ------------------ Run Server ------------------
if __name__ == '__main__':
    app=create_app()
    app.run(debug=True, port=5000)