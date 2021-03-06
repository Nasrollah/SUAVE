# Constants.py: Physical constants and helepr functions
# 
# Created By:       J. Sinsay
# Updated:          M. Colonno   04/09/2013
#                   T. Lukaczyk  06/23/2013

""" SUAVE Data Class for Constants """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# initialized constants
from Constant import Constant

# ----------------------------------------------------------------------
#  Constants 
# ----------------------------------------------------------------------

class Universe(Constant):
    """ Universal constants """
    def __defaults__(self):
        self.c     = 2.99792458e8 # m/s, speed of light in a vacuum
        self.G     = 6.67384e-11  # N-m^2/kg^2, gravitational constant in flat space
        self.N     = 6.023e23     # per mol, Avagandro's number
        self.e0    = 8.8e-12      # F/m, electric permittivity in a vacuum
        self.mew0  = 1.26e-6      # H/m, permeability of a vacuum 
        self.h     = 6.63e-34     # J-s, Plank constant 
        self.k     = 1.38e-23     # J/K, Boltzmann constant
        self.e     = 1.60e-19     # C, charge of an electron
        self.me    = 9.11e-31     # kg, electron mass
        self.mp    = 1.67e-27     # kg, proton mass
        self.R     = 8314.32      # N-m/(kmol-K), universal gas constant
        
        # todo: use unit converter
        #self.AbsoluteZeroInC = -273.15  # deg C, absolute zero in C     #
        #self.ZeroCInK        = 273.15   # deg K, zero in C  

