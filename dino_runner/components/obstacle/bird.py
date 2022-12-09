import random
from  dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
    
    def draw(self, screen):
        if self.index >= 9:
           self.index = 0
        return super().draw(screen)