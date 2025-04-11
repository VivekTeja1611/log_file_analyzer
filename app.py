from flask import Flask, redirect, render_template, request, send_file
from werkzeug.utils import secure_filename
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        filepath = os.path.join("uploads", filename)
        f.save(filepath)

        # Correctly passing the filename as an argument
        result = subprocess.run(['bash', 'script.sh', filepath], capture_output=True, text=True)
        
        # Optional: print output or pass it to the HTML
        print(result.stdout)

        return render_template("acknowledgment.html", output=result.stdout)

app.run(debug=True)
