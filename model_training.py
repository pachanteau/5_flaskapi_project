import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("src/winequality.csv")

y = df["quality"]
X = df.drop(["quality", "type"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Pipeline(steps=[("imputer", SimpleImputer(strategy="mean")),
                        ("scaler", StandardScaler()),
                        ("classifier", RandomForestClassifier())])

model.fit(X_train, y_train)

print("Accuracy: {:.2f}".format(model.score(X_test, y_test)))

joblib.dump(model, "model/model.joblib")
