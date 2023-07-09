from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/api",methods=["GET","POST"])

def qa():
    if request.method == "POST":
        
        data = {"result": "Thank you! I'm just a machine learning model"}
        return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model"}
    return jsonify(data)

app.run(debug=True)