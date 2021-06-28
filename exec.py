# load text
from clint.textui import *
import os.path
import sys
import os

def Isfile(file):
    if os.path.isfile(file):
        return 1
    else:
        return -1
def Load(path):
    if Isfile(path) == -1:
        return 0
    file = open(path, 'rb')
    load = file.read()
    text = load.decode(encoding="utf-8")
    if text.find(' ')!=0:
        return text
    else:
        return -1
def NowDir():
    return os.path.dirname(os.path.abspath(__file__))
def ManVer():
    now = NowDir()
    ver_file = now + "/doc/version.md"
    isfile = Isfile(ver_file)
    if isfile == -1:
        print("Error: No version.md file")
        return -1
    file = open(ver_file, "rb")
    load = file.read()
    file.close()
    print(colored.green(load.decode(encoding="utf-8")[:2]) + ' ' + load.decode(encoding="utf-8")[3:]) # Prints
def ManHelp():
    ManVer()
    now = NowDir()
    help_file = now + "/doc/help.md"
    isfile = Isfile(help_file)
    if isfile == -1:
        print("Error: No help.md file")
        return -1
    file = open(help_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
def Flags(text):
    if (text.find("-h")==0 or text.find("--h")==0):
        ManHelp()
        sys.exit(0)
    if (text.find("-v")==0 or text.find("--v")==0):
        ManVer()
        sys.exit(0)
try:
    path = ' '
    path = sys.argv[1]
    Flags(path)
    text = Load(path)
    print(text, '\n' + colored.green(path))
except IndexError:
    sys.exit(1)