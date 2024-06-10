import json

# Load the JSON data from the file
with open('mudata.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Calculate the total number of question-answer pairs
total_pairs = len(data)

print("Total number of question-answer pairs:", total_pairs)
