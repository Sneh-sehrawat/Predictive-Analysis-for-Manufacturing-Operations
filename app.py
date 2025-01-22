#!/usr/bin/env python
# coding: utf-8

# In[14]:


from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Uploading endpoint
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save("uploaded_data.csv")
    return jsonify({"message": "File uploaded successfully."})

# Training endpoint
@app.route('/train', methods=['POST'])
def train():
    # Load uploaded data
    data = pd.read_csv("uploaded_data.csv")
    X = data[["Temperature", "Run_Time"]]
    y = data["Downtime_Flag"]

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X, y)

    # Save trained model
    joblib.dump(model, "model.pkl")
    return jsonify({"message": "Model trained successfully."})

# Predicting endpoint
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    temperature = input_data["Temperature"]
    runtime = input_data["Run_Time"]

    # Load model and make prediction
    model = joblib.load("model.pkl")
    prediction = model.predict([[temperature, runtime]])
    confidence = model.predict_proba([[temperature, runtime]]).max()

    return jsonify({
        "Downtime": "Yes" if prediction[0] == 1 else "No",
        "Confidence": round(confidence, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




