from flask import Flask, redirect, render_template, request, send_file
import os
import matplotlib
matplotlib.use('Agg') #using this to reduce loading speed
import matplotlib.pyplot as plt
import time

def not_show():
    pass
plt.show=not_show
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
        s_csv=time.time()
        EventId='All'
        Level='All'
        if request.form.get("EventId"):
            EventId=request.form.get("EventId")  
        if request.form.get("Level"):
           Level=request.form.get("Level")   
        #print(EventId,Level)
        if 'file' in request.files:
          f = request.files['file']
          f.save('Apache_2k.log')
        command=f"bash script.sh Apache_2k.log {Level} {EventId}"
        os.system(command)  
        e_csv=time.time()
        print(e_csv-s_csv,"for the execution of success...where page is csv file making") 
        return render_template("acknowledgment.html",selected_event=EventId,selected_level=Level)

  

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
              if line.strip()!= "EventId":
               arr.append(line.strip())
         
    #plt.figure(figsize=(14, 6.5))
    if x+y >0:       
         labels = ['[notice]', '[error] ']
         sizes = [x, y]
         colors = ['#ff9999', '#66b3ff']
        # plt.subplot(2,2,1)
         plt.pie(sizes, labels=labels,autopct='%1.1f%%', colors=colors)
         plt.title("Pie chart")
         plt.savefig("static/pie_plot.png")
         plt.close()
    else:
        #plt.subplot(2, 2, 1)
        plt.text(0.5, 0.5, 'No data in pie range', ha='center', va='center', fontsize=12)
        plt.axis('off')
        plt.title("Pie chart")     
        plt.close()

    #plt.subplot(2,2,2)
    plt.plot(arr_x,arr_y)
    # plt.gca().set_xticklabels([])
    plt.title("Line Plot")
    plt.savefig("static/plot_plot.png")
    
    plt.close()
    #plt.gca().set_xticklabels([]) #to hide the labels on x axis in line plot
    # plt.subplot(2,2,3)
    plt.hist(arr,bins=5,color='skyblue',edgecolor='black')
    plt.title("Bar Graph")
    plt.savefig("static/hist_plot.png")
    plt.close()





@app.route('/plot.html',methods=["POST"])
def plot():
    s1_plot=time.time()
    os.system('bash script2.sh static/Apache_2k.csv')
    with open("tmp1.txt",'r') as file:
        for line in file:
            print("time2:",line.strip())
            time2=int(line.strip())
    time1 = 1
    #time2 = "[Mon Dec 05 19:15:57 2005]"
    generate_plot(time1, time2)
    e1_plot=time.time()
    print(e1_plot-s1_plot,"for sefault plotting the time is this")
    return render_template("plot.html")     



@app.route("/submit", methods=["POST"])
def submit():
    s2_plot=time.time()
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
        e2_plot=time.time()
        print(e2_plot-s2_plot,"filter plotting time is this")
        return render_template("plot.html")




@app.route("/graph_plotter",methods=["post"])
def plotter():
         s_graph=time.time()
         plot_url=""
         code="""import matplotlib.pyplot as plt

# Data to plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
                
# Create a simple line plot
plt.plot(x, y)
 
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')    
# Show the plot
plt.show()
"""
         if request.form.get("text-box"):
            code=request.form.get("text-box")
            exec(code)
            plt.savefig("static/user_plot.png")
            plt.close()
            plot_url= "static/user_plot.png" 
           
            return render_template("plotter.html",plot_url=plot_url,code=code)
          
         else:
             e_graph=time.time()
             print(e_graph-s_graph,"time to graph is this")  
             return render_template("plotter.html",plot_url=plot_url,code=code)

        
app.run(debug=True)











































