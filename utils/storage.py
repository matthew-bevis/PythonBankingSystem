import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_data(file_path, new_record):
    data = load_data(file_path)
    data.append(new_record)
    save_data(file_path, data)

def update_record(file_path, record_id, updated_record, key="customer_id"):
    data = load_data(file_path)
    for i, record in enumerate(data):
        if record.get(key) == record_id:
            data[i] = updated_record
            break
    else:
        data.append(updated_record)  # If not found, append new
    save_data(file_path, data)

def delete_record(file_path, record_id, key="customer_id"):
    data = load_data(file_path)
    data = [record for record in data if record.get(key) != record_id]
    save_data(file_path, data)
