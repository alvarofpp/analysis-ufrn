import json
from typing import Dict


class AppData:

    @staticmethod
    def save(data: Dict) -> None:
        with open('app_data.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)

    @staticmethod
    def get_data_by_key(key: str) -> Dict:
        return json.load(open('app_data.json'))[key]
