import json
from typing import Dict

DATA_PATH = 'data/app_data.json'


class Data:

    @staticmethod
    def save(data: Dict) -> None:
        with open(DATA_PATH, 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)
