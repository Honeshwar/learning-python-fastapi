class Enemy:
    type_of_enemy:str
    health_points:int = 10
    damage_points:int = 1

    def __init__(self,type_of_enemy) -> None:
        self.type_of_enemy = type_of_enemy

    def walk_forward(self)->None:
        pass
    def attack(self)->None:
        pass
    def talk(self)->None:
        pass


 