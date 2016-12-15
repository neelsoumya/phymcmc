from distutils.core import setup

setup(
	name = 'phymcmc',
	version = '0.1',
	author = 'Catherine Beauchemin',
	author_email = 'cbeau@users.sourceforge.net',
	description = 'The phymbie fitting/mcmc library.',
	url = 'http://phymbie.physics.ryerson.ca',
	license = 'See file LICENSE',
	packages = [
		'phymcmc',
		'phymcmc.emcee'
	],
	scripts = [
		'bin/phymcmc_diagnostics',
		'bin/phymcmc_fix_fracaccept',
		'bin/phymcmc_parstats',
		'bin/phymcmc_rmderived'
	],
	package_dir = {'phymcmc':'lib'}
)
