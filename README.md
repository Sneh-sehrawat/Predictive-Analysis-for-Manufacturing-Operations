
# **Predictive-Analysis-for-Manufacturing-Operations**

## **Overview**
This project implements a RESTful API for predicting machine downtime using a Decision Tree Classifier. The API supports:
- **Uploading manufacturing data in CSV format.**
- **Training a machine learning model on the uploaded dataset.**
- **Predicting downtime based on temperature and runtime inputs.**

---

## **What the Code Does**

### **model_training.py**
- **Generates** a synthetic manufacturing dataset (`manufacturing_data.csv`).
- **Trains** a Decision Tree Classifier to predict downtime based on temperature and runtime.
- **Saves** the trained model as `model.pkl`.

### **app.py**
- Implements a Flask API with the following endpoints:
  - **`/upload`**: Uploads a CSV dataset for training.
  - **`/train`**: Trains the model using the uploaded dataset.
  - **`/predict`**: Accepts temperature and runtime as inputs and returns downtime predictions.

### **manufacturing_data.csv**
- A sample dataset to test the API.

---

## **Instructions to Set Up and Run the API**

### **Step 1: Install Python**
1. Download and install Python 3.7 or higher from [python.org](https://www.python.org/).
2. Ensure Python is added to your system's PATH.

---

### **Step 2: Clone the Repository**
Clone this repository or download the files into a folder:
```bash
git clone <repository-link>
cd <repository-folder>
```

---

### **Step 3: Install Required Libraries**
Install the required Python libraries using `pip`:
```bash
pip install flask scikit-learn pandas numpy joblib
```

---

### **Step 4: Train the Model**
Run the `model_training.py` script to generate the synthetic dataset, train the machine learning model, and save the trained model:
```bash
python model_training.py
```

Confirm the creation of the following files:
- **`manufacturing_data.csv`**: The dataset used for training.
- **`model.pkl`**: The trained machine learning model.

---

### **Step 5: Start the API Server**
Run the `app.py` script to start the Flask API server:
```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`.

---

## **Example API Requests and Responses**

### **1. `/upload` Endpoint**

#### **Request**
- **URL**: `http://127.0.0.1:5000/upload`
- **Method**: `POST`
- **Body**: Upload a CSV file (e.g., `manufacturing_data.csv`).

#### **Using Postman**
1. Open Postman.
2. Select `POST` method.
3. Set the URL to `http://127.0.0.1:5000/upload`.
4. In the body, select `form-data` and upload the file:
   - **Key**: `file`
   - **Type**: File
   - **Value**: `manufacturing_data.csv`.

#### **Response**
```json
{
    "message": "File uploaded successfully."
}
```

---

### **2. `/train` Endpoint**

#### **Request**
- **URL**: `http://127.0.0.1:5000/train`
- **Method**: `POST`

#### **Using Postman**
1. Open Postman.
2. Select `POST` method.
3. Set the URL to `http://127.0.0.1:5000/train`.

#### **Response**
```json
{
    "message": "Model trained successfully."
}
```

---

### **3. `/predict` Endpoint**

#### **Request**
- **URL**: `http://127.0.0.1:5000/predict`
- **Method**: `POST`
- **Body**: JSON input containing `Temperature` and `Run_Time`.

#### **Using Postman**
1. Open Postman.
2. Select `POST` method.
3. Set the URL to `http://127.0.0.1:5000/predict`.
4. In the body, select `raw` and set the format to JSON. Add the following input:
   ```json
   {
       "Temperature": 85,
       "Run_Time": 300
   }
   ```

#### **Response**
```json
{
    "Downtime": "Yes",
    "Confidence": 0.85
}
```

---

## **Usage Summary**

1. **Setup**:
   - Install Python and required libraries.
   - Run `model_training.py` to generate the dataset and train the model.
2. **Run the API**:
   - Start the Flask server using:
     ```bash
     python app.py
     ```
   - Use tools like Postman or curl to interact with the API.
3. **Test the Endpoints**:
   - **Upload a dataset** using `/upload`.
   - **Train a model** using `/train`.
   - **Make predictions** using `/predict`.

---
