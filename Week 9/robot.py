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


if (__name__ == "__main__"):
  robot = Robot()
  robot.display()

