class Pet:
    def __init__(self, name, species):
        self._name = name
        self._species = species
        self._hunger = 50
        self._happiness = 50
        self._energy = 50
    
    def feed(self):
        self._hunger = max(0, self._hunger - 10)
        self._energy += 5

    def play(self):
        self._happiness = min(100, self._happiness + 15)
        self._energy = max(0, self._energy - 10)
        self._hunger += 5

    def sleep(self):
        self._energy = min(100, self._energy + 20)
        self._hunger += 5

    def get_status(self):
        return f"{self._name} the {self._species} | Hunger: {self._hunger} Happiness: {self._happiness} | Energy: {self._energy}" 

    def __str__(self):
        return f"{self._name} the {self._species}"     
# Example usage: