import  pygame
from pygame.examples.moveit import WIDTH

pygame.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Trial Game')

WHITE = (255,255,255)
RED = (255,0,0)
Green = (0,255,0)
blue = (0,0,255)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
screen.fill(WHITE)

pygame.display.flip()

clock.tick(60)

pygame.quit()
