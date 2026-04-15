import json

def initialize_system():
    filename = "config.json"
    default_settings = {
        "version": "1.0",
        "status": "initial",
        "theme": "dark"
    }
    try:
        with open(filename,"r") as file:
            print("System Ready")
    except FileNotFoundError:
        print("File not found")
        with open(filename,"w") as file:
            json.dump(default_settings, file,indent = 4)


initialize_system()