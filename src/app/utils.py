import json
import datetime
import sys
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.main import App

class Utils():
    def __init__(self, app: "App"):
        self.app = app
        self.home_directory = os.path.expanduser("~")
        self.config = None
        self.log_directory = None
        self.load_config()
        if self.config is None:
            sys.exit(1)
        self.init()


    def load_config(self):
        with open("config.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        self.config = data


    def init(self) -> None | str:
        if self.config is None:
            sys.exit(1)
        core_directory = os.path.join(self.home_directory, self.config["core_directory"])
        log_directory = os.path.join(core_directory, self.config["log_directory"]) 
        os.makedirs(core_directory, exist_ok=True)
        os.makedirs(log_directory, exist_ok=True)
        self.log_directory = log_directory
        print(self.log_directory)


    def write_to_log_file(self, input_str: str):
        if self.log_directory is None or self.config is None:
            sys.exit(1)
        now = datetime.datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        file_name = f"{self.config['filename_prefix']}_{date_str}"
        path = os.path.join(self.log_directory, file_name)
        timestamp = now.strftime(self.config["timestamp_format"])[:-3].replace(".", ":")
        write_str = f"{timestamp} {input_str}\n"
        with open(path, "a") as file:
            file.write(write_str)
