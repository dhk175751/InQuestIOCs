import pandas as pd
import json
import requests
import csv


headers = {
  'Accept': 'application/json'
}

r = requests.get('https://labs.inquest.net/api/iocdb/list', headers = headers)


r = r.json()



# Data to be written
dictionary = r


# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)



# Read JSON
with open('sample.json') as inputfile:
  data = json.load(inputfile)

# Extract values
values_list = data.get('data', [])

# Normalize nested values
df = pd.json_normalize(values_list)

#print(df)

# Extract desired fields
selected_columns = [
    'artifact', 
    'artifact_type', 
    'created_date',
    'reference_text',
    'reference_link', 
]
df_selected = df[selected_columns]

# Write DF to CSV
#df_new = df[df['artifact_type'] == 'domain']  --- https://www.geeksforgeeks.org/how-to-select-rows-from-a-dataframe-based-on-column-values/
df.to_csv('IOCs.csv', index=False)
print("Values have been added. Please check the output.csv file.")


#after first file is created.
#df.to_csv('IOCs.csv', mode='a', index=False, header=False) ----#https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/ 
