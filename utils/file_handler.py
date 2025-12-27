import json
import os

def load_user(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath,"r") as file:
        return json.load(file)
    
    
def save_json(filepath,data):
    with open(filepath,"w") as file:
        json.dump(data,file,indent=4)
        