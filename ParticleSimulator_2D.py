# This file will be a particle simulator on a two dimensional scale.
# This file is based on
# https://github.com/anishsatalkar/python_gravity_simulation_pygame/blob/master/gravity_simulation.py

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
	def __init__(self, particletype, position, acceleration, velocity):
		self.particletype = particletype  # This determines what kind of particle it is
		self.position = position  # The position is a list [x, y]; position is measured in pixels
		self.acceleration = acceleration  # Acceleration is a list [x, y] measured in pixels
		self.velocity = velocity  # Same as Acceleration, but the actual velocity component
		
		p_type_string = str(particletype)
		self.mass = float(particle_mass[p_type_string]) * modifier_scale


particles = []
if auto_make_particles is True:
	for i in range(number_of_bodies):
		particle_type = str(random.choice(possible_particle_type))
		pos_x = random.randint(19, (size_of_window[0] - 20))
		pos_y = random.randint(19, (size_of_window[1] - 20))
		
		particles.append(Particle(particle_type, [pos_x, pos_y], [0, 0], [0, 0]))

# Test particles
# particles.append(Particle('p', [40, 40], [0, 0], [0, 0]))
# particles.append(Particle('p', [size_of_window[0] - 40, size_of_window[1] - 40], [0, 0], [0, 0]))
# /Test particles

pygame.init()
screen = pygame.display.set_mode(size_of_window)

font = pygame.font.SysFont('Arial', 20)
text = font.render('0', True, Colors['Blue'])
textRect = text.get_rect()
footer_font = pygame.font.SysFont('Consolas', 12)
footer = f'[D]ebug [Q]uit [+]Increase Max Fps [-]Decrease Max Fps'
f_text = footer_font.render(footer, True, Colors['White'])
f_textRect = f_text.get_rect()
f_textRect.bottomleft = (0, size_of_window[0])
simulator_on = 0
simulation_clock = pygame.time.Clock()
max_fps = 120
framerate = 60
debug = False
while True:
	simulation_clock.tick(framerate)
	in_t = t.time()
	screen.fill(Colors['Black'])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			elif event.key in [pygame.K_PLUS, pygame.K_KP_PLUS]:
				# Increase speed of simulation (capped at 120 fps for now)
				if framerate < 5:
					framerate += 1
				else:
					framerate = min(max_fps, framerate + 5)
			
			elif event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
				# Decrease speed of simulation (Capped at 1 fps)
				if framerate <= 5:
					framerate = framerate - 1 if framerate - 1 else 1
				else:
					framerate -= 5
			
			elif event.key == pygame.K_d:
				# Toggle Debug Text
				debug = ~debug
	
	for particle_a in particles:
		a_type = particle_a.particletype
		a_position = particle_a.position
		a_acceleration = particle_a.acceleration
		a_velocity = particle_a.velocity
		a_mass = particle_a.mass
		
		fx_total = 0
		fy_total = 0
		
		for particle_b in particles:
			b_type = particle_b.particletype
			b_position = particle_b.position
			b_mass = particle_b.mass
			if b_position == a_position:
				continue
			force = [0, 0]
			# Gravity function
			force += calculate_gravity(a_position, a_type, b_position, b_type)
			# Electromagnetic Function
			force += calculate_electromagnetic(a_position, a_type, b_position, b_type)
			# Strong Nuclear Force Function
			
			fx_total += force[0]
			fy_total += force[1]
		
		a_acceleration[0] = fx_total / a_mass
		a_acceleration[1] = fy_total / a_mass
		
		a_velocity[0] = a_velocity[0] + a_acceleration[0]
		a_velocity[1] = a_velocity[1] + a_acceleration[1]
		
		# Universal Slowing of particles
		if Autoslowdown['Slow'] is True:
			for vel in a_velocity:
				if vel < (0 - (Autoslowdown['SlowFactor'])):
					vel += Autoslowdown['SlowFactor']
				if vel > Autoslowdown['SlowFactor']:
					vel -= Autoslowdown['SlowFactor']
		# /Universal Slowing of particles
		
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
		
		# Velocity text
		if debug:
			velocity_text = 'V=({},{})'.format(a_velocity[0].__round__(5), a_velocity[1].__round__(5))
			text = font.render(velocity_text, True, Colors['Blue'])
			textRect.center = (a_position[0] + 10, a_position[1] + 10)
			
			screen.blit(text, textRect)
		# /Velocity text

		pygame.draw.rect(screen, Colors[a_type], pygame.Rect(a_position[0], a_position[1], size_of_blip, size_of_blip))
	
	fps = f'FPS: {simulation_clock.get_fps():05.2f}, Goal: {framerate}'
	text = font.render(fps, True, Colors['Blue'])
	textRect.topleft = (0, 0)
	screen.blit(text, textRect)
	screen.blit(f_text, f_textRect)
	pygame.display.flip()
	print('Time since start: ' + str(t.time() - start))
