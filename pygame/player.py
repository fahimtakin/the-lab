import pygame

from data import asset_mapping



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.assets = asset_mapping.player_assets["attack_primary"]
        self.state="idle"
#         super().__init__()
#         self.image = pygame.image.load("images/player.png")
#         self.rect = self.image.get_rect()
#         self.rect.center(160, 520)
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
#

#
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
# player = player.Player()
# player_assets = player.assets[0]
#
# sprite_image = pygame.image.load(player_assets).convert_alpha()
#
# BLACK = (0, 0, 0)


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("images/player.png")
#         self.rect = self.image.get_rect()
#         self.rect.center(160, 520)
#
#

