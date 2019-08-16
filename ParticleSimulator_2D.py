# This file will be a particle simulator on a two dimensional scale.
# This file is based on
# https://github.com/anishsatalkar/python_gravity_simulation_pygame/blob/master/gravity_simulation.py


import random
import time as t
import math as m
import numpy
import sys
import pygame
from ImportantMathForCode import *

start = t.time()

number_of_bodies = 100
size_of_window = 500, 500

Colors = {
	'White': (255, 255, 255),
	'Black': (0, 0, 0),
	'Blue': (109, 196, 255),
	'p': (255, 0, 255),
	'e': (255, 255, 0),
	'n': (255, 255, 255)
	}  # (Red, Green, Blue) color values from 0 to 255


class Particle:
	def __init__(self, particle_type, position, acceleration, velocity):
		self.ptype = particle_type  # This determines what kind of particle it is; one of three is the input 'p', 'n', 'e'
		self.position = position  # The position is a list [x, y]; position is measured in pixels
		self.acceleration = acceleration  # Acceleration is a list [x, y] measured in pixels
		self.velocity = velocity  # Same as Acceleration, but the actual velocity component
		
		p_type_string = str(particle_type)
		self.mass = float(particle_mass[p_type_string]) * mass_modifier


def calculate_forces_between_p_and_n():
	return None  # temp


def calculate_forces_between_p_and_e():
	return None  # Temp


def calculate_forces_between_e_and_n():
	return None


def gravity(a_pos, a_mass, b_pos, b_mass):
	x_diff = b_pos[0] - a_pos[0]
	y_diff = b_pos[1] - a_pos[1]
	hypotenuse = m.sqrt((x_diff ** 2) + (y_diff ** 2))
	sin = x_diff / hypotenuse
	cos = y_diff / hypotenuse
	
	f = (constant_G * a_mass * b_mass) / (hypotenuse ** 2)
	
	fx = f * sin
	fy = f * cos
	
	return fx, fy


possible_particle_type = ('p', 'e', 'n')

particles = []
for i in range(number_of_bodies):
	particle_type_int = random.randint(-1, 2)
	particle_type = str(possible_particle_type[particle_type_int])
	pos_x = random.randint(9, (size_of_window[0] - 10))
	pos_y = random.randint(9, (size_of_window[1] - 10))
	
	particles.append(Particle(particle_type, [pos_x, pos_y], [0, 0], [0, 0]))

pygame.init()
screen = pygame.display.set_mode(size_of_window)

font = pygame.font.SysFont('Arial', 20)
text = font.render('0', True, Colors['Blue'])
textRect = text.get_rect()
simulator_on = 0
while simulator_on == 0:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			simulator_on += 1
	
	for particle_a in particles:
		a_type = particle_a.ptype
		a_pos = particle_a.position
		a_accel = particle_a.acceleration
		a_vel = particle_a.velocity
		a_mass = particle_a.mass
		
		fx_total = 0
		fy_total = 0
		
		for particle_b in particles:
			b_type = particle_b.ptype
			b_pos = particle_b.position
			b_mass = particle_b.mass
			if b_pos == a_pos:
				continue
			
			fx, fy = gravity(a_pos, a_mass, b_pos, b_mass)
			fx_total += fx
			fy_total += fy
		
		a_accel[0] = fx_total / a_mass
		a_accel[1] = fy_total / a_mass
		
		a_vel[0] = a_vel[0] + a_accel[0]
		a_vel[1] = a_vel[1] + a_accel[1]
		
		a_pos[0] = a_pos[0] + a_vel[0]
		a_pos[1] = a_pos[1] + a_vel[1]
		
		velocity_text = 'V=({},{})'.format(a_vel[0].__round__(3), a_vel[1].__round__(3))
		text = font.render(velocity_text, True, Colors['Blue'])
		textRect.center = (a_pos[0] + 10, a_pos[1] + 10)
		
		screen.blit(text, textRect)
		
		size_of_blip = 0
		if a_type == 'p':
			size_of_blip += 10
		elif a_type == 'n':
			size_of_blip += 10
		else:
			size_of_blip += 3
		
		pygame.draw.rect(screen, Colors[a_type], pygame.Rect(a_pos[0], a_pos[1], size_of_blip, size_of_blip))
	
	pygame.display.flip()
	print('Time since start: ' + str(t.time() - start))
