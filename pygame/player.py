import pygame
from data.asset_mapping import player_assets
from data.frame_generator import frame_generator

FRAME_W = 199
FRAME_H = 191
GROUND_Y = 520


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()


        # LOAD ANIMATIONS

        self.animations = {
            state: frame_generator(path, frames, FRAME_W, FRAME_H)
            for state, (path, frames) in player_assets.items()
        }


        # ANIMATION STATE

        self.state = "idle"
        self.prev_state = None
        self.frame_index = 0
        self.animation_speed = 10

        self.image = self.animations[self.state][0]
        self.rect = self.image.get_rect(topleft=pos)


        # PHYSICS

        self.velocity = pygame.Vector2(0, 0)
        self.speed = 300
        self.gravity = 2000
        self.jump_force = -550
        self.on_ground = False


        # STATE LOCKS

        self.locked_states = {"attack_primary", "take_hit", "death"}

        # EVENTS

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            # Jump (ground only)
            if event.key == pygame.K_SPACE and self.on_ground:
                self.velocity.y = self.jump_force
                self.on_ground = False
                self.set_state("jump")

            # Attack (ground or air)
            if event.key == pygame.K_q:
                if self.state not in self.locked_states:
                    self.set_state("attack_primary")


    # UPDATE

    def update(self, dt):
        if self.state not in self.locked_states:
            self.handle_input()
            self.handle_state()

        self.apply_gravity(dt)
        self.move(dt)
        self.check_ground()
        self.animate(dt)


    # INPUT

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0

        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
        if keys[pygame.K_d]:
            self.velocity.x = self.speed


    # STATE LOGIC

    def handle_state(self):
        if not self.on_ground:
            if self.velocity.y < 0:
                self.set_state("jump")
            else:
                self.set_state("fall")
        elif self.velocity.x != 0:
            self.set_state("run")
        else:
            self.set_state("idle")

    def set_state(self, new_state):
        if new_state != self.state:
            self.prev_state = self.state
            self.state = new_state
            self.frame_index = 0


    # PHYSICS

    def apply_gravity(self, dt):
        self.velocity.y += self.gravity * dt

    def move(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

    def check_ground(self):
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.velocity.y = 0
            self.on_ground = True
        else:
            self.on_ground = False


    # ANIMATION

    def animate(self, dt):
        frames = self.animations[self.state]
        self.frame_index += self.animation_speed * dt

        if self.frame_index >= len(frames):
            if self.state in self.locked_states:
                self.set_state("idle")
            else:
                self.frame_index = 0

        self.image = frames[int(self.frame_index)]
