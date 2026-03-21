class Hippo:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def move(self):
        return f"{self.name} топает"

class PygmyHippo(Hippo):
    def __init__(self, name, weight, forest):
        super().__init__(name, weight)
        self.forest = forest

    def hide(self):
        return f"{self.name} спрятался в лесу {self.forest}"
