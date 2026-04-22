from pet import Pet

class Fish(Pet):
    def __init__(self, name, species):
        super().__init__(name, "Fish")
        self._species = species

    def feed(self):
        super().feed()
        self._hunger = max(0, self._hunger - 10)
        print(f"{self._name} the {self._species} swims around happily after being fed.")

    def play(self):
        super().play()
        self._happiness = min(100, self._happiness + 5)  # Fish get a small happiness boost from playing
        self._energy = max(0, self._energy - 5)  # Fish use a small amount of energy when playing
        print(f"{self._name} the {self._species} swims in circles with excitement.")

    def blow_bubbles(self):
        self._energy = max(0, self._energy - 2)  # Blowing bubbles uses a bit of energy
        print(f"{self._name} the {self._species} blows bubbles in the water!")
        