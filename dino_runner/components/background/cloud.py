from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD
import random

class Cloud:
    def __init__(self, game_speed):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.game_speed = game_speed
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))