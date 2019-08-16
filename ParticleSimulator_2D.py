# This file will be a particle simulator on a two dimensional scale.
# This file is based on
# https://github.com/anishsatalkar/python_gravity_simulation_pygame/blob/master/gravity_simulation.py


import random
import time
import math
import numpy
import sys
import pygame
from Particle_masses import *

number_of_bodies = 5
size_of_window = [100, 100]

Colors = {
	'White': (255, 255, 255),
	'Black': (0, 0, 0),
	'Blue': (109, 196, 255),
	}  # (Red, Green, Blue) color values from 0 to 255


class Particle:
	def __init__(self, particle_type, position, acceleration, velocity):
		self.type = particle_type  # This determines what kind of particle it is; one of three is the input 'p', 'n', 'e'
		self.position = position  # The position is a list [x, y]; position is measured in pixels
		self.acceleration = acceleration  # Acceleration is a list [x, y] measured in pixels
		self.velocity = velocity  # Same as Acceleration, but the actual velocity component
		
		p_type_string = str(particle_type)
		self.mass = particle_mass[p_type_string]


def calculate_forces_between_p_and_n():
	return None  # temp


def calculate_forces_between_p_and_e():
	return None  # Temp


def calculate_forces_between_e_and_n():
	return None


posible_particle_type = ('p', 'e', 'n')

particles = []
for i in range(number_of_bodies):
	particle_type_int = random.randint(-1, 2)
	particle_type = str(posible_particle_type[particle_type_int])
	pos_x = random.randint(4, (size_of_window[0] - 5))
	pos_y = random.randint(4, (size_of_window[1] - 5))
	
	particles.append(Particle(particle_type, [pos_x, pos_y], [0, 0], [0, 0]))
