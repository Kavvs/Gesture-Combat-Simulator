import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("data/gesture_data.csv")
X = data.drop(columns=["label" if "label" in data.columns else data.columns[0]])
y = data[data.columns[0]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
print("✅ Model accuracy:", clf.score(X_test, y_test))

joblib.dump(clf, "gestures/model.pkl")
print("✅ Model saved to gestures/model.pkl")
