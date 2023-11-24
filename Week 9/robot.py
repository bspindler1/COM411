class Robot:

    MAX_ENERGY = 100
    def __init__(self, name="Robot", age=0):
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old with an energy of {self.energy}'

    def grow(self):
        self.age = self.age + 1

    def eat(self, amount):
        p_energy = self.energy + amount
        if p_energy > Robot.MAX_ENERGY:
            return p_energy - self.energy
        else:
            p_energy = self.energy
            return 0

    def move(self, distance):
        p_energy = self.energy - distance
        if p_energy < 0:
            self.energy = 0
            return self.energy - abs(p_energy)
        else:
            self.energy = p_energy
            return 0


if (__name__ == "__main__"):
  robot = Robot()
  robot.display()


