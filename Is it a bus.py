class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
school_bus=bus("School Volvo",100,30)
print("The name of the bus is:",school_bus.name,"Max speed:",school_bus.max_speed,"mileage:",school_bus.mileage)