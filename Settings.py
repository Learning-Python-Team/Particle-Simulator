# Settings

number_of_bodies = 10
size_of_window = 700, 700

modifier_10 = 17
modifier_slow_velocity = 0

particle_mass = {
	'p': float(1.6726219 * (10 ** (-27 + modifier_10))),
	'e': float(9.10938356 * (10 ** (-31 + modifier_10))),
	'n': float(1.674927471 * (10 ** (-27 + modifier_10)))
	}
constant_G = 6.674 * (10 ** (-11 + modifier_10))  # m^3 * kg^-1 * s^-2
constant_coulombs_constant = 8987551787.3681764  # N * m^2 * C^-2
