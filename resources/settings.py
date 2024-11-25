import json
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

title = "SETTINGS: "
settings_file = Path("resources/settings.json")
default_firmus = str(Path("resources/default_firmus.mxl"))

def import_user_settings(settings_file=settings_file):
    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            settings = json.load(f)
            print(f"{title}settings.json founded in: {settings_file}")
            return settings
    else:
        root = tk.Tk()
        root.withdraw()
        settings = {
            "msx_path": filedialog.askopenfilename(),
            "defaut_firmus": default_firmus,
        }

        with open(settings_file, "w") as f:
            json.dump(settings, f)

        print(f"{title}settings.json founded in: {settings_file}")
        return settings