import sweetviz as sv
import pandas as pd

# Load the dataset
file_path = './Consultrix Data Set.csv'
data = pd.read_csv(file_path)

# Convert 'TotalCharges' to numeric, forcing errors to NaN
if 'TotalCharges' in data.columns:
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

# Generate the Sweetviz report
report = sv.analyze(data)

# Save the report as an HTML file
report.show_html('index.html')

# Confirmation message
print("EDA report generated successfully: index.html")
