import pygame
from math import *

class Bullet:
	def __init__(self, rect, _dir, vel):
		self.rect = rect
		self._dir = _dir
		self.vel = vel
		self.dx = cos(self._dir) * self.vel
		self.dy = sin(self._dir) * self.vel

	def update(self):
		self.rect.move_ip(self.dx, self.dy)

	def draw(self, surf, camera):
		pygame.draw.circle(surf, (30, 30, 30), (camera.offset_rect(self.rect).centerx, camera.offset_rect(self.rect).centery), self.rect.width / 2)