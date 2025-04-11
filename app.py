from flask import Flask,redirect,render_template,request,send_file
import subprocess
app=Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")
@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
       f=request.files['file']
       f.save(f.filename)
    result=subprocess.run(['bash','script.sh ,f.filename ',"uploads/"+f.filename],capture_output=True,text=True)
    return render_template("acknowledgment.html")
app.run()






