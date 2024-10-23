from music21 import *
import os

# * Environment Settings
env = environment.UserSettings()
# print(env['musicxmlPath'])
env['musicxmlPath'] = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"
print(env['musicxmlPath'])

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