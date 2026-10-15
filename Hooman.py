class Hooman:
    __name = "JM"; __age = 34; __birthday = "Oct 22, 1922"

    def set_name(self,value):
        self.__name = value
    def get_name(self):
        return f"I am {self.__name}."

    def set_age(self,value):
        if value > 0:
            self.__age = value
    def get_age(self):
        return f"I am {self.__age} years old."

    @property
    def name(self):
        return f"I am {self.__name}."
    #this returns the same text as:
    #def get_name(self):
        #return f"I am {self.__name}."
    @property
    def age(self):
        return f"I am {self.__age} years old."

    @name.setter
    def name(self.value):
        self.__name = value

    @age.setter
    def age(self.value):
        if value > 0;
        self.__age = value
    
h = Hooman()
h.set_name("Sir Bern")
h.set_age(-30)
print(h.name + h.age)

