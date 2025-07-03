python

# vin-decoder/app.py


from flask import Flask, render_template, request  # Flask handles the web framework
import requests

# Create a new Flask web app instance
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for the VIN Decoder app.
    - Displays the form on GET request
    - Handles VIN form submission on POST request
    - Fetches data from the NHTSA VIN decoding API
    """
    vehicle_data = None  # Will hold decoded vehicle info
    error = None
