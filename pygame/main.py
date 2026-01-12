# Example file showing a circle moving on screen
import pygame
from pygame.examples.sprite_texture import sprite

import spirtesheet

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

sprite_image = pygame.image.load("assets/player_attack_ii.png").convert_alpha()

BLACK = (0, 0, 0)


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("images/player.png")
#         self.rect = self.image.get_rect()
#         self.rect.center(160, 520)
#
#


animation_list = []
animation_steps = 6

sprite_sheet = spirtesheet.SpriteSheet(sprite_image)


for i in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(i, 191, 191, 1, BLACK ))




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    # pygame.draw.circle(screen, "red", player_pos, 40)
    for i in range(len(animation_list)):
        screen.blit(animation_list[i], (i* 72,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()