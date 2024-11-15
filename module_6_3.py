from random import randint
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords=[0, 0, 0]):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        try_cords = [dx*self.speed, dy*self.speed, dz*self.speed]
        if self._cords[-1] < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = try_cords

    def get_cords(self):
        print('X:', self._cords[0], 'Y:', self._cords[1], 'Z:', self._cords[2])

    def attack(self):
        if self._DEGREE_OF_DANGER<5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER>5:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print('Here are(is)', randint(1, 4), 'eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[-1] -= int(dz*self.speed/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    def speek(self):
        print("Click-click-click")

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speek()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()