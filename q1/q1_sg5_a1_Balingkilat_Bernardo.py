class Hero:
    def __init__(self,name,HP = 100):
        self.name = name
        self.HP = HP
    def take_damage(self,amount):
        self.HP -= amount
        print(self.name , "has", self.HP,"HP left.")


myHero = Hero("Arthur")
myHero.take_damage(10)

hero2 = Hero("Morgana")
hero2.take_damage(0)

