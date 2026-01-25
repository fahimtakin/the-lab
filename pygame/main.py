import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

player = Player((160, 520))
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_event(event)

    all_sprites.update(dt)

    screen.fill("purple")
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
