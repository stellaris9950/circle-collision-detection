# Import External Librarys
import pygame
import random
import math

# Create Player
class Player:
    def __init__(self, radius: int, pos: pygame.Vector2, move_facotr: pygame.Vector2):
        self.radius = radius
        self.pos = pos
        self.move = pygame.Vector2(move_facotr.x * 5    , move_facotr.y * 5)

    def moveCircle(self, mouse):
        self.pos += self.move

        distance = mouse - self.pos
        displacment = math.sqrt(distance.x **2 + distance.y **2)

        if displacment <= 10:
            self.pos = mouse


class Food:
    def __init__(self, radius: int, pos: pygame.Vector2):
        self.radius = radius
        self.pos = pos




def findMouse(player_pos):

    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    distance = mouse_pos - player_pos
    total = abs(distance.x) + abs(distance.y)
    move_factor = pygame.Vector2(distance.x / total, distance.y / total)

    return move_factor




food_list = []
def createFood():
    print("food created")




# pygame Run
pygame.init()

screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0


circle_movement = 300*dt

lose = False
win = False
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # write a function that runs at random  random.randrange in range (sfasd f)


    move_factor = findMouse(player_pos)
    player = Player(100, player_pos, move_factor)




    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    # draw player
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    player.moveCircle(mouse_pos)

    pygame.draw.circle(screen, "black", player.pos, player.radius)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
