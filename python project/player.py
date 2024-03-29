import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,collision_sprites):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE // 2,TILE_SIZE))
		self.image.fill(PLAYER_COLOR)
		self.rect = self.image.get_rect(topleft = pos)

		# player movement 
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.collision_sprites = collision_sprites
		self.on_floor = False

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		if keys[pygame.K_SPACE] and self.on_floor:
			self.direction.y = -self.jump_speed

	def horizontal_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0: 
					self.rect.left = sprite.rect.right
				if self.direction.x > 0: 
					self.rect.right = sprite.rect.left

	def vertical_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0

		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y
	
	def bottom_bound(self):
		if self.rect.top > len(LEVEL_MAP) * TILE_SIZE:
			self.rect.topleft = (0,0)
			
			

	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collisions()
		self.apply_gravity()
		self.vertical_collisions()
		self.bottom_bound()


class Player2(pygame.sprite.Sprite):
	def __init__(self,pos,groups,collision_sprites):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE // 2,TILE_SIZE))
		self.image.fill(PLAYER2_COLOR)
		self.rect = self.image.get_rect(topright = pos)
		
		# player movement 
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.collision_sprites = collision_sprites
		self.on_floor = False
		self.holding = False

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.direction.x = -1
		elif keys[pygame.K_d]:
			self.direction.x = 1
		else:
			self.direction.x = 0

		if keys[pygame.K_g] and self.on_floor:
			self.direction.y = -self.jump_speed

		if keys[pygame.K_h] and self.holding:
			if self.direction.x > 0:
				self.throw(facing_right=True)
			elif self.direction.x < 0:
				self.throw(facing_right=False)



	def horizontal_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0: 
					self.rect.left = sprite.rect.right
				if self.direction.x > 0: 
					self.rect.right = sprite.rect.left

	def vertical_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0

		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y
	
	def bottom_bound(self):
		if self.rect.top > len(LEVEL_MAP) * TILE_SIZE:
			self.rect.topleft = (0,0)

			
	def throw(self, facing_right):
		speed = 10
		if facing_right:
			self.direction = pygame.math.Vector2(1,0)
		else:
			self.direction = pygame.math.Vector2(-1,0)
		self.offset = self.direction * speed	

	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collisions()
		self.apply_gravity()
		self.vertical_collisions()
		self.bottom_bound()

