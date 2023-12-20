# Import External Librarys
import pygame
import random
import math

# Create walls,only run once
class Player:
    def __init__(self, radius: int, pos: pygame.Vector2, move_facotr: pygame.Vector2):
        self.radius = radius
        self.pos = pos
        self.move = pygame.Vector2(move_facotr.x * 10, move_facotr.y * 10)


    def moveCircle(self, mouse):
        self.pos += self.move
        # print(self.pos)

        distance = mouse - self.pos

        displacment = math.sqrt(distance.x **2 + distance.y **2)

        if displacment <= 10:
            self.pos = mouse

            # self.pos.x = mouse[0]
            # self.pos.y = mouse[1]
class Food:
    def __init__(self, radius: int, pos: pygame.Vector2):
        self.radius = radius
        self.pos = pos




# pygame setup

"""
circle_list = []
obstacles_list = []
def createDraw():

    times = random.randrange(5, 10)
    for i in range(times):
        circle_pos = pygame.Vector2(random.randrange(10, 700), random.randrange(10, 500))
        circle_direction = pygame.Vector2(2, 2)
        circle_created = Circles(20, circle_pos, circle_direction)

        circle_list.append(circle_created)

        # square_size = pygame.Vector2(20, 20)
        # square_pos = pygame.Vector2(random.randrange(10, 700), random.randrange(10, 500))
        rect_created = pygame.Rect(random.randrange(10, 700),
                                   random.randrange(10, 500),
                                   20, 20)
        square_direction = pygame.Vector2(5, 5)
        square_created = Obstacles(rect_created, square_direction)



        obstacles_list.append(square_created)




def mouseDetect(obstacle_list, circle_list):
    mouse_pos = pygame.mouse.get_pos()

    for obstacle in obstacles_list:
        if obstacle.rect.collidepoint(mouse_pos):
            return obstacle

    for circle in circle_list:
        if circle.pos.distance_to(mouse_pos) < circle.radius:
            return circle

createDraw()
"""
def findMouse(player_pos):

    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    distance = mouse_pos - player_pos
    total = abs(distance.x) + abs(distance.y)
    move_factor = pygame.Vector2(distance.x / total, distance.y / total)

    return move_factor





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




    move_factor = findMouse(player_pos)
    player = Player(10, player_pos, move_factor)

    # print(player)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    """

    # draw
    for circle in circle_list:
        pygame.draw.circle(screen, "green", circle.pos, circle.radius)
        circle.moveCircle()
        # collisionDetection(position, circle_movement, boarders)

    for obstacle in obstacles_list:
        pygame.draw.rect(screen, "red", obstacle.rect)
        obstacle.moveObstacles()



    """
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
