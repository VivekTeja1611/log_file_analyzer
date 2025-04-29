from flask import Flask, redirect, render_template, request
import os
import matplotlib
matplotlib.use('Agg') #using this to reduce loading speed
import matplotlib.pyplot as plt
import time
#To overwrite the plt.show() if the userr writes plt.show in text-editor
def not_show():
    pass
plt.show=not_show

app = Flask(__name__)



#upload page (index.html shows the upload page)
@app.route('/')
def main():
    return render_template("index.html")


#to dispay the Display page(csv table of uploaded file)
@app.route('/success', methods=['POST'])
def success():
        s_csv=time.time() #just to check run time
        EventId='All'
        Level='All'
        if request.form.get("EventId"):
            EventId=request.form.get("EventId")   #EventId input in filtering in display page
        if request.form.get("Level"):
           Level=request.form.get("Level")    #Level input in filtering in displlay page
        if 'file' in request.files:   
          f = request.files['file']
          f.save('Apache_2k.log')             #saving the uploaded file with name Apache_2k.log
        command=f"bash parsing_filtering.sh Apache_2k.log {Level} {EventId}"
        os.system(command)                    #runnig the bash script which parser as well as filters the csv table
        with open("tmp2.txt",'r') as file:    #To check  if the uploaded file is a valid Apache log file
            for line in file:
                print(line)
                if int(line.strip())==1:
                  st="only Apache log  files can be analyzed"
                  return render_template("index.html",st=st)  # to return error that wromg file is uploaded
        e_csv=time.time()                                      #to check code run time
        print(e_csv-s_csv,"for the execution of success...where page is csv file making")   #for debugging purpose
        return render_template("acknowledgment.html",selected_event=EventId,selected_level=Level)    #returning the Displlay page 

  
####This is  a function plots the grpahs based on line numbers in the file(line no's are generrated in a different way from the time inputs)
##this function will be used in later functions
def generate_plot(X, Y):
    X=int(X)
    Y=int(Y)
    print("in generate func X and Y are:",X,Y)
    with open("notice_error", 'r') as file:    #data for pie plot
        x = 0
        y =0
        z = 0
        for line in file:
            if X < z and z <= Y:
                print(line)
                if line.strip() == "[notice]":
                    x += 1
                elif line.strip() == "[error]":
                    y += 1
            z += 1
    with open("time",'r') as file:  #data for line plot
     p=0
     q=0
     r=0
     dic={}
     for line in file:
         if X<r and r<=Y:
             if line.strip() not in dic:
                 dic[line.strip()]=1
             else:
                 dic[line.strip()]+=1
         r+=1
     arr_x=list(dic.keys()) 
     arr_y=list(dic.values())   
    
    a,b,c=0,0,0
    with open("events",'r') as file:  #data for bar graph
         arr=[]
         for line in file:
              if X<c and c<=Y :
                arr.append(line.strip())
              c=c+1    
         counts = {}
         print(arr)
         print(set(arr),"this is the set of arr")
         for item in arr:
              if item in counts:
                  counts[item] += 1
              else:
                  counts[item] = 1

      ##data collection is done
      # now plotting        
    if x+y >0:       
         labels = ['[notice]', '[error] ']
         sizes = [x, y]
         colors = ['#ff9999', '#66b3ff']
         plt.pie(sizes, labels=labels,autopct='%1.1f%%', colors=colors)  #pie plotting
         plt.title("Pie chart")
         plt.savefig("static/pie_plot.png")
         plt.close()
    else:
        plt.text(0.5, 0.5, 'No data in pie range', ha='center', va='center', fontsize=12)
        plt.axis('off')
        plt.title("Pie chart")     
        plt.close()


    #line plot plotting
    plt.plot(arr_x,arr_y)     
    plt.title("Line Plot")
    plt.savefig("static/plot_plot.png")
    plt.close()


    labels = ['E1','E2','E3','E4','E5','E6']
    print(labels,"labels of bar graph")
    for k in labels:
        if k not in counts.keys():
            counts[k]=0
    values=counts.values()        
    print(values,"values of bar graph")
    colors = ['red', 'green', 'blue', 'orange','yellow','violet']  #
   
    #bar graph plotting
    plt.bar(labels, values,color=colors)   
    plt.title("Bar Graph")
    plt.savefig("static/hist_plot.png")
    plt.close()



#Page where graphs are visible
@app.route('/plot.html',methods=["POST"])
def plot():
    s1_plot=time.time()
    os.system('bash default_filter.sh static/Apache_2k.csv')   # this is used to find the default line numbers as i am using a function
    with open("tmp1.txt",'r') as file:                         #which takes line numbers as arguments (so usinng ths script)
        for line in file:
            print("time2:",line.strip())
            time2=int(line.strip())
    time1 = 1
    generate_plot(time1, time2)                                 # the default plot of the csv table(no filtering has been done)
    e1_plot=time.time()
    print(e1_plot-s1_plot,"for sefault plotting the time is this")
    return render_template("plot.html")     


##when we want to filter the graphs based on time

@app.route("/submit", methods=["POST"])
def submit():
    s2_plot=time.time()
    if request.method == "POST":
        formatted1 = request.form['sdt'].strip()
        formatted2 = request.form['edt'].strip() 
        with open("submitted_times.txt", "w") as f:   ##submittedd_times is a temporary file containg the submited times when doing filtering
            f.write(f"{formatted1}\n")
            f.write(f"{formatted2}\n")
        print(formatted1,formatted2,"are the formatted times")
        os.system(f'bash filter_time.sh time submitted_times.txt')   #
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











































