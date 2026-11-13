from flask import Flask, app, render_template, request 

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form["data"]
    return f"Received: {data}" 























if __name__ == "__main__":
    
    app.run(debug=True)