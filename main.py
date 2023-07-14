import json
import logging
from datetime import datetime

import requests

logging.basicConfig(level=logging.INFO)


def requests_url(url: str, output: str) -> None:
    URL: str = url
    response = requests.get(url=URL).json()
    logging.info(response)

    with open(output, 'w') as file:
        file.write(json.dumps(response))


if __name__ == "__main__":
    print("Git rules!")
    requests_url(
        "https://dummyjson.com/products",
        f"dummy_json_{datetime.now():%Y-%m-%d_%H_%M}.json"
    )
