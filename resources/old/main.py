import json
import os
import shutil
import resources.settings
from music21 import *
import tkinter as tk
from tkinter import filedialog

# * Environment Settings
env = environment.UserSettings()
user_musicxmlPath = env["musicxmlPath"]

print(f"Old musicxml path: {env['musicxmlPath']}")

root = tk.Tk()
root.withdraw()
env["musicxmlPath"] = filedialog.askopenfilename()
print(env["musicxmlPath"])

print(f"New musicxml path: {env['musicxmlPath']}")
# musescore_version = int(input("Set Musescore version (3/4): "))

cantus_firmus = stream.Part()
altus = stream.Part()

filepath = "cantus_firmus.mxl"
default = shutil.which("default_firmus.mxl")
print(default)

if not os.path.exists(filepath):
    score = converter.parse(default)
    
else:
    file = converter.parse(filepath)
    print(file)
    for element in file.recurse().notes:
        print(element)

if os.name != "posix":
    print(system.on_windows())
else:
    print(system.on_unix())

# ! Handle error