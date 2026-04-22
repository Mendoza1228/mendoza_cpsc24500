from pet import Pet


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")
    
    def feed(self):
        super().feed()
        print(f"{self._name} purrs happily after being fed.")

    def play(self):
        super().play()
        self._happiness = min(100, self._happiness + 5)  # Cats get extra happiness from playing
        self._energy = max(0, self._energy - 5)  # Cats use less energy when playing
        print(f"{self._name} bats at the toy with excitement.")

    def purr(self):
        print(f"{self._name} is purring contentedly.")
