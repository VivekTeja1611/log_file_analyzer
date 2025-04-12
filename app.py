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
        f.save('Apache_2k.log')

        # run the script with os.system (not subprocess)
        os.system('bash script.sh Apache_2k.log')       
        return render_template("acknowledgment.html")

app.run(debug=True)
