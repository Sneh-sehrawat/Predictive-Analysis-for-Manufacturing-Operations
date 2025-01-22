#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib



# # Generating synthetic dataset

# In[11]:


def generate_data():
    np.random.seed(42)
    data = pd.DataFrame({
        "Machine_ID": np.arange(1, 101),
        "Temperature": np.random.randint(50, 100, 100),
        "Run_Time": np.random.randint(100, 500, 100),
        "Downtime_Flag": np.random.choice([0, 1], size=100, p=[0.8, 0.2])
    })
    data.to_csv("manufacturing_data.csv", index=False) 
    print("Dataset created and saved as 'manufacturing_data.csv'")
    return data



# # Model Training

# In[12]:


def train_model():
    # Loading dataset
    data = pd.read_csv("manufacturing_data.csv")
    X = data[["Temperature", "Run_Time"]]
    y = data["Downtime_Flag"]

    # Splitting dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training Decision Tree Classifier
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluating model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Saving model
    joblib.dump(model, "model.pkl")
    print("Model saved as 'model.pkl'")




# In[13]:


if __name__ == "__main__":
    generate_data()
    train_model()


# In[ ]:




