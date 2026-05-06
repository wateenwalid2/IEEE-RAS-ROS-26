class Package:
    current_id = 0
    def __init__(self,package_mass,destination = (0,0)):
        Package.current_id +=1
        self.pk_id = Package.current_id 
        self.package_mass = package_mass
        self.destination = destination

    #prepare the package to be saved in the dictionary
    def save_to_dict(self):
        return {
            "id": self.pk_id,
            "mass": self.package_mass,
            "destination": list(self.destination)
        }
    
    #prepare to recieve the packages from the fleet class
    @classmethod
    def save_from_dict(cls,data):
        return cls(
            package_mass=data["mass"],
            destination=tuple(data["destination"])
        )
    