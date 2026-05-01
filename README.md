#Team Members
1)Chanchal - GitHub:
2)Arpita Yadav - GitHub:
3) Aditi Chauhan - GitHub: aditichauhancs24-dot

# Encrypted-vs-Unencrypted-Traffic-Detection
Mini cybersecurity project that analyzes encrypted and unencrypted network traffic .






PERSON 1 : CHANCHAL(Responsibility: Capture network packets and prepare dataset.)[Ch1 ,Ch2 and Ch3 png are her work images and also scv packets file.csv]



Step 1:
Tools Used:
Kali Linux
Wireshark
Tcpdump
Python (Scapy)
 Step 2:
Use tcpdump to capture packets.
sudo tcpdump -i eth0 -w traffic.pcap
Step 3:
Capture Different Types of Traffic
Generate both encrypted and unencrypted traffic and Verify in Wireshark
Step 4:
Save captured packets for analysis.
File → Export → CSV




PERSON 2 : ADITI CHAUHAN (Responsibility: Clean the CSV → Add features → Label data → Prepare for ML  )[Ad1, Ad2 , Ad3 png are her work images and also the processed_dataset.csv file and process_csv.py file]



 Step 1:Check CSV File
 Step 2 — Install Required Libraries
Open Command Prompt:
pip install pandas numpy
Step 3 — Create Python Script
Create file:
process_csv.py
Open in:
 Visual Studio Code
 Step 4 — Load CSV File
import pandas as pd

print("Reading CSV file...")

df = pd.read_csv("traffic.csv")

print(df.head())
Step 5 — Clean Data
Step 6 — Add Label
Step 7 — Save Processed Dataset


Overall code:
import pandas as pd

 
print("Reading CSV file...")

df = pd.read_csv("csv packets file.csv")

 
print(df.head())

 
print("Columns in dataset:")
print(df.columns)

 
df = df.dropna()
df = df.drop_duplicates()

 
def label_traffic(row):

    if "443" in str(row["Info"]):
        return 1   # Encrypted traffic (HTTPS)

    else:
        return 0   # Unencrypted traffic


df["Label"] = df.apply(label_traffic, axis=1)

 
df.to_csv("processed_dataset.csv", index=False)

print("Dataset cleaned, labeled and saved successfully!")





 
 PERSON 3 ARPITA YADAV(Responsibility: Build the classifier that detects encrypted traffic.)
 
 
 Tools USED:
Python
Scikit-learn
Matplotlib

Step 1: Load Dataset
Step 2: Split Dataset
Step 3: Train Model
Step 4: Predict Traffic Type
Step 5: Check Accuracy
Step 6: Generate Report


OVERALL CODE:

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt


 
data = pd.read_csv("processed_dataset.csv")

print("Dataset Loaded\n")
print(data.head())
 
X = data[["Length","Protocol"]]
y = data["Label"]

 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

 
model = RandomForestClassifier()

model.fit(X_train, y_train)

print("\nModel Training Completed")

 
predictions = model.predict(X_test)

 
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)


 
encrypted = sum(predictions)
unencrypted = len(predictions) - encrypted

print("\nEncrypted packets:", encrypted)
print("Unencrypted packets:", unencrypted)

 
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:\n", cm)


 
labels = ["Encrypted", "Unencrypted"]
values = [encrypted, unencrypted]

plt.bar(labels, values)

plt.title("Traffic Detection Result")

plt.xlabel("Traffic Type")
plt.ylabel("Packet Count")

plt.show()



Added project report pdf and images

