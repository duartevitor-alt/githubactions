import json
import logging
import requests


def requests_url(url: str, 
                 output: str, 
                 write_output: bool = True) -> None:
    URL: str = url
    response = requests.get(url=URL).json()
    logging.info(response)

    if write_output:
        with open(output, 'w') as file:
            file.write(json.dumps(response))
