from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    def __init__(self, image):
        ranHeight = random.randint(0, 1)
        self.type = 0
        self.image = image
        super().__init__(self.image, self.type)
        self.step_index = 0
        self.rect.y = 250
        self.rect.y = 250 if ranHeight == 1 else 200
    
    def draw(self, SCREEN):
        if self.step_index >= 10:
            self.step_index = 0

        SCREEN.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

    
    # def fly(self):
    #     self.image = BIRD[0] if self.step_index < 5 else BIRD[1]