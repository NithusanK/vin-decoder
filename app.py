
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
    error = None  # Stores error messages for display

    if request.method == "POST":
        vin = request.form["vin"].strip().upper()  # Get and sanitize the VIN input
        if len(vin) == 17:
            # Prepare the API URL
            url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                vehicle_data = {
                    item["Variable"]: item["Value"]
                    for item in data["Results"]
                    if item["Value"]
                }
            else:
                error = "Failed to fethc data from the NHTSA API."
        else:
            error = "VIN must be exactly 17 characters."

    # Render frontend template with either data or an error
    return render_template("index.html", vehicle_data=vehicle_data, error=error)


# Run the Flask app locally in debug mode
if __name__ == "__main__":
    app.run(debug=True)
