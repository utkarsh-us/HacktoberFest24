#Decision Tree algorithm for by using dataset of mobile retail shop to predict if the user buys the mobile or not

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import warnings

warnings.filterwarnings("ignore")
mobile_data = pd.read_csv("mobiledata.csv")

#to select features or attributes by neglecting purchases_mobile feature
features = mobile_data.columns.drop("purchases_mobile")

# the target that the model need to predict
target = ["purchases_mobile"]

mobile_data_encoded = pd.get_dummies(mobile_data[features])
print(f"mobile data encoded is: {mobile_data_encoded}")
mobile_data_encoded["purchases_mobile"] = mobile_data["purchases_mobile"]

from sklearn.model_selection import train_test_split
mobile_train,mobile_test = train_test_split(mobile_data_encoded,test_size=0.15,random_state=100)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
target = ["purchases_mobile"]
features = mobile_train.columns.drop("purchases_mobile")
model.fit(mobile_train[features],mobile_train[target])

from sklearn.tree import plot_tree
plt.figure(figsize=(20,10))
plot_tree(model,
          feature_names=features,
          class_names = [str(c) for c in model.classes_],
          filled=True,
          rounded=True,
          fontsize=10)
plt.show()
