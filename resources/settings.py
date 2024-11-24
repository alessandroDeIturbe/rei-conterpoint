import json
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# * env
settings_file = Path("resources/settings.json")

if os.path.exists(settings_file):
    with open(settings_file, "r") as f:
        settings = json.load(f)
else:
    root = tk.Tk()
    root.withdraw()
    settings = {
        "os_path": filedialog.askopenfilename(),
        "": None,
    }

    with open(settings_file, "w") as f:
        json.dump(settings, f)