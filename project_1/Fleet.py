import json
from Drone import Drone

class Fleet:
    def __init__(self):
        self.drones = [] #to use all drones stored 
        self.packages = [] 

    #store all data into the json file
    def store_data(self,path_obj):
        saved_data = {
        "drones": [],
        "no_fly_zones": list(path_obj.no_fly_zones)
        }
        for drone in self.drones:
            saved_data["drones"].append(drone.save_to_dict())

        with open("store_json.json",mode = "w",encoding="utf-8") as write_file:
            json.dump(saved_data,write_file,indent =4)
    
    #load all data form the json file
    def load_data(self,path_planner):
        try:
            with open("store_json.json",mode = "r",encoding="utf-8") as read_file:
                load_data =  json.load(read_file)
            self.drones = []
            for drone in load_data["drones"]:
                self.drones.append(Drone.save_from_dict(drone))
            path_planner.no_fly_zones = set(tuple(z) for z in load_data["no_fly_zones"])
            print("Data loaded successfully")
            return self.drones
        except Exception as e:
            print(f"An error occured {e}")
            return []
    
    #return a list of the top drones that delivered more packages
    def get_top_drones(self):
        result = list(self.drones)
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                if len(result[i].delivered_packages) < len(result[j].delivered_packages):
                    result[i], result[j] = result[j], result[i]
        return result
    


