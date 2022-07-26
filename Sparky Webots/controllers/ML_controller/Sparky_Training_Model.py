from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib

scaler = StandardScaler()
model = DecisionTreeClassifier()

df = pd.read_csv("sensors_data.csv")
x = df[["Left_Sensor", "Front_Sensor", "Right_Sensor"]].values
y = df["Result"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Score:", round(model.score(x_train, y_train) * 100, 2), "%")

# Accuracy: 99.56 % -> We export the model
joblib.dump(model, "trained_model.pkl")
