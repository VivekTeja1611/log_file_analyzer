Visit my wokr :https://log-file-analyzer.onrender.com/
Apache Log File Analyzer
This project is a web application designed to process and analyze Apache log files. It provides users with a simple interface to upload log files, filter data, and visualize patterns and trends through various charts. Additionally, it offers an advanced feature for users to generate custom plots using their own Python code.

Key Features
File Upload & Validation: Easily upload Apache log files through a user-friendly web interface.

Interactive Data Filtering: Filter log entries based on Level (e.g., [notice], [error]) and EventId to focus on specific data points.

Standard Visualizations: Automatically generates a variety of charts, including pie charts, line plots, and bar graphs, to provide quick insights.

Custom Plot Generation: An advanced feature that allows users to write and execute their own Python code to create custom plots using Matplotlib.

CSV Export: Download filtered data as a CSV file for further analysis in external tools.

Requirements
To run this project, you'll need the following installed:

Python 3

Flask: A web framework for Python.

Matplotlib: A plotting library for Python.

It is highly recommended to use a virtual environment to manage project dependencies.

Installation & Setup
Clone the Repository:

git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
cd your-repository


(Note: Replace the URL and directory name with your actual project details)

Create and Activate a Virtual Environment:

On Linux/macOS:

python3 -m venv venv
source venv/bin/activate


On Windows:

python -m venv venv
venv\Scripts\activate


Install Required Packages:

pip install flask matplotlib


Running the Application
From the project's root directory, run the main application file:

python3 app.py


Open your web browser and navigate to http://localhost:5000 to access the application.

Code Explained
The project is built around a series of Python and bash scripts that work together to process the log files.

app.py: This is the heart of the web application. It uses the Flask framework to manage all the web routes. It handles file uploads, processes form data from the user, and serves the correct HTML pages. It also coordinates the calls to the bash scripts for log processing and uses Matplotlib to generate the charts.

parsing_filtering.sh: This bash script is responsible for the initial parsing and filtering of the uploaded log file. It uses powerful command-line tools like sed and awk to efficiently extract specific log entries and data points, which are then used by the Python application for analysis.

filter_time.sh: Another bash script that performs time-based filtering on the log data. It allows the application to narrow down the analysis to a specific time range, which is especially useful for investigating specific events or trends.

default_filter.sh: This script sets up the initial or "default" visualization data for the application. It runs a set of standard filters to prepare the data for the pie charts, line plots, and bar graphs that are displayed on the graphs page.

Directory Structure
The project is organized into the following main directories and files:

project/
├── app.py                      # Main Flask application file
├── parsing_filtering.sh        # Bash script for log parsing
├── templates/                  # HTML templates for the web pages
│   ├── upload_page.html
│   ├── tabular_display.html
│   ├── graphs_page.html
│   └── plotter.html
├── static/                     # Static files like CSS and generated plots
│   ├── css/
│   └── (generated images)
└── Temporary_files/            # Temporary data files

