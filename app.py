from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('.env')

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask server!"

if __name__ == '__main__':
    port = int(os.getenv('PORT'))  # fallback to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
