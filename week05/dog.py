from pet import Pet

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self._breed = breed

    def feed(self):
        super().feed()
        self._hunger = max(0, self._hunger - 20)
        print(f"{self._name} the {self._breed} wags its tail happily after being fed.")

    def play(self):
        super().play()
        self._happiness = min(100, self._happiness + 10)  # Dogs get extra happiness from playing
        self._energy = max(0, self._energy - 15)  # Dogs use more energy when playing
        print(f"{self._name} the {self._breed} fetches the ball with enthusiasm.")

    def bark(self):
        self._energy = max(0, self._energy - 5)  # Barking uses a bit of energy
        print(f"{self._name} the {self._breed} barks loudly!")
        
