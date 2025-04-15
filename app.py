from flask import Flask, redirect, render_template, request, send_file
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save('Apache_2k.log')
        os.system('bash script.sh Apache_2k.log')  
        
        return render_template("acknowledgment.html")
 
app.run(debug=True)
