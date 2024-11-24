from music21 import *
import os
import shutil
import tkinter as tk
from tkinter import filedialog

# * Environment Settings
env = environment.UserSettings()
# print(env['musicxmlPath'])
env['musicxmlPath'] = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"
print(env['musicxmlPath'])
musescore_version = int(input("Set Musescore version (3/4): "))

cantus_firmus = stream.Part()
altus = stream.Part()

filepath = "cantus_firmus.mxl"
default = "default_firmus.mxl"

if not os.path.exists(filepath):
    score = converter.parse(default)
    
else:
    file = converter.parse(filepath)
    print(file)
    for element in file.recurse().notes:
        print(element)


if os.name != "posix":
    pass
else:
    musescore_path = shutil.which(f"Musescore {musescore_version}")
    if musescore_path == None:
        root = tk.Tk()
        root.withdraw()
        try:
            musescore_path = filedialog.askopenfile()
            print(musescore_path)
        except IsADirectoryError:
# ! Handle error