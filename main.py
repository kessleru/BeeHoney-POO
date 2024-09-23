import pygame
from obj import Obj
from menu import Menu, GameOver
from game import Game
pygame.init()

class Main:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()


    def draw(self):
        self.window.fill([0, 0, 0])
        if self.menu.change_scene == False:
            self.menu.draw(self.window)
        elif self.game.change_scene == False:
            self.game.draw(self.window)
            self.game.update()
        elif self.gameover.change_scene == False:
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0




    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if self.menu.change_scene == False:
                self.menu.events(events)
            elif self.game.change_scene == False:
                self.game.bee.move__bee(events)
            else:
                self.gameover.events(events)
            

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


game = Main(360, 640, "BeeHoney")
game.update()
