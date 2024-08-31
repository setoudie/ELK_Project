import pandas as pd
import json

# Define the path to the CSV file
csv_file_path = 'EmploisSenegal_IT_jobs.csv'

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Define the path for the JSON output file
json_file_path = 'EmploisSenegal_IT_jobs.json'

# Save the JSON data to the file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f'JSON data has been saved to {json_file_path}')
