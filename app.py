from flask import Flask, redirect, render_template, request, send_file
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
        f = request.files['file']
        f.save('Apache_2k.log')
        os.system('bash script.sh Apache_2k.log')  
        return render_template("acknowledgment.html")


def generate_plot(X, Y):
    X=int(X)
    Y=int(Y)
    print("in generate func X and Y are:",X,Y)
    with open("notice_error", 'r') as file:
        x = 0
        y =0
        z = 0
        for line in file:
            if X <= z <= Y:
                if line.strip() == "[notice]":
                    x += 1
                elif line.strip() == "[error]":
                    y += 1
            z += 1
    with open("time",'r') as file:
     p=0
     q=0
     r=0
     dic={}
     for line in file:
         if X<=r<=Y:
             if line.strip() not in dic:
                 dic[line.strip()]=1
             else:
                 dic[line.strip()]+=1
         r+=1
     arr_x=list(dic.keys()) 
     arr_y=list(dic.values())   
    

    with open("events",'r') as file:
         arr=[]
         for line in file:
              arr.append(line.strip())
         
    plt.figure(figsize=(14, 6.5))
    if x+y >0:       
         labels = ['notice', 'error']
         sizes = [x, y]
         colors = ['#ff9999', '#66b3ff']
         plt.subplot(2,2,1)
         plt.pie(sizes, labels=labels, colors=colors)
    else:
        plt.subplot(2, 2, 1)
        plt.text(0.5, 0.5, 'No data in pie range', ha='center', va='center', fontsize=12)
        plt.axis('off')     

    plt.subplot(2,2,2)
    plt.plot(arr_x,arr_y)
    plt.gca().set_xticklabels([]) #to hide the labels on x axis in line plot
    plt.subplot(2,2,3)
    plt.hist(arr,bins=5,color='skyblue',edgecolor='black')
    plt.savefig("static/pie_plot.jpg")
    plt.close()




@app.route('/plot.html')
def plot():
    os.system('bash script2.sh static/Apache_2k.csv')
    with open("tmp1.txt",'r') as file:
        for line in file:
            print("time2:",line.strip())
            time2=int(line.strip())
    time1 = 1
    #time2 = "[Mon Dec 05 19:15:57 2005]"
    generate_plot(time1, time2)
    return render_template("plot.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        formatted1 = request.form['sdt'].strip()
        formatted2 = request.form['edt'].strip()
        with open("submitted_times.txt", "w") as f:
            f.write(f"{formatted1}\n")
            f.write(f"{formatted2}\n")
        print(formatted1,formatted2,"are the formatted times")
        os.system(f'bash script1.sh time submitted_times.txt')
        with open("tmp.txt",'r') as file:
            for line in file:
                line=line.split(',')
                X=line[0].strip()
                Y=line[1].strip()
            print(X,Y,"are the values of X,Y")    
        generate_plot(int(X), int(Y))

        return render_template("plot.html")


app.run(debug=True)











































