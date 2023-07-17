import logging
from utils import requests_url
import projectfolder as pj


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    logging.info("Getting start!")
    logging.info("Application class instantiated!")

    app: pj.Application = pj.Application()
    output: pj.Output = pj.Output(3)

    output.write_json(requests_url)
    