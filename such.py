import sys
file = sys.argv[1]
def Load(file):
    load = open(file, "rb")
    r = load.read()
    return r.decode(encoding="utf-8")
load = Load(file)
print(load)