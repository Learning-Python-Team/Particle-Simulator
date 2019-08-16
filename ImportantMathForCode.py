# All masses are in kilograms

mass_modifier = 27
particle_mass = {
	'p': float(1.6726219 * (10 ** (-27 + mass_modifier))),
	'e': float(9.10938356 * (10 ** (-31 + mass_modifier))),
	'n': float(1.674927471 * (10 ** (-27 + mass_modifier)))
	}

constant_G = 6.674 * (10 ** -11) * 100_000_000  # m^3 * kg^-1 * s^-2
constant_coulombs_constant = 8987551787.3681764  # N * m^2 * C^-2
