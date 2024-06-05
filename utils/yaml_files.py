import glob
import os
from os import listdir
from os.path import isfile, join
from ..utils.tools import get_addon_absolute_path
from ..utils.config import data as config

class YAMLCache:
    master_files = []
    yaml_files = []
    last_count = 0
    
    @staticmethod
    def check_for_changes(folder: str) -> bool:
        absolute_path = os.path.join(get_addon_absolute_path(), folder)
        yamlcounter = len(glob.glob1(absolute_path,"*.yaml"))
        if YAMLCache.last_count != yamlcounter:
            YAMLCache.last_count = yamlcounter
            return True
        return False


def get_editable_files():
    if YAMLCache.check_for_changes(config["yaml_files_folder"]) is False:
        return YAMLCache.yaml_files;

    files = get_files(config["yaml_files_folder"])
    YAMLCache.yaml_files = format_files(files)
    print("YAML Cached updated: ", files)
    return YAMLCache.yaml_files

def get_master_files():
    if YAMLCache.master_files: return YAMLCache.master_files
    
    files = get_files(config["rig_master_files"])
    YAMLCache.master_files = format_files(files)

    return YAMLCache.master_files

def format_files(files: list) -> list:
    formatted = []
    for f in files:
        full_filename = f.name  # Filename including extension
        filename_without_extension = os.path.splitext(f.name)[0]
        description = " ".join(("Select", f.name))  # Using filename with extension as description

        formatted.append((full_filename, filename_without_extension, description))
    return formatted

def get_files(folder: str) -> list:
    absolute_path = os.path.join(get_addon_absolute_path(), folder)
    files = []
    with os.scandir(absolute_path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".yaml"):
                files.append(entry);
    return files