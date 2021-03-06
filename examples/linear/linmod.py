# Copyright (C) 2014-2018 Catherine Beauchemin <cbeau@users.sourceforge.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# =============================================================================
#
#                                   Utilities
#
# =============================================================================
#
import numpy
import phymcmc


class params(phymcmc.ParamStruct):
	def validate(self):
		""" Assess validity of model parameters. """
		if min(self.pardict.values()) < 0.0:
			raise ValueError(repr(self.pardict))


class line(phymcmc.base_model):
	def get_solution(self):
		""" Solve the model and obtain the model-generated data prediction. """
		return self.par['slope']*self.data[:,0]+self.par['yint']
	def get_normalized_ssr(self,pvec):
		""" Computes total normalized SSR, i.e. SSR/stdev. """
		try:
			self.params.vector = pvec
		except ValueError:
			return float('inf')
		self.par = self.params.pardict
		# Here SSR is not normalized by standard dev of residuals but should be
		# (see example baccam to see what I mean)
		return numpy.sum( (self.data[:,1] - self.get_solution())**2.0 )
