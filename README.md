#Team Members
1)Chanchal - GitHub:
2)Arpita Yadav - GitHub:
3) Aditi Chauhan - GitHub: aditichauhancs24-dot

# Encrypted-vs-Unencrypted-Traffic-Detection
Mini cybersecurity project that analyzes encrypted and unencrypted network traffic .






PERSON 1 : CHANCHAL(Responsibility: Capture network packets and prepare dataset.)
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




PERSON 2 : ADITI CHAUHAN (Responsibility: Clean the CSV → Add features → Label data → Prepare for ML  )
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

# Step 1: Read CSV file
print("Reading CSV file...")

df = pd.read_csv("csv packets file.csv")

# Step 2: Show first rows
print(df.head())

# Step 3: Show column names
print("Columns in dataset:")
print(df.columns)

# Step 4: Clean data
df = df.dropna()
df = df.drop_duplicates()

# Step 5: Label traffic
def label_traffic(row):

    if "443" in str(row["Info"]):
        return 1   # Encrypted traffic (HTTPS)

    else:
        return 0   # Unencrypted traffic


df["Label"] = df.apply(label_traffic, axis=1)

# Step 6: Save new dataset
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
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load dataset
print("Loading dataset...")
data = pd.read_csv("processed_dataset.csv")

print("\nDataset Preview:")
print(data.head())

# Step 2: Select features and label
# (Change column names if different)
X = data[["PacketLength", "Protocol", "SourcePort", "DestinationPort"]]
y = data["Label"]

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 4: Train model
print("\nTraining model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Predictions
predictions = model.predict(X_test)

# Step 6: Accuracy
accuracy = accuracy_score(y_test, predictions)
print("\nModel Accuracy:", accuracy)

# Step 7: Detailed Report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Step 8: Count encrypted vs unencrypted
encrypted = sum(predictions)
unencrypted = len(predictions) - encrypted

print("\nResults:")
print("Encrypted Traffic:", encrypted)
print("Unencrypted Traffic:", unencrypted)

# Step 9: Graph
labels = ["Encrypted", "Unencrypted"]
values = [encrypted, unencrypted]

plt.bar(labels, values)
plt.title("Traffic Classification Result")
plt.xlabel("Traffic Type")
plt.ylabel("Count")
plt.show()

# Step 10: Save model
with open("traffic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved as traffic_model.pkl")

