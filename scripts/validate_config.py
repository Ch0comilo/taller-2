import yaml
import sys
try:
    with open('config/pipeline_config.yaml') as f:
        yaml.safe_load(f)
    print("Config OK")
except Exception as e:
    print("Config invalida:", e)
    sys.exit(1)