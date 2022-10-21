import json
data = [
    "hi",
    "NO u"
]
with open("jP.json", "w") as file:
    json.dump(data,file,sort_keys = True, indent=1)
    #json.dump({'4': 5, '6': 7},file, sort_keys=True, indent=4)