# 파일의 문자열 불러오기 (simple)
import sys
import os.path
def Load(file):
    isfile = Isfile(file)
    if isfile == -1:
        print(-1)
        return exit()
    load = open(file, "rb")
    r = load.read()
    text = r.decode(encoding="utf-8") # Text가 반환됨
    if text.find("\n"):
        text = text.strip("\n")
    return text  
def Isfile(file):
    if os.path.isfile(file):
        return 1
    else:
        return -1
def PathInput():
    file = sys.argv[1]
    return file
path = PathInput()
print(Load(path))