################################################################################
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((735, 413))
bg = pygame.image.load('sprites/bg.jpg')
goose = pygame.image.load('sprites/goose.png')
pygame.display.set_caption('Goose')
sound = pygame.mixer.Sound('sound/goose.mp3')
sound.play()
x = 0
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    screen.blit(bg, (x % bg.get_width() - bg.get_width(), 0))
    screen.blit(bg, (x % bg.get_width(), 0))
    screen.blit(goose, (300, 200))
    x -= 2
    pygame.display.update()
################################################################################
