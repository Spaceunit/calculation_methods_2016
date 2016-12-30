import math
import matrix


class Lmatrix:
    def __init__(self,arg):
        self.matrix = matrix.Matrix(arg,"Lmatrix")
        pass

    def setraw(self,raw,um):
        self.matrix.matrix.append([])
        for item in range(0, raw):
            self.matrix.matrix[raw].append(um.matrix.matrix[raw][item])
            um.matrix.matrix[raw][item] = 0

    def rawzero(self, start, um):
        for i in range(start + 1, um.matrix.len):
            self.matrix.matrix[start].append(0)

class Umatrix:
    def __init__(self,arg):
        self.matrix = matrix.Matrix(arg,"Umatrix")
        pass

    def createumatrix(self):
        lmatrix = Lmatrix([[1]])
        lmatrix.rawzero(0,self)
        self.numberconversion(0)
        for raw in range(1,self.matrix.len):
            self.rawsubtract(raw)
            lmatrix.setraw(raw,self)
            lmatrix.rawzero(raw, self)
            self.numberconversion(raw)
        return lmatrix

    def rawzero(self,start,lmatrix):
        for i in range(start + 1, self.matrix.len):
            lmatrix[start].append(0)

    def rawsubtract(self,raw):
        print("rawsubtract")
        print("raw: ",raw)
        for i in range(raw, self.matrix.len):
            self.matrix.matrix[raw][i] -= self.matrix.matrix[raw][raw - 1] * self.matrix.matrix[raw - 1][i]
            self.matrix.showmatrix()
        print("rawsubtract end")

    def newrawsubtract(self,raw):
        print("rawsubtract")
        print("raw: ", raw)
        for rawk in range(raw, self.matrix.len):
            for i in range(rawk, self.matrix.len):
                self.matrix.matrix[raw][i] -= self.matrix.matrix[raw][raw - 1] * self.matrix.matrix[raw - 1][i]
                self.matrix.showmatrix()
        print("rawsubtract end")


    def numberconversion(self,raw):
        print("numberconversion")
        print("raw: ",raw)
        a = self.matrix.matrix[raw][raw]
        for item in range(raw, self.matrix.len):
            self.matrix.matrix[raw][item] /= a
            self.matrix.showmatrix()
        print("numberconversion end")

class LU:
    def __init__(self,arg):
        umatrix = Umatrix(arg)
        #lmatrix = Lmatrix(umatrix.)
        pass