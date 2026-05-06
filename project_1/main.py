from Fleet import Fleet
from Drone import Drone
from Package import Package
from PathPlanner import PathPlanner
from visualization import draw


path_planner = PathPlanner(20)
fleet = Fleet()
waiting_delveries = []
                
#simulate the drone flight from start to the end
def simulate_drone(drone_obj, pk_obj):
    going_path = path_planner.find_path(drone_obj.position, pk_obj.destination)
    for next_pos in going_path[1:]:
        drone_obj.position = next_pos
        draw(path_planner, fleet.drones, [pk_obj.destination],path_planner.no_fly_zones)

    drone_obj.deliver_package()
    print(f"Drone {drone_obj.d_id} delivered package {pk_obj.pk_id}")

    return_path = path_planner.find_path(drone_obj.position, (0, 0))
    for next_pos in return_path[1:]:
        drone_obj.position = next_pos
        draw(path_planner, fleet.drones, no_fly_zones=path_planner.no_fly_zones)
    
    drone_obj.battery = drone_obj.get_new_battery(path_planner,pk_obj)
    print(f"Drone {drone_obj.d_id} returned to base")
    fleet.store_data(path_planner)

#see if the package is assigned to the req. drone
def ensure_package_is_registered(drone_id,pk):
        for drone in fleet.drones :
                if(drone_id == drone.d_id):
                    sure = drone.register_pk_to_drone(pk, path_planner)
                    if sure:
                        return drone
                    drone.battery = 100.0
                    return None
        return None

def ensure_package_got_destination(x,y):
    if (x, y) in path_planner.no_fly_zones:
                print("Destination is in a no-fly zone, please choose another destination")
                return False
    else:
         return True


if __name__ == "__main__":
    fleet.load_data(path_planner)
    draw(path_planner, fleet.drones, no_fly_zones=path_planner.no_fly_zones) #at first no goals displayed in the simulation
    while True:
        print("\n=== AeroPath Menu ===")
        print("1. Add Drone")
        print("2. Add Package")
        print("3. Set No-Fly Zone")
        print("4. Start Simulation")
        print("5. Champions of Efficiency")
        print("6. Exit")
        choice = input("Choose an option: ")

        if (choice == "1"):
            drone_mass = float(input("Drone mass: "))
            max_capacity = float(input("Max capacity: "))
            drone = Drone(100.0,(0,0),drone_mass,max_capacity)
            print(f"Drone {drone.d_id} added")
            fleet.drones.append(drone)
            draw(path_planner, fleet.drones, no_fly_zones=path_planner.no_fly_zones) #to update the number of drones displayed in simulation

        elif (choice == "2"):
            mass = float(input("Package mass: "))
            while(True): #to ensure that it got the right destination
                x = int(input("Destination x: "))
                y = int(input("Destination y: "))
                if((x,y) == (0,0)):
                     print("wrong distination (start point)")
                elif(ensure_package_got_destination(x,y)):
                     break
            pk = Package(mass,(x, y))
            fleet.packages.append(pk)
            print(f"Package {pk.pk_id} added")
            drone_id = int(input("Which drone you want this package to be assigned to :"))
            while(True): #to ensure that it's registered to the suitable drone
                drone = ensure_package_is_registered(drone_id,pk)
                if drone is not None:
                    break
                else:
                    drone_id = int(input("choose another drone id: "))
            
            
            waiting_delveries.append((drone,pk))
            active_goals = []
            for _, pk in waiting_delveries:
                active_goals.append(pk.destination)
            draw(path_planner, fleet.drones, active_goals, path_planner.no_fly_zones) #to display the goals until starting the flights simulation 
            
        elif (choice == "3"):
            zone = []
            print("Enter coordinates one by one, type 'done' when finished")
            while True:
                x = input("x: ")
                if (x == "done"):
                    break
                y = input("y: ")
                zone.append((int(x), int(y)))
            path_planner.register_no_fly_zone(zone)
            print("No-fly zone registered")
            draw(path_planner, fleet.drones, no_fly_zones=path_planner.no_fly_zones) #to display the no-fly zones
        
        elif (choice == "4"):
            if (not waiting_delveries):
                print("No drones have been assigned packages yet, Use option 2 first")
                continue

            for drone, package in waiting_delveries:
                simulate_drone(drone, package)

            waiting_delveries.clear()

            draw(path_planner, fleet.drones, no_fly_zones=path_planner.no_fly_zones) #to remove the goals after delivering packages
            print("All deliveries completed")

        elif (choice == "5"):
            top = fleet.get_top_drones()
            print("\n=== Champions of Efficiency ===")
            i = 1
            for drone in top:
                print(f"{i}. Drone {drone.d_id} - {len(drone.delivered_packages)} packages delivered")
                i += 1

        elif choice == "6":
            fleet.store_data(path_planner)
            print("Data saved, Goodbye!")
            break

        else:
            print("Invalid option, try again")
    



