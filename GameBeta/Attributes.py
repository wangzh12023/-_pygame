class Collidable:
    def __init__(self):
        self.collidingWith = {
            "obstacle": False, 
            "npc": False, 
            "monster": False, 
            "portal": False, 
            "boss": False, 
            "bossAttack":False,
        }
        self.collidingObject = {
            "obstacle": [], 
            "npc": None, 
            "monster": None, 
            "portal": None, 
            "boss": None, 
            "bossAttack":None
        }
    
    def is_colliding(self):
        return (self.collidingWith["obstacle"] or 
                self.collidingWith["npc"] or 
                self.collidingWith["monster"] or
                self.collidingWith["portal"] or 
                self.collidingWith["boss"] or
                self.collidingWith["bossAttack"])
