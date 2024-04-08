import pandas as pd  # Importing pandas library for data manipulation

# Load the Excel file into a pandas DataFrame
# Replace 'C:\\Users\\MhaskarN04\\Downloads\\baseball.xlsx' with the correct path to your file
baseball_data = pd.read_excel('C:\\Users\\MhaskarN04\\Downloads\\baseball.xlsx')

# Selecting the relevant columns for prediction
# Columns D, E, F, G, H, and I correspond to indices 3, 4, 5, 6, 7, and 8 (0-indexed)
# We're selecting 'Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', and 'Team Batting Average'
selected_columns = baseball_data.iloc[:, [3, 4, 5, 6, 7, 8]]

# Define features (X) and target variable (y)
X = selected_columns[['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']]
y = baseball_data['Playoffs']  # Target variable

# Splitting the data into training and testing sets
from sklearn.model_selection import train_test_split

# Split data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Importing the Logistic Regression model
from sklearn.linear_model import LogisticRegression

# Creating the Logistic Regression model
model = LogisticRegression()

# Training the model on the training data
model.fit(X_train, y_train)

# Making predictions on the testing data
predictions = model.predict(X_test)

# Evaluating the model
from sklearn.metrics import classification_report, confusion_matrix

# Printing the confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Printing the classification report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Printing the coefficients of the model
print("\nModel Coefficients:")
for feature, coef in zip(X.columns, model.coef_[0]):
    print(f"{feature}: {coef}")

    # Go Yankees!

