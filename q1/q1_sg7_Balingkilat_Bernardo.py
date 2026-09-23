class Glassware:
    def __init__(self,name='glassware'):
        self.name = name
        print(f"{self.name} has been created.")
    def functions(self):
        print(f"This {self.name} holds nothing.")
        
class Beaker (Glassware):
    def __init__(self,name="Beaker"):
        super().__init__(name) 
    def __del__(self):
        print(f"{self.name} is gone") 

class Tray:
    def __init__(self):
        self.glassware = Glassware("Glassware") 
        self.beaker = [Beaker(f"Beaker{i+1}") for i in range(5)]
        print("\nThe tray has been created.")
    def glassexist(self):
        print("Glassware is still existing")
    def _del_(self):
        del self.beaker
        print("\nTray has been deleted")
        
labGlass = Tray()
labGlass.glassexist()
del labGlass
