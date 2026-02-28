import os

class DataValidator:
    def __init__(self, config):
        self.config = config

    def validate(self):
        required = self.config.get('required_files', [])
        missing = []
        for f in required:
            if not os.path.exists(os.path.join('data/raw', f)):
                missing.append(f)
        if missing:
            return {'success': False, 'errors': missing}
        return {'success': True}