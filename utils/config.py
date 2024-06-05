## Ensure YAML is installed
import sys
import subprocess
import os
try:
    import yaml  # type: ignore
except:
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    # upgrade pip
    subprocess.call([python_exe, "-m", "ensurepip"])
    subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
    # install required packages
    subprocess.call([python_exe, "-m", "pip", "install", "pyyaml"])

## ./Ensure YAML
import io, yaml # type: ignore
from .tools import get_addon_absolute_path

path_to_config = os.path.join(get_addon_absolute_path(), "config.yaml")
with io.open(path_to_config) as stream:
    data = yaml.safe_load(stream)
print("Config File:" + str(data))

data["version"] = tuple(data["version"])
data["blender"] = tuple(data["blender"])
data["variants"] = [tuple(k) for k in data["variants"]]