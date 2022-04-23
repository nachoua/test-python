from flask import Flask,redirect,render_template
app = Flask(__name__)
@app.route("/home")
def home():
    return render_template('calcule-tablee.html')
#fyy7@app.route("/<name>")
#def user(name):
   #return f"text-align: center;helloo {name}!"
#@app.route("/admin")
#def admin():
    #return redirect(url_for("user", name="Admin!"))
if __name__=="__main__":
 app.run(debuggg=True)