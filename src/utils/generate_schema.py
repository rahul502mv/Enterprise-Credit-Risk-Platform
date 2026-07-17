import pandas as pd

df = pd.read_csv(
    "data/processed/application_train_recommendation.csv"
)

drop_columns = [
    "SK_ID_CURR",
    "TARGET"
]

X = df.drop(columns=drop_columns)

X = X.select_dtypes(include="number")

print("Total Features:", len(X.columns))

for col in X.columns:
    print(col)