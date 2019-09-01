# Equations used in ParticleSimulator_2D.py
from Settings import *
import math as m


def calculate_gravity(a_pos, a_type, b_pos, b_type):
	x_diff = b_pos[0] - a_pos[0]
	y_diff = b_pos[1] - a_pos[1]
	hypotenuse = m.sqrt((x_diff ** 2) + (y_diff ** 2))
	sin = x_diff / hypotenuse
	cos = y_diff / hypotenuse
	a_mass = particle_mass[a_type]
	b_mass = particle_mass[b_type]
	
	f = (constant_G * a_mass * b_mass) / (hypotenuse ** 2)
	
	fx = f * sin
	fy = f * cos
	
	return fx, fy


def calculate_electromagnetic(a_pos, a_type, b_pos, b_type):
	if a_type or b_type == 'n':
		return [0, 0]
	
	x_diff = b_pos[0] - a_pos[0]
	y_diff = b_pos[1] - a_pos[1]
	hypotenuse = m.sqrt((x_diff ** 2) + (y_diff ** 2))
	sin = x_diff / hypotenuse
	cos = y_diff / hypotenuse
	
	a_mass = particle_mass[a_type]
	b_mass = particle_mass[b_type]
	
	f = (constant_coulombs_constant * a_mass * b_mass) / (hypotenuse ** 2)
	
	if a_type == b_type:
		fx = (f * sin) * -1
		fy = (f * cos) * -1
	else:
		fx = (f * sin)
		fy = (f * cos)
	return fx, fy

# def calculate_strong(forces_list, )
