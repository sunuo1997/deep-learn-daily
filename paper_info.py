import json

def readJson(path):
    file = open(path,"r")
    fileJson = json.load(file)
    result = fileJson['result']
    hits = result["hits"]
    hit = hits['hit']
    print(hit)

readJson("paper_info.json")

