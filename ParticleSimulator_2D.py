# This file will be a particle simulator on a two dimensional scale.
# This file is based on
# https://github.com/anishsatalkar/python_gravity_simulation_pygame/blob/master/gravity_simulation.py


import math as m
import random
import sys
import time as t

import pygame

from FundamentalForces import *

start = t.time()

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
		self.mass = float(particle_mass[p_type_string]) * modifier_10


possible_particle_type = ('p', 'e')  # , 'n')

particles = []
for i in range(number_of_bodies):
	particle_type = str(random.choice(possible_particle_type))
	pos_x = random.randint(19, (size_of_window[0] - 20))
	pos_y = random.randint(19, (size_of_window[1] - 20))
	
	particles.append(Particle(particle_type, [pos_x, pos_y], [0, 0], [0, 0]))

pygame.init()
screen = pygame.display.set_mode(size_of_window)

font = pygame.font.SysFont('Arial', 20)
text = font.render('0', True, Colors['Blue'])
textRect = text.get_rect()
simulator_on = 0
while True:
	in_t = t.time()
	screen.fill(Colors['Black'])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	for particle_a in particles:
		a_type = particle_a.ptype
		a_position = particle_a.position
		a_acceleration = particle_a.acceleration
		a_velocity = particle_a.velocity
		a_mass = particle_a.mass
		
		fx_total = 0
		fy_total = 0
		
		for particle_b in particles:
			b_type = particle_b.ptype
			b_position = particle_b.position
			b_mass = particle_b.mass
			if b_position == a_position:
				continue
			
			# Gravity function
			force = calculate_gravity(a_position, a_mass, b_position, b_mass)
			# Electromagnetic Function
			force = calculate_electromagnetic(force, a_position, b_position, a_mass, b_mass, a_type, b_type)
			
			fx_total += force[0]
			fy_total += force[1]
		
		a_acceleration[0] = fx_total / a_mass
		a_acceleration[1] = fy_total / a_mass
		
		a_velocity[0] = a_velocity[0] + a_acceleration[0]
		a_velocity[1] = a_velocity[1] + a_acceleration[1]
		
		a_position[0] = a_position[0] + a_velocity[0]
		a_position[1] = a_position[1] + a_velocity[1]
		
		size_of_blip = 0
		if a_type == 'p':
			size_of_blip += 10
		elif a_type == 'n':
			size_of_blip += 10
		else:
			size_of_blip += 3
		
		# Prevent blocks from going of screen
		if a_position[0] < 0:  # Left
			a_position[0] *= 0
			a_velocity[0] *= -1
		elif (a_position[0] + size_of_blip) > size_of_window[0]:  # Right
			a_position[0] *= 0
			a_position[0] += (size_of_window[0] - size_of_blip)
			a_velocity[0] *= -1
		if a_position[1] < 0:  # Top
			a_position[1] *= 0
			a_velocity[1] *= -1
		elif (a_position[1] + size_of_blip) > size_of_window[1]:  # Bottom
			a_position[1] *= 0
			a_position[1] += (size_of_window[1] - size_of_blip)
			a_velocity[1] *= -1
		# /Prevent blocks from going of screen
		
		velocity_text = 'V=({},{})'.format(a_velocity[0].__round__(5), a_velocity[1].__round__(5))
		text = font.render(velocity_text, True, Colors['Blue'])
		textRect.center = (a_position[0] + 10, a_position[1] + 10)
		
		screen.blit(text, textRect)
		
		pygame.draw.rect(screen, Colors[a_type], pygame.Rect(a_position[0], a_position[1], size_of_blip, size_of_blip))
	
	pygame.display.flip()
	print('Time since start: ' + str(t.time() - start))
