# SG 5 Activity 1: The RPG Hero


class Hero:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def take_damage(self,amount):
        self.hp -= amount


# Define hero names    
Hero1 = Hero("Arthur",100)
Hero2 = Hero("Morgana",100)


# Arthur take 10 damage part
Hero1.take_damage(10)
print("Arthur's HP is ",Hero1.hp," Morgana's HP is ",Hero2.hp)
