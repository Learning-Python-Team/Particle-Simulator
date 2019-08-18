# Equations used in ParticleSimulator_2D.py
from Settings import *


def calculate_gravity(a_pos, a_mass, b_pos, b_mass):
	x_diff = b_pos[0] - a_pos[0]
	y_diff = b_pos[1] - a_pos[1]
	hypotenuse = m.sqrt((x_diff ** 2) + (y_diff ** 2))
	sin = x_diff / hypotenuse
	cos = y_diff / hypotenuse
	
	f = (constant_G * a_mass * b_mass) / (hypotenuse ** 2)
	
	fx = f * sin
	fy = f * cos
	
	return [fx, fy]


def calculate_electromagnetic(forces_list, a_pos, b_pos, a_mass, b_mass, a_type, b_type):
	fx, fy = forces_list
	if a_type or b_type == 'n':
		return forces_list
	
	x_diff = b_pos[0] - a_pos[0]
	y_diff = b_pos[1] - a_pos[1]
	hypotenuse = m.sqrt((x_diff ** 2) + (y_diff ** 2))
	sin = x_diff / hypotenuse
	cos = y_diff / hypotenuse
	
	f = (constant_coulombs_constant * a_mass * b_mass) / (hypotenuse ** 2)
	
	if a_type == b_type:
		fx -= (f * sin)
		fy -= (f * cos)
	else:
		fx += (f * sin)
		fy += (f * cos)
	return forces_list
