import json
import random
from pathlib import Path

# Read the healthcare FAQ dataset
input_file = Path("data/healthcare_faq_day2.json")

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Shuffle the records
random.seed(42)
random.shuffle(data)

# Split the dataset
train = data[:14]
validation = data[14:17]
test = data[17:20]

# Save each dataset
datasets = {
    "train.json": train,
    "validation.json": validation,
    "test.json": test
}

for filename, records in datasets.items():
    output_file = Path("data") / filename

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)

    print(f"{filename}: {len(records)} records saved")

print("Dataset splitting completed!")