from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
scaler = joblib.load("scaler.joblib")
model = joblib.load("agglo_model.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    cluster = None
    if request.method == "POST":
        try:
            age = float(request.form['age'])
            income = float(request.form['income'])
            visits = float(request.form['visits'])
            score = float(request.form['satisfaction'])
            user_input = np.array([[age, income, visits, score]])
            scaled_input = scaler.transform(user_input)
            prediction = model.fit_predict(scaled_input)  # for agglomerative
            cluster = prediction[0]
        except:
            cluster = "Error"
    return render_template("index.html", cluster=cluster)

if __name__ == "__main__":
    app.run(debug=True)
