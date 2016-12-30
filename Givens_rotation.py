import math
import matrix

class GR:
    def __init__(self):
        self.am = matrix.Matrix([], "Initial matrix")
        self.qm = matrix.Matrix([], "Q-matrix")
        self.rm = matrix.Matrix([], "R-matrix")
        self.gm = matrix.Matrix([], "G-matrix")
        self.um = matrix.Matrix([], "U-matrix")
        self.dv = matrix.Vector([], "Vector B")
        self.commands = {
            "none": 0,
            "exit": 1,
            "test": 2,
            "clear": 3,
            "help": 4,
            "new": 5,
            "show slist": 6,
            "show scount": 7,
            "acc": 8,
            "mk": 9,
            "start": 10,
            "old": 11
        }

    def inputdata(self, accuracy):
        self.accuracy = accuracy

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

    def enterCommand(self):
        command = "0"
        print('')
        print("Enter command (help for Q&A)")
        while (command not in self.commands):
            command = input("->")
            if (command not in self.commands):
                print("There is no such command")
            else:
                return self.commands[command]

    def showHelp(self):
        print('')
        print("Help v0.001")
        self.showCommands()

    def inputnewdata(self):
        task = 0
        self.am = matrix.Matrix([], "Initial matrix")
        while (task != 1):
            print('')
            print("Enter matrix dimension:")
            while (task != 1):
                num = int(input("-> "))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n"):
                    self.am = self.inputmatrix(num)
                    self.dv = self.inputvector()
                    task = 1
            task = 0
            self.am.rename("Initial matrix")
            self.um = self.am.copy()
            self.am.showmatrix()
            self.dv.showvector()
            print("Matrix is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1

    def inputmatrix(self, num):
        print('')
        i = 0
        task = 0
        nm = matrix.Matrix([], "new matrix")
        while (i < num):
            print("Enter matrix row (use spaces)")
            print("Row ", i + 1)
            while (task != 1):
                row = list(map(float, input("-> ").split()))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n" and len(row) == num):
                    task = 1
                    nm.appendnraw(row)
                elif (len(row) != num):
                    print('')
                    print("Incorrect input: count of items.")
            task = 0
            i += 1
        return nm

    def inputvector(self):
        print('')
        i = 0
        task = 0
        num = self.am.len[0]
        print("Enter vector row (use spaces)")
        print("Row")
        while (task != 1):
            row = list(map(float, input("-> ").split()))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n" and len(row) == num):
                task = 1
                nm = matrix.Vector(row, "new vector")
            elif (len(row) != num):
                print('')
                print("Incorrect input: count of items.")
        return nm

    def setbettavector(self):
        self.btv = matrix.Vector([], "Betta-vector")
        for i in range(0, self.dv.len):
            self.btv.appendel(self.dv.getel(i) / self.am.getel(i, i))

    def somedata(self):
        self.am = matrix.Matrix([[10, 2, -1],
                                 [-2, -6, -1],
                                 [1, -3, 12]],
                                "Initial matrix")

        self.dv = matrix.Vector([5, 24.42, 36], "Vector B")

    def makedafault(self):
        self.am = matrix.Matrix([[6.010, 2.210, 1.210],
                                 [2.210, 5.860, -1.510],
                                 [1.210, -1.510, 5.130]],
                                "Initial matrix")
        self.dv = matrix.Vector([15.09, 11.00, 15.11], "Vector B")

    def setaccuracy(self):
        task = 0
        print('')
        print("Enter accuracy:")
        while (task != 1):
            self.accuracy = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1
        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Rotation method for matrix v0.0002 betta")
            print('')
            task = self.enterCommand()
            if (task == 2):
                self.somedata()
                pass
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                self.am.showmatrix()
                self.dv.showvector()
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 9):
                self.makedafault()
                pass
            elif (task == 10):
                self.resolve()
                pass
            elif (task == 11):
                self.inputnewdata()
        pass

    def resolve(self):
        self.am.showmatrix()
        self.um = self.am.copy()
        self.um.rename("U-matrix")
        self.umrotation()
        pass

    def takeqmatrix(self):
        # x1=β1 - α12x2 - α13x3 - ... - α1nxn
        # x2=β2 - α21x1 - α23x3 - ... - α2nxn
        # xn=βn - αn1xn - αn3x3 - ... - αnn-1xn-1
        # where βi=bi/aii; αij=aij/aii and i ≠ j; αii=0
        # x=β - αx
        # x0 = β
        # x1=b - a x0
        # x2=b - a x1
        # ....
        # xk+1=b - a xk
        self.setbettavector()
        self.btv.showvector()
        self.qm = self.am.copy()
        self.qm.rename("Q-matrix")
        for i in range(0, self.qm.len[0]):
            num = self.qm.getel(i, i)
            self.qm.chel(i, i, 0)
            for j in range(0, self.qm.len[1]):
                if (i != j):
                    self.qm.chel(i, j, round(self.qm.getel(i, j) / num, self.accuracy))
        self.qm.showmatrix()
        self.x = self.btv.copy()
        self.x.rename("X-vector")
        self.xn = self.x.copy()
        print(self.xn.vector)
        i = 0
        print('')
        while True:
            i += 1
            self.xn = self.btv.rawsubtract(self.qm.matrixmv(self.x, self.accuracy), self.accuracy)
            print("#", i, self.displayvh(self.xn))
            print('')
            if (self.xn.compare(self.x, self.accuracy) or i >= 100):
                break
            self.x.setvector(self.xn.vector)
        pass

    def displayvh(self, V):
        s = ""
        for i in range(0, V.len):
            if (V.getel(i) < 0):
                s += " " + str(round(V.getel(i), self.accuracy))
            else:
                s += "  " + str(round(V.getel(i), self.accuracy))
        return s

    def makec(self, i, k):
        c = self.um.getel(i, i) / math.sqrt(math.pow(self.um.getel(i, i), 2) + math.pow(self.um.getel(k, i), 2))
        return c
        pass

    def makes(self, i, k):
        s = self.um.getel(k, i) / math.sqrt(math.pow(self.um.getel(i, i), 2) + math.pow(self.um.getel(k, i), 2))
        return s
        pass

    def umrotation(self):
        print("Rotation step ----->")
        rawb = self.dv.copy()
        rawb.rename("Vector B")
        for i in range(0, self.um.len[0]):
            for k in range(i + 1, self.um.len[0]):
                c = self.makec(i, k)
                s = self.makes(i, k)
                raw = self.um.getrow(i)
                #step 1
                b = rawb.getel(i)
                v1 = self.um.getrow(i)
                v2 = self.um.getrow(k)
                v1.mnumber(c, self.accuracy)
                v2.mnumber(s, self.accuracy)
                self.um.setrowm(i, v1.rowsummarize(v2, self.accuracy))
                rawb.chel(i, round(rawb.getel(i) * c + rawb.getel(k) * s, self.accuracy))
                #step 2
                v1 = raw.copy()
                v2 = self.um.getrow(k)
                v1.mnumber(-s, self.accuracy)
                v2.mnumber(c, self.accuracy)
                self.um.setrowm(k, v1.rowsummarize(v2, self.accuracy))
                rawb.chel(k, round(b * -s + rawb.getel(k) * c, self.accuracy))
            print("Step #", i + 1)
            self.um.showmatrix()
            rawb.showvector()
        self.um.showmatrix()
        rawb.showvector()
        self.um.join(rawb.tomatrix(self.accuracy))
        self.um.rowdnumber(0, self.um.getel(0, 0), self.accuracy)
        for i in range(1, self.um.len[0]):
            num = self.um.getel(i, i)
            for j in range(i, self.um.len[1]):
                self.um.chel(i, j, round(self.um.getel(i, j) / num, self.accuracy))
        self.um.showmatrix()
        print("End of rotation step <-----")
        print("Back step ----->")
        i = self.um.len[0]
        while (i > 0):
            i -= 1
            k = i - 1
            e = k
            while (not k < 0):
                j = self.um.len[1] - 1
                print("Step #",self.um.len[0] - i, "Do: R", k + 1, "- R", i + 1, "* R(", k + 1, ",", i + 1, ")")
                while (j > e):
                    self.um.chel(k, j, round(self.um.getel(k, j) - self.um.getel(i, j) * self.um.getel(k, i), self.accuracy))
                    self.um.showmatrix()
                    j -= 1
                k -= 1
        print("End of back step <-----")
        print(' ')
        print("End of calculation")
        self.um.showmatrix()
        self.result = self.um.getcol(self.um.len[1] - 1)
        self.result.rename("Result")
        self.result.showvector()
        pass