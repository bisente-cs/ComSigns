import pickle
import cv2
import mediapipe as mp
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.calibration import CalibratedClassifierCV

# Load the preprocessed data
data_dict = pickle.load(open("./data.pickle", "rb"))

# Ensure all sublists have the same length by padding with zeros
max_length = max(len(sublist) for sublist in data_dict["data"])
data_padded = [
    sublist + [0] * (max_length - len(sublist)) for sublist in data_dict["data"]
]

# Convert the data to numpy arrays
data = np.asarray(data_padded)
labels = np.asarray(data_dict["labels"])

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42
)

# Initialize and train the RandomForestClassifier
base_model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)

# Fit the model on the training set
base_model.fit(x_train, y_train)

# Calibrate the classifier using Platt's scaling or Isotonic regression (default is Platt's scaling)
calibrated_model = CalibratedClassifierCV(base_model, method='sigmoid', cv='prefit')
calibrated_model.fit(x_train, y_train)

# Evaluate using cross-validation
cv_scores = cross_val_score(calibrated_model, data, labels, cv=5, scoring="accuracy")
print("Cross-Validation Scores:", cv_scores)
print("Mean Accuracy:", np.mean(cv_scores))

# Make predictions on the test set
y_predict = calibrated_model.predict(x_test)

# Evaluate the performance of the model
score = accuracy_score(y_test, y_predict)
print(f"Accuracy: {score * 100:.2f}% of samples were classified correctly!")

# Display classification report
print("Classification Report:\n", classification_report(y_test, y_predict))

# Save the trained model to a file
with open("calibrated_model.p", "wb") as f:
    pickle.dump({"model": calibrated_model}, f)
