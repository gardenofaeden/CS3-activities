class Father:
    hair = "Brown"

class Mother:
    eyes = "Blue"


class You(Father,Mother):
    def describeYourself(self):
        print("I have", self.hair, "hair and", self.eyes, "eyes.")
        
you = You()
you.describeYourself()
