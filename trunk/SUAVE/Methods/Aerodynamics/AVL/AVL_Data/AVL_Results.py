# AVL_Results.py
# Tim Momose, January 2015

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
from SUAVE.Structure import Data

# ------------------------------------------------------------
#   Wing
# ------------------------------------------------------------

class AVL_Results(Data):
    def __defaults__(self):
    	
    	self.aerodynamics = Data()
    	self.stability    = Data()
    	
    	self.stability.alpha_derivatives = Data()
    	self.stability.beta_derivatives  = Data()