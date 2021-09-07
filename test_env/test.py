import json

with open("save.json", "r") as read_file:
    SaveData = json.load(read_file)
print(SaveData)
playerInfo = SaveData.get("playerInfo")
print(playerInfo)
inventory = playerInfo.get("inventory")
print(inventory)
