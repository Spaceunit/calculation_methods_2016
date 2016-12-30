import math
import matrix
import inverse_matrix


class FPIM:
    def __init__(self):
        self.am = matrix.Matrix([], "Initial matrix")
        self.dm = matrix.Matrix([], "Initial matrix")
        self.dpm = matrix.Matrix([], "DPM")
        self.dv = matrix.Vector([], "Vector B")
        self.accuracy = 3
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
        pass

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

    def resolve(self):
        # Task2 = inverse_matrix.IM()
        # Task2.inputdata(self.am, self.accuracy)
        # Task2.inversematrix()
        # self.dm = Task2.aim
        # self.dm = self.am.copy()
        # self.dm.transpose()
        # self.dpm = self.am.matrixm(self.dm, self.accuracy)
        # print('dpm')
        # self.dpm.showmatrix()
        self.takeqmatrix()

        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Fixed point iteration for matrix v0.0002 betta")
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
                print("Result:")
                print("result")
                pass
            elif (task == 11):
                self.inputnewdata()
        pass

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

    def makedafault(self):
        self.am = matrix.Matrix([[6.010, 2.210, 1.210],
                                 [2.210, 5.860, -1.510],
                                 [1.210, -1.510, 5.130]],
                                "Initial matrix")
        self.dv = matrix.Vector([15.09, 11.00, 15.11], "Vector B")

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

    def takeqmatrix0(self):
        # Ax = b -> x= Qx + c
        # Q = E - D*A, c = D*b

        Task2 = inverse_matrix.IM()
        Task2.inputdata(self.am, self.accuracy)
        Task2.inversematrix()
        D = Task2.aim
        E = matrix.Matrix([],"E-matrix")
        E.makedimatrix(self.am.len[0])
        R = D.matrixm(self.am, self.accuracy)
        self.qm = E.matrixsubtract(R, R.len[0])
        self.qm.rename("Q-matrix")
        self.cv = D.matrixmv(self.dv, self.accuracy)
        self.cv.rename("C-vector")
        self.qm.showmatrix()
        self.cv.showvector()
        pass

    def setbettavector(self):
        self.btv = matrix.Vector([],"Betta-vector")
        for i in range(0, self.dv.len):
            self.btv.appendel(self.dv.getel(i)/self.am.getel(i,i))

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
            #print(self.qm.matrixmv(self.x, self.accuracy).showvector())
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

    def somedata(self):
        self.am = matrix.Matrix([[10, 2, -1],
                                 [-2, -6, -1],
                                 [1, -3, 12]],
                                "Initial matrix")

        self.dv = matrix.Vector([5, 24.42, 36], "Vector B")
