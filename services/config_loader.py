import json
import yaml
from configparser import ConfigParser
from pathlib import Path


class ConfigLoader:
    @staticmethod
    def load(file_path):
        """Load configuration from JSON, YAML, or .properties file."""
        config_path = Path(file_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {file_path}")

        if config_path.suffix == ".json":
            with open(file_path, "r") as file:
                return json.load(file)
        elif config_path.suffix in {".yml", ".yaml"}:
            with open(file_path, "r") as file:
                return yaml.safe_load(file)
        elif config_path.suffix == ".properties":
            parser = ConfigParser()
            parser.read(file_path)
            return {key: value for section in parser.sections() for key, value in parser.items(section)}
        else:
            raise ValueError("Unsupported config file format. Use JSON, YAML, or .properties.")
