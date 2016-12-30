import math
import matrix

class SRM:
    def __init__(self,arg):
        self.am = matrix.Matrix(arg, "Initial matrix")
        self.um = matrix.Matrix(arg, "Umatrix")
        self.ut = matrix.Matrix([], "Lmatrix")
        self.dm = matrix.Matrix([],"Dmatrix")
        pass
