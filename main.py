import openpyxl
import matrix
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import newLU
import inverse_matrix
import fixed_point_iteration_matrix
import Givens_rotation
import fixed_point_iteration

class Work:
    def __init__(self):
        self.a = matrix.Matrix([[0]],"Initial matrix")
        self.accuracy = 2
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
            "lu":   10,
            "inv":  11,
            "fpim": 12,
            "rm":   13,
            "fpi":  14

        }
        pass

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

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

    def showHelp(self):
        print('')
        print("Help v0.001")
        print("Author of this program: Sir Oleksiy Polshchak")
        self.showCommands()

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Matrix calculation v0.0002 betta task #15")
            print('')
            task = self.enterCommand()
            if (task == 2):
                self.dostaff()
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                self.a.showmatrix()
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 10):
                Task1 = newLU.LU()
                Task1.inputdata(self.a,self.accuracy)
                Task1.dostaff()
                pass
            elif (task == 9):
                self.makedafault()
                pass
            elif (task == 11):
                Task2 = inverse_matrix.IM()
                Task2.inputdata(self.a,self.accuracy)
                Task2.dostaff()
                pass
            elif (task == 12):
                Task3a = fixed_point_iteration_matrix.FPIM()
                Task3a.inputdata(self.accuracy)
                Task3a.dostaff()
                pass
            elif (task == 13):
                Task3b = Givens_rotation.GR()
                Task3b.inputdata(self.accuracy)
                Task3b.dostaff()
            elif (task == 14):
                Task4 = fixed_point_iteration.FPI()
                Task4.inputdata(self.accuracy)
                Task4.dostaff()
        pass

    def inputnewdata(self):
        task = 0
        self.a = matrix.Matrix([], "Initial matrix")
        while (task != 1):
            print('')
            print("Enter matrix dimension:")
            while (task != 1):
                num = int(input("-> "))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n"):
                    self.a = self.inputmatrix(num)
                    task = 1
            task = 0
            self.a.rename("Initial matrix")
            self.a.showmatrix()
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
        self.a = matrix.Matrix([[3.81, 0.25, 1.28, 1.75],
                                [2.25, 1.32, 5.58, 0.49],
                                [5.31, 7.28, 0.98, 1.04],
                                [10.39, 2.45, 3.35, 2.28]],
                               "Initial matrix")


Some = Work()
Some.dostaff()
