import os
from time import sleep
from datetime import datetime


class Application:

    def __init__(self) -> None:
        self.data_folder: str = "./data/"
        self.config: str = "./config.json"

        if not os.path.exists(self.data_folder):
            os.mkdir(self.data_folder)

        if not os.path.exists(self.config):
            with open(self.config, "w") as config_file:
                ...

class Output(Application):

    def __init__(self, regs: int) -> None:
        super().__init__()
        self.regs = regs
        self.output_folder: str = f"{self.data_folder}/output/"
        
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)
        
    def write_json(self, func):
        for _ in range(self.regs):
            func("https://dummyjson.com/products",
                 f"{self.output_folder}/dummy_json_{datetime.now():%Y-%m-%d_%H_%M_%S}.json")
            sleep(2)
