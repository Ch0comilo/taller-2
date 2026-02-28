import os
import csv

class DataProcessor:
    def __init__(self, config):
        self.config = config

    def process(self):
        output = []
        count = 0
        path = 'data/raw'
        for fname in self.config.get('required_files', []):
            fp = os.path.join(path, fname)
            if os.path.exists(fp):
                with open(fp, newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        output.append(row)
                        count += 1
        os.makedirs(self.config.get('output_path', 'data/processed/'), exist_ok=True)
        return {'processed_data': output, 'record_count': count}