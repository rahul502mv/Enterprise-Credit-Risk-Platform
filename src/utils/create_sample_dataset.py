import pandas as pd

# Read the processed dataset
df = pd.read_csv(
    "data/processed/application_train_anomaly.csv"
)

# Create a random sample
sample = df.sample(
    n=5000,
    random_state=42
)

# Save the sample
sample.to_csv(
    "data/processed/application_train_sample.csv",
    index=False
)

print("Sample Dataset Created Successfully!")
print(sample.shape)