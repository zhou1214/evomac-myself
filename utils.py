import yaml

def load_config(config_path):
    with open(config_path, 'r',encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

def handle_retry_error(retry_state):
    print(f"Retry failed")