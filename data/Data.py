import json
from typing import Dict


class Data:
    PATH = 'data/app_data.json'

    @staticmethod
    def save(data: Dict) -> None:
        with open(Data.PATH, 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)
