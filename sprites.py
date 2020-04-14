
import pygame
from settings import *
from tilemap import collide_hit_rect
vec = pygame.math.Vector2

def collide_with_walls(sprite, group, direction):
    if direction == "x":
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x

    if direction == "y":
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.midbottom = self.rect.midbottom
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.last_shot = 0

    def get_keys(self):
        self.vel = vec(0, 0)
        k = pygame.key.get_pressed()
        if k[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
        if k[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
        if k[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
        if k[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


        if k[pygame.K_LEFT] and k[pygame.K_UP]:
            dir = vec(-0.7071, -0.7071)
            self.shoot(dir)
        if k[pygame.K_RIGHT] and k[pygame.K_UP]:
            dir = vec(0.7071, -0.7071)
            self.shoot(dir)
        if k[pygame.K_RIGHT] and k[pygame.K_DOWN]:
            dir = vec(0.7071, 0.7071)
            self.shoot(dir)
        if k[pygame.K_LEFT] and k[pygame.K_DOWN]:
            dir = vec(-0.7071, 0.7071)
            self.shoot(dir)

        if k[pygame.K_LEFT]:
            dir = vec(-1, 0)
            self.shoot(dir)
        if k[pygame.K_RIGHT]:
            dir = vec(1, 0)
            self.shoot(dir)
        if k[pygame.K_UP]:
            dir = vec(0, -1)
            self.shoot(dir)
        if k[pygame.K_DOWN]:
            dir = vec(0, 1)
            self.shoot(dir)

    def shoot(self, dir):
        now = pygame.time.get_ticks()
        if now - self.last_shot > BULLET_RATE:
            self.last_shot = now
            Bullet(self.game, self.pos, dir)

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, "x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, "y")
        self.rect.midbottom = self.hit_rect.midbottom

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = MOB_HEALTH

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.vel = vec(MOB_SPEED, 0).rotate(-self.rot)
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, "x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, "y")
        self.rect.center = self.hit_rect.center
        # Killing mob
        if self.health <= 0:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        self.vel = dir * BULLET_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > BULLET_LIFETIME:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y