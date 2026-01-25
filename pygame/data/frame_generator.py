import pygame
from spritesheet import SpriteSheet

BLACK = (0, 0, 0)

def frame_generator(path, frame_count, width, height, scale=1):
    sprite_image = pygame.image.load(path).convert_alpha()
    sprite_sheet = SpriteSheet(sprite_image)

    frames = []
    for i in range(frame_count):
        frames.append(
            sprite_sheet.get_image(i, width, height, scale, BLACK)
        )

    return frames
