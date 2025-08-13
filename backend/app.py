# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from ydata_profiling import ProfileReport # Updated import
import os

# Initialize the Flask application
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) to allow the frontend to communicate with this backend
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_csv():
    """
    This endpoint receives a CSV file, analyzes it using ydata-profiling,
    and returns the analysis report as an HTML string.
    """
    # Check if a file was sent in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # Check if the file has a name
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file is a CSV
    if file and file.filename.endswith('.csv'):
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file)

            # Generate the profile report using ydata-profiling
            # The title of the report will be 'YData Profiling Report'
            profile = ProfileReport(df, title='YData Profiling Report', explorative=True)

            # Convert the report to an HTML string
            report_html = profile.to_html()

            # Return the HTML report as a JSON response
            return jsonify({'report': report_html})
        except Exception as e:
            # Handle any errors that occur during file processing or analysis
            return jsonify({'error': str(e)}), 500
    else:
        # Return an error if the file is not a CSV
        return jsonify({'error': 'Invalid file type. Please upload a CSV file.'}), 400

# Run the Flask app
if __name__ == '__main__':
    # You can specify the port number here
    app.run(debug=True, port=5001)