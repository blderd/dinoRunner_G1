import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinasour.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacleManager import ObstacleManager
from dino_runner.components.score_menu.text_utils import *
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.powerup.powerupManager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 30
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager() 
        self.player_heart_manager = PlayerHeartManager()

        self.points = 0
        self.death_count = 0
        self.running = True

        self.power_up_manager = PowerUpManager()

    def run(self):
        self.obstacle_manager.reset_obstacles(self)
        self.player_heart_manager.reset_heart()
        self.power_up_manager.reset_power_ups(self.points)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        # pygame.quit()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill( (255,255,255) )
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if(self.x_pos_bg <= -image_width):
            self.screen.blit(BG , ( image_width + self.x_pos_bg, self.y_pos_bg ) )
            self.x_pos_bg = 0
        self.x_pos_bg = self.x_pos_bg - self.game_speed
        
    def score(self):
        self.points = self.points + 1

        if self.points % 100 == 0:
            self.game_speed += 1
        
        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)
        self.player.check_invisivility(self.screen)

    def show_menu(self):
        self.running = True

        white_color = (255,255,255)
        self.screen.fill(white_color)

        self.print_menu_elements(self.death_count)
        pygame.display.update()
        self.handle_key_events_on_menu()


    def print_menu_elements(self, death_count = 0):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if death_count == 0:
            text, text_rect = get_centered_message('Press any key to Start')
            self.screen.blit(text, text_rect)
        elif death_count > 0:
            text, text_rect = get_centered_message('Press any key to Restart')
            score, score_rect = get_centered_message('Your score ' + str(self.points), height = half_screen_height + 50)
            death, death_rect = get_centered_message('You died ' + str(self.death_count) + ' times ', height= half_screen_height + 100)
            
            self.screen.blit(death, death_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)


    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                print("Dino: Good bye!!")
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if(event.type == pygame.KEYDOWN):
                self.run()