import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt


# STEP 1 - Load dataset
data = pd.read_csv("traffic_dataset.csv")

print("Dataset Loaded")
print(data.head())


# STEP 2 - Select Features
X = data[["PacketLength","Protocol"]]

y = data["Label"]


# STEP 3 - Split dataset
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)


# STEP 4 - Train Machine Learning Model
model = RandomForestClassifier()

model.fit(X_train,y_train)

print("Model Training Completed")


# STEP 5 - Predict Traffic Type
predictions = model.predict(X_test)


# STEP 6 - Check Accuracy
accuracy = accuracy_score(y_test,predictions)

print("Model Accuracy:",accuracy)


# STEP 7 - Count encrypted and unencrypted traffic
encrypted = sum(predictions)
unencrypted = len(predictions) - encrypted


print("Encrypted packets:", encrypted)
print("Unencrypted packets:", unencrypted)


# STEP 8 - Plot graph
labels = ["Encrypted","Unencrypted"]
values = [encrypted,unencrypted]

plt.bar(labels,values)

plt.title("Traffic Detection Result")

plt.xlabel("Traffic Type")

plt.ylabel("Packet Count")

plt.show()