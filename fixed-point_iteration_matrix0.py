import math
import matrix


class FPIM:
    def __init__(self):
        self.am = matrix.Matrix([],"Initial matrix")
        self.commands = {
            "none": 0,
            "exit": 1,
            "test": 2,
            "clear": 3,
            "help": 4,
            "new": 5,
            "show slist": 6,
            "show scount": 7,
            "makei": 8,
            "showi": 9,
            "start": 10,
            "old": 11
        }
        pass

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
                    task = 1
            task = 0
            self.am.rename("Initial matrix")
            self.am.showmatrix()
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
        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("LU factorization v0.0002 betta")
            print('')
            task = self.enterCommand()
            if (task == 2):
                #self.dostaff()
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                self.am.showmatrix()
                pass
            elif (task == 10):
                self.resolve()
                print("Result:")
                print("result")
                pass
            elif (task == 11):
                self.inputnewdata()
        pass