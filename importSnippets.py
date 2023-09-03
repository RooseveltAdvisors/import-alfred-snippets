import csv
import json
import os
import binascii
import glob

# List all CSV files in the current directory
csv_files = glob.glob("*.csv")

fieldNames = ['name', 'keyword', 'content']

for sourceFile in csv_files:
    # Create a directory named after the sourceFile without the .csv extension
    folder_name = os.path.splitext(sourceFile)[0]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(sourceFile, 'rt', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldNames)
        for row in reader:
            # Convert bytes to string using 'decode' in Python 3
            uid = binascii.b2a_hex(os.urandom(15)).decode('utf-8')
            output = json.dumps(
                {
                    "alfredsnippet": {
                        "snippet": row['content'],
                        "uid": uid,
                        "name": row['name'],
                        "keyword": row['keyword']
                    }
                },
                sort_keys=False,
                indent=4,
                separators=(',', ': ')
            )
            
            # Save the .json file in the folder created
            outputFile = os.path.join(folder_name, f"{row['name']} [{uid}].json")
            with open(outputFile, 'w') as f:
                f.write(output)
