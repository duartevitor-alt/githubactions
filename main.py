import json
import logging
from datetime import datetime
import projectfolder as pj

import requests

logging.basicConfig(level=logging.INFO)


def requests_url(url: str, output: str) -> None:
    URL: str = url
    response = requests.get(url=URL).json()
    logging.info(response)

    with open(output, 'w') as file:
        file.write(json.dumps(response))


if __name__ == "__main__":
    logging.info("Getting start!")
    logging.info("Application class instantiated!")

    app: pj.Application = pj.Application()
    output: pj.Output = pj.Output(3)

    output.write_json(requests_url)
    