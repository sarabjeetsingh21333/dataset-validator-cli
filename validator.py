import json
import os
import sys
import pandas as pd

def validate_jsonl(file_path, required_keys):
    """
    Validates a JSONL file for schema compliance, missing keys, and duplicates.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    print(f"Analyzing '{file_path}'...\n")
    
    valid_rows = []
    errors = []
    seen_entries = set()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue # Skip empty lines
            
            try:
                data = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append({"line": line_num, "error": f"JSON Decode Error: {e}"})
                continue
                
            # Check for missing required keys
            missing_keys = [key for key in required_keys if key not in data]
            if missing_keys:
                errors.append({"line": line_num, "error": f"Missing required keys: {missing_keys}"})
                continue
                
            # Check for exact duplicates based on prompt/input values
            row_signature = json.dumps(data, sort_keys=True)
            if row_signature in seen_entries:
                errors.append({"line": line_num, "error": "Duplicate entry detected"})
                continue
                
            seen_entries.add(row_signature)
            valid_rows.append(data)

    # Output Summary Report
    print("=== Validation Summary ===")
    print(f"Total Valid Records: {len(valid_rows)}")
    print(f"Total Errors/Anomalies Found: {len(errors)}")
    
    if errors:
        print("\n--- Error Log ---")
        for err in errors[:10]: # Show first 10 errors
            print(f"Line {err['line']}: {err['error']}")
            
    # Save cleaned output
    if valid_rows:
        df = pd.DataFrame(valid_rows)
        output_file = "cleaned_dataset.jsonl"
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for item in valid_rows:
                out_f.write(json.dumps(item) + '\n')
        print(f"\nSuccess! Cleaned dataset saved to '{output_file}' using Pandas & JSON parsing.")

if __name__ == "__main__":
    # Example configuration: looking for 'prompt' and 'response' keys typical in RLHF pipelines
    REQUIRED = ["prompt", "response"]
    
    # Target file passed via command line or default test file
    target_file = sys.argv[1] if len(sys.argv) > 1 else "sample_data.jsonl"
    validate_jsonl(target_file, REQUIRED)