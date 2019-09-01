# Settings

number_of_bodies = 10
size_of_window = 300, 300
auto_make_particles = True
possible_particle_type = ('p', 'e', 'n')
Autoslowdown = {
	'Slow': False,
	'SlowFactor': 10
	}

modifier_scale = 4.5e12
modifier_slow_velocity = 0

particle_mass = {
	'p': float(1.6726219 * (10 ** (-27)) * modifier_scale),
	'e': float(9.10938356 * (10 ** (-31)) * modifier_scale),
	'n': float(1.674927471 * (10 ** (-27)) * modifier_scale)
	}
constant_G = 6.674e-11 * modifier_scale  # m^3 * kg^-1 * s^-2
constant_coulombs_constant = (8.9875517873681764e9) * modifier_scale  # N * m^2 * C^-2
