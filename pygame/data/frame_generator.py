import pygame

import spritesheet


def frame_generator(character):

    animation_cooldown = 100

    character_assets = character.assets[0]

    sprite_image = pygame.image.load(character_assets).convert_alpha()

    BLACK = (0, 0, 0)

    animation_list = []
    animation_steps = int(character.assets[1])

    sprite_sheet = spritesheet.SpriteSheet(sprite_image)

    for i in range(animation_steps):
        animation_list.append(sprite_sheet.get_image(i, 199, 191, 1, BLACK))


    return [animation_list, animation_steps, animation_cooldown]



