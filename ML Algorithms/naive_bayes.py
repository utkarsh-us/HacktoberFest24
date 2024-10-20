import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import joblib

# Load dataset
data = pd.read_csv('mobiledata.csv')  # Make sure 'mobiledata.csv' is in the current working directory

# Display the first few rows to ensure the dataset loaded correctly
print("First few rows of the dataset:")
print(data.head())

# Feature selection and target variable
features = data[['Feature1', 'Feature2', 'Feature3', 'Feature4']]  # Adjust features based on your dataset
target = data['Target']  # Update with the actual target column name

# Handle missing values if needed
if data.isnull().values.any():
    print("Warning: There are missing values in the dataset. Filling missing values with the mean.")
    features = features.fillna(features.mean())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the Naive Bayes model
nb = GaussianNB()

# Train the model
nb.fit(X_train, y_train)

# Make predictions
y_pred = nb.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Naive Bayes Accuracy: {accuracy:.2f}')

# Save the model for future use
joblib.dump(nb, 'naive_bayes_model.pkl')
print("Model saved as 'naive_bayes_model.pkl'.")