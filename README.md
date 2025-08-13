📊 CSV Analyzer Web App
A full-stack web application that allows users to upload a CSV file and get an automated, comprehensive data analysis report. The project uses a Python backend for data processing and a simple HTML/JavaScript frontend for user interaction.

✨ Features
File Upload: Upload any CSV file directly from your browser.

Automated Data Profiling: The backend uses the powerful ydata-profiling library to generate a detailed report, including descriptive statistics, missing values analysis, and correlations.

Dynamic UI: The web app displays a loading spinner during analysis and presents the final report directly in the browser.

Responsive Design: The user interface is built with Tailwind CSS for a clean, modern, and mobile-friendly design.

Robust Backend: The Flask backend handles file uploads, processes the data, and returns a sanitized HTML report.

🛠️ Technologies Used
Backend
Python: The core language for the backend logic.

Flask: A micro web framework for creating the server and API endpoints.

ydata-profiling: An open-source library for automated exploratory data analysis.

Pandas: A data analysis and manipulation library for handling CSV files.

Frontend
HTML: The structure of the web page.

JavaScript: For handling user events, making API calls, and updating the UI dynamically.

Tailwind CSS: A utility-first CSS framework for styling and creating a responsive layout.

⚙️ Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x

pip: Python's package installer

🚀 Installation and Setup
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository
Clone the project from your version control system (e.g., Git) into a local directory.

git clone <your-repository-url>
cd csv-analyzer

2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies and avoid conflicts.

On Windows:

python -m venv venv
venv\Scripts\activate

On macOS and Linux:

python3 -m venv venv
source venv/bin/activate

Your terminal prompt should now show (venv) to indicate the virtual environment is active.

3. Install Dependencies
With the virtual environment active, install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

4. Run the Backend Server
Navigate to the backend directory and start the Flask development server.

cd backend
python app.py

The server will start, and you should see a message like * Running on http://127.0.0.1:5001.

5. Open the Frontend
The frontend is a static HTML file. Simply open the index.html file in your web browser.

C:\path\to\your\project\frontend\index.html

👨‍💻 Usage
Open the index.html file in your browser.

Click the "Choose File" button and select a CSV file from your computer.

Click the "Upload & Analyze" button.

A loading spinner will appear while the backend processes the file.

Once the analysis is complete, a comprehensive HTML report will be displayed directly in the web page.

📜 License
This project is open-source and available under the MIT License.
