# JSON/JSONL Schema Validator & Dataset Cleaner

A lightweight Python command-line utility designed to automate schema compliance checks, error detection, duplicate filtering, and data cleaning for raw text and JSONL datasets—commonly used in LLM training, RLHF pipelines, and multimodal data operations[cite: 2].

## Features
- **Schema Compliance:** Validates incoming records against mandatory keys (e.g., `prompt`, `response`).
- **Anomaly Detection:** Flags JSON decoding errors, structural formatting issues, and missing fields.
- **Duplicate Filtering:** Identifies and strips redundant entries to ensure dataset uniqueness.
- **Automated Reporting:** Summarizes error logs and outputs production-ready cleaned JSONL files using `pandas`.

## Tech Stack
- **Python** (Core, File I/O, JSON parsing)[cite: 2]
- **Pandas & NumPy** (Tabular data handling and transformation)[cite: 2]

## Quick Start
1. Clone the repository:
   ```bash
   git clone [https://github.com/sarabjeetsingh21333/dataset-validator-cli.git](https://github.com/sarabjeetsingh21333/dataset-validator-cli.git)
   cd dataset-validator-cli