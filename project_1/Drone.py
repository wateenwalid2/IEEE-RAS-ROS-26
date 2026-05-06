from Package import Package
from PathPlanner import PathPlanner

class Drone:

    current_id =0

    def __init__(self,battery = 100.0,position=(0,0),drone_mass = 5.0,max_capacity = 10.0):
        Drone.current_id +=1
        self.d_id = Drone.current_id
        self.battery = battery
        self.position = position
        self.drone_mass = drone_mass
        self.max_capacity = max_capacity
        self.available = True
        self.delivered_packages = []
        self.current_packages = []

    #prepare the drone to be saved in the dictionary
    def save_to_dict(self):
            delivered_packages_list = []
            for pk in self.delivered_packages:
                delivered_packages_list.append(pk.save_to_dict())
            return {
            "id": self.d_id,
            "battery": self.battery,
            "position": list(self.position),
            "drone_mass": self.drone_mass,
            "max_capacity": self.max_capacity,
            "available": self.available,
            "delivered_packages": delivered_packages_list
            }
    
    #prepare to recieve the drones from the fleet class
    @classmethod
    def save_from_dict(cls,data):
        drone = cls(
        battery=data["battery"],
        position=tuple(data["position"]),
        drone_mass=data["drone_mass"],
        max_capacity=data["max_capacity"]
        )

        packages_data = data.get("delivered_packages", [])
        delivered_packages_list = []
        for p in packages_data:
            package = Package.save_from_dict(p)
            delivered_packages_list.append(package)
        drone.delivered_packages = delivered_packages_list

        return drone
    
    #assign a the package to drone, return true or false
    def assign_new_package(self,package_obj):
        if (self.current_packages):
            print(f"Drone {self.d_id} is already carrying a package")
            return False
        elif(package_obj.package_mass <= self.max_capacity):
             self.current_packages.append(package_obj)
             self.available = False 
             return True
        else:
             print("Can't take this Package as it exceed the maximum capacity limit")
             return False
    
    #take the package delivered from current packages to delivered packages & mark the drone as available now
    def deliver_package(self):
        if (self.current_packages):
            self.delivered_packages.append(self.current_packages[0])
            self.current_packages.clear()
            self.available = True
 
        
    #before accepting the mission, it calculate the entire consumption of mission
    def evaluate_mission(self,path_obj,package_obj):
         going_dis = (len(path_obj.find_path(self.position, package_obj.destination)) - 1)
         returning_dis = (len(path_obj.find_path(package_obj.destination, (0, 0))) - 1)
         total_mass = self.drone_mass + package_obj.package_mass
         going_consumption = (0.1 * going_dis) + (total_mass * 9.81 * 0.01 * going_dis)
         returning_consumption = (0.1 * returning_dis) + (self.drone_mass * 9.81 * 0.01 * returning_dis)
         total_consumption = going_consumption + returning_consumption
         if((self.battery-total_consumption) > 10.0):
              
              return True
         else:
              return False
         
    #test the battery condtion before registering the package to drone      
    def register_pk_to_drone(self,pk_obj,path_obj):
        if not (self.evaluate_mission(path_obj, pk_obj)):
            print(f"Drone {self.d_id} does not have enough battery for this mission")
            return False

    
        return (self.assign_new_package(pk_obj))
    
    def get_new_battery(self,path_obj,package_obj):
         going_dis = (len(path_obj.find_path(self.position, package_obj.destination)) - 1)
         returning_dis = (len(path_obj.find_path(package_obj.destination, (0, 0))) - 1)
         total_mass = self.drone_mass + package_obj.package_mass
         going_consumption = (0.1 * going_dis) + (total_mass * 9.81 * 0.01 * going_dis)
         returning_consumption = (0.1 * returning_dis) + (self.drone_mass * 9.81 * 0.01 * returning_dis)
         total_consumption = going_consumption + returning_consumption
         return (self.battery-total_consumption)

         
         
    
    
    
    




         
    

    

    
    

    
    
    
    




