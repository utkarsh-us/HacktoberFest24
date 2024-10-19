import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv('mobiledata.csv')

# Select features and target variable
features = data[['age_group', 'gender', 'employment_status', 'budget']]
target = data['purchases_mobile']

# Encode categorical data
features = pd.get_dummies(features)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Random Forest Accuracy: {accuracy:.2f}')

# Save the model for later use
joblib.dump(clf, 'random_forest_model.pkl')
