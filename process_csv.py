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
        return 1  

    else:
        return 0   
df["Label"] = df.apply(label_traffic, axis=1)
df.to_csv("processed_dataset.csv", index=False)

print("Dataset cleaned, labeled and saved successfully!")