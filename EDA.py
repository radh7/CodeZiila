import sweetviz as sv
import pandas as pd

file_path = './Consultrix Data Set.csv' 
data = pd.read_csv(file_path)  # Use read_csv for CSV files

if 'TotalCharges' in data.columns:
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

report = sv.analyze(data)
report.show_html('Consultrix_EDA_Report.html')

print("EDA report generated successfully: MLZilla_EDA_Report.html")
