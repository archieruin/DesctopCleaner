import os
import sys
from pathlib import Path
from time import sleep
import shutil

RELOAD_DELAY = 5
DESKTOP_PATH = Path.home() / "Desktop"

SAVE_PATH = Path("D:\\FromDesktop")
FOLDERS_PATH = SAVE_PATH / "Folders"
IMAGES_PATH = SAVE_PATH / "Images"
MUSIC_PATH = SAVE_PATH / "Music"
VIDEOS_PATH = SAVE_PATH / "Videos"
ARCHIVES_PATH = SAVE_PATH / "Archives"
OTHERS_PATH = SAVE_PATH / "Others"
ALL_PATHS = [
    SAVE_PATH,
    FOLDERS_PATH,
    IMAGES_PATH,
    MUSIC_PATH,
    VIDEOS_PATH,
    ARCHIVES_PATH,
    OTHERS_PATH,
]

images_extensions = ("jpg", "png", "psd", ".gif")
videos_extensions = ("mp4", "")
archives_extensions = ("rar", "7z", "zip")


def check_folders():
    print("Folders checking...")
    for path in ALL_PATHS:
        if not path.exists():
            path.mkdir()
    print("Folders checking has been done.")


def move(item, dst):
    try:
        shutil.move(item.path, dst)
    except shutil.Error:
        try:
            os.remove(f"{dst}\\{item.name}")
        except PermissionError:
            print(f" !!! Can not delete: {dst}")

def main():
    while True:
        print("RELOADING...")
        moved_items_count = 0
        desctop_items = [item for item in os.scandir(DESKTOP_PATH)]

        for item in desctop_items:
            print(item.name)
            if item.is_dir():
                move(item, FOLDERS_PATH)

            elif item.name.endswith(images_extensions):
                move(item, IMAGES_PATH)

            elif item.name.endswith(images_extensions):
                move(item, MUSIC_PATH)

            elif item.name.endswith(images_extensions):
                move(item, VIDEOS_PATH)

            elif item.name.endswith(images_extensions):
                move(item, ARCHIVES_PATH)
            else:
                move(item, OTHERS_PATH)
            moved_items_count += 1

        print(f"INFO: {moved_items_count} items are successful moved!")
        print(f"Sleep {RELOAD_DELAY} sec.")
        sleep(RELOAD_DELAY)


if __name__ == "__main__":
    print("Application is started.")
    try:
        check_folders()
        main()
    except KeyboardInterrupt:
        print("Application is closed.")
