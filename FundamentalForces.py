# Equations used in ParticleSimulator_2D.py
from Settings import *
import math as m


def calculate_gravity(forces_list, a_pos, a_mass, b_pos, b_mass):
	bypass = True
	if bypass is False:
		x_diff = b_pos[0] - a_pos[0]
		y_diff = b_pos[1] - a_pos[1]
		hypotenuse = m.sqrt((x_diff ** 2) + (y_diff ** 2))
		sin = x_diff / hypotenuse
		cos = y_diff / hypotenuse
		
		f = (constant_G * a_mass * b_mass) / (hypotenuse ** 2)
		
		forces_list[0] += f * sin
		forces_list[1] += f * cos
		
		return forces_list
	else:
		return forces_list


def calculate_electromagnetic(forces_list, a_pos, b_pos, a_mass, b_mass, a_type, b_type):
	fx, fy = forces_list
	
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

# def calculate_strong(forces_list, )
