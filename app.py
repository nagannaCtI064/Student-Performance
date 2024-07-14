from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from pymongo import MongoClient


app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("X_val.json", "r") as f:
    validation_data = pd.read_json(f)

all_data = validation_data.to_dict('records')

client=MongoClient("mongodb://localhost:27017/")
db=client["student"]
collection=db["student"]


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", all_data=all_data)

@app.route('/predict', methods=["POST"])
def predict():
    try:
        data = request.form.to_dict(flat=False)
        input_data = [float(data[field][0]) for field in data]
        input_data = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        document = {field: data[field][0] for field in data}
        document["prediction"] = prediction
        collection.insert_one(document)
        return render_template("home.html", all_data=all_data, prediction=prediction)
    except Exception as e:
        error = str(e)
        return render_template("home.html", all_data=all_data, error=error)
    

if __name__ == "__main__":
    app.run(debug=True)
