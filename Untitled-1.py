# Importing necessary libraries
import pandas as pd  # For data manipulation
import statsmodels.api as sm  # For statistical modeling

# Step 1: Define the file path
file_path = r'C:\Users\MhaskarN04\Downloads\Restaurant Revenue.xlsx'

# Step 2: Read the Excel spreadsheet
try:
    # Read the Excel file into a DataFrame
    restaurant_data = pd.read_excel(file_path)
    
    # Step 3: Select relevant columns for analysis
    selected_columns = ['Number_of_Customers', 'Menu_Price', 'Marketing_Spend',
                        'Average_Customer_Spending', 'Promotions', 'Reviews', 'Monthly_Revenue']
    data_for_analysis = restaurant_data[selected_columns]
    
    # Step 4: Define independent and dependent variables
    X = data_for_analysis.drop('Monthly_Revenue', axis=1)  # Independent variables
    y = data_for_analysis['Monthly_Revenue']  # Dependent variable
    
    # Step 5: Add constant for the intercept term
    X_with_const = sm.add_constant(X)  # Add a constant term to the independent variables
    
    # Step 6: Fit the multiple regression model
    model = sm.OLS(y, X_with_const).fit()  # Fit the multiple regression model using Ordinary Least Squares
    
    # Step 7: Print the regression model summary
    print(model.summary())  # Print the summary of the regression model
    
except FileNotFoundError:
    print("File not found at the specified path. Please check the file path and try again.")

#Predict the monthly revenue!
