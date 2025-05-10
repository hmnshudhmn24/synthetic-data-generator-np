# 🧪 Large-Scale Synthetic Data Generator (NumPy + YAML/JSON)

This project uses NumPy to efficiently generate large synthetic datasets based on a user-defined schema in **YAML** or **JSON** format.

## 🎯 Features

- Supports int, float, category, bool, and date columns
- Define column properties and ranges via schema
- Generate millions of rows efficiently
- Export to CSV with one command

## 🧰 Supported Types

- `int`: min, max
- `float`: min, max
- `category`: list of categories
- `bool`: true/false
- `date`: start, end (YYYY-MM-DD)

## 📝 Schema Example (YAML)

```yaml
num_rows: 1000
columns:
  - name: age
    type: int
    min: 20
    max: 60
  - name: salary
    type: float
    min: 40000
    max: 100000
  - name: role
    type: category
    categories: ["Manager", "Developer", "Analyst"]
  - name: active
    type: bool
  - name: joined
    type: date
    start: "2010-01-01"
    end: "2023-01-01"
```

## 🚀 How to Run

```bash
pip install numpy pandas pyyaml
python src/main.py --schema schema.yaml --output data.csv
```

## 📂 Project Structure

```
synthetic_data_generator_np/
├── src/
│   └── main.py          # Generator script
├── schema.yaml          # Sample schema file
├── README.md            # Project documentation
```

---

📦 Use this tool to simulate realistic ML-ready datasets instantly!