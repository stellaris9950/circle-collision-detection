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

    def collisionWithFood(self, food):
        distance = self.pos - food.pos
        displacment = math.sqrt(distance.x ** 2 + distance.y ** 2)
        if displacment <= self.radius:
            return True



class Food:
    def __init__(self):
        self.radius = random.randrange(5, 20)
        self.pos = pygame.Vector2(random.randrange(0, 720), random.randrange(0, 540))
        self.color = pygame.Vector3(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))



def findMouse(player_pos):

    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    distance = mouse_pos - player_pos
    total = abs(distance.x) + abs(distance.y)
    move_factor = pygame.Vector2(distance.x / total, distance.y / total)

    return move_factor




food_list = []
def createFood():
    if random.randrange(1, 100) == 5:
        food_list.append(Food())



# pygame Run
pygame.init()

screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

radius_of_player = 100
circle_movement = 300*dt
growth_factor = 0.5

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
    createFood()

    move_factor = findMouse(player_pos)
    player = Player(radius_of_player, player_pos, move_factor)

    for food in food_list:
        if player.collisionWithFood(food):
            food_list.remove(food)
            radius_of_player += food.radius * growth_factor

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    # draw player
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    player.moveCircle(mouse_pos)

    pygame.draw.circle(screen, "black", player.pos, player.radius)


    # draw food
    for food in food_list:
        pygame.draw.circle(screen, food.color, food.pos, food.radius)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
