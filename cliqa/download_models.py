import shutil
from os import path
from nunif.utils.downloader import ArchiveDownloader
from nunif.logger import logger


VERSION = "20240212"
MODEL_DIR = path.join(path.dirname(__file__), "pretrained_models")
VERSION_FILE = path.join(MODEL_DIR, VERSION)
MODEL_URL = f"https://github.com/nagadomi/nunif/releases/download/0.0.0/cliqa_pretrained_models_{VERSION}.zip"


class ModelDownloader(ArchiveDownloader):
    def handle(self, src):
        src = path.join(src, "pretrained_models")
        dst = MODEL_DIR
        logger.debug(f"Downloder: {self.name}: copytree: {src} -> {dst}")
        shutil.copytree(src, dst, dirs_exist_ok=True)
        with open(VERSION_FILE, mode="w") as f:
            f.write(VERSION)


def main():
    if not path.exists(VERSION_FILE):
        downloder = ModelDownloader(MODEL_URL, name="CLIQA Models", format="zip")
        downloder.run()


if __name__ == "__main__":
    main()
