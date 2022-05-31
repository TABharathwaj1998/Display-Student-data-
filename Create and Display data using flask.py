from flask import Flask, request, render_template, redirect

app = Flask(__name__,template_folder='template')


@app.route("/data/create")
def home():
    return render_template("create.html")
    
@app.route("/data/", methods = ['POST','GET'])
def display():
    if request.method == 'GET':
        return redirect("/data/create")
    if request.method == 'POST':
        studentID = request.form.get("studentID")
        firstName = request.form.get("firstName")
        lastName  = request.form.get("lastName")
        dob = request.form.get("dob")
        amountDue = request.form.get("amountDue")
        return render_template("data.html",studentID=studentID,firstName=firstName,lastName=lastName,dob=dob,amountDue=amountDue)

if __name__=="__main__":
    app.run()