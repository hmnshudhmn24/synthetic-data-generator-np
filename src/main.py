import numpy as np
import pandas as pd
import yaml
import json
import argparse

def generate_data_from_schema(schema):
    num_rows = schema.get("num_rows", 1000)
    columns = schema["columns"]
    data = {}

    for col in columns:
        name = col["name"]
        dtype = col["type"]

        if dtype == "int":
            data[name] = np.random.randint(col["min"], col["max"] + 1, size=num_rows)
        elif dtype == "float":
            data[name] = np.random.uniform(col["min"], col["max"], size=num_rows).round(2)
        elif dtype == "category":
            data[name] = np.random.choice(col["categories"], size=num_rows)
        elif dtype == "bool":
            data[name] = np.random.choice([True, False], size=num_rows)
        elif dtype == "date":
            start = np.datetime64(col["start"])
            end = np.datetime64(col["end"])
            data[name] = np.random.choice(np.arange(start, end), size=num_rows)
        else:
            raise ValueError(f"Unsupported column type: {dtype}")

    return pd.DataFrame(data)

def main(schema_file, output_file):
    with open(schema_file, 'r') as f:
        if schema_file.endswith(".json"):
            schema = json.load(f)
        elif schema_file.endswith(".yaml") or schema_file.endswith(".yml"):
            schema = yaml.safe_load(f)
        else:
            raise ValueError("Schema file must be .json or .yaml")

    df = generate_data_from_schema(schema)
    df.to_csv(output_file, index=False)
    print(f"✅ Data generated and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synthetic Data Generator using NumPy")
    parser.add_argument("--schema", type=str, required=True, help="Path to schema file (.json or .yaml)")
    parser.add_argument("--output", type=str, default="synthetic_data.csv", help="Output CSV file name")
    args = parser.parse_args()
    main(args.schema, args.output)