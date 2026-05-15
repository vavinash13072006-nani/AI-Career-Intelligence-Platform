import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = {
    "python":[1,1,0,0],
    "sql":[1,0,1,0],
    "ml":[1,0,0,1],
    "web":[0,1,1,0],
    "career":[
        "AI Engineer",
        "Web Developer",
        "Database Administrator",
        "Data Scientist"
    ]
}

df = pd.DataFrame(data)

X = df[["python","sql","ml","web"]]
y = df["career"]

model = DecisionTreeClassifier()

model.fit(X,y)

pickle.dump(model, open("career_model.pkl","wb"))

print("Career Model Trained")