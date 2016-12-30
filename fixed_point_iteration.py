import math

class FPI:
    def __init__(self):
        self.range = []
        self.q = []
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

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

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

    def inputdata(self, accuracy):
        self.accuracy = accuracy

    def inputnewdata(self):
        task = 0
        num = 0
        while (task != 1):
            print('')
            print("Input range")
            row = list(map(float, input("-> ").split()))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n" and len(row) == 2):
                task = 1
                self.range = row
            elif (len(row) != num):
                print('')
                print("Incorrect input: count of items.")

    def findroot(self):
        # print(self.problem(self.range[1]))
        i = 0
        while i < 3:
            self.iteration(i)
            i += 1

    def dostaff0(self):
        self.findroot()
        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("LU factorization v0.0002 betta")
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
                print('')
                print("Range")
                print(self.range)
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 9):
                self.makedafault()
                pass
            elif (task == 10):
                self.findroot()
                pass
            elif (task == 11):
                self.inputnewdata()
        pass

    def problem0(self, x):
        # Task 4 v15
        # 2 * x ** 3 - 3 * x ** 2 - 60 * x + 1 = 0
        # x^3 - 1.5x^2 - 30x + 0.5
        # x^2(2x - 3) - (60x + 1) = 0
        # x^2(x - 1.5) - 30(x + 1/60) = 0
        # 3 * x ** 2 + 60 * x - 1 = 0
        # 3x(x + 20) - 1 = 0
        # x = 1/3
        # x = -20

        # 2 * x^3 = 0
        # x = 0

        # (|f`(x)| * |Xk-1 - Xk| / |1 - f`(x)| <= q/(q - 1) * |Xk-1 - Xk|
        print('')
        print("Problem solution")
        print("X is")
        print(x)
        # f = (1.5 * x ** 2 + 30 * x - 0.5) ** (1 / 3)
        f = 1.5 * math.pow(x, 2) + 30 * x - 0.5
        print("Before pow")
        print(f)
        #f = math.pow(1.5 * x ** 2 + 30 * x - 0.5, 1 / 3)
        #f = math.pow(f, round(1.0 / 3.0, self.accuracy))
        if (f < 0 and math.fabs(f) >= 1):
            f = (-f) ** (1.0 / 3)
            f = -f
        elif (f < 0 and math.fabs(f) < 1.5):
            f = math.fabs(f) ** (1.0 / 3)
        else:
            f = f ** (1.0 / 3)
        print("Before round")
        print(f)
        # f1 = 1 / (3 * ((1.5 * x ** 2 + 30 * x - 0.5) ** 2) ** (0.33))
        return round(f, self.accuracy)

    def problem(self, x):
        # Task 4 v15
        # 2 * x ** 3 - 3 * x ** 2 - 60 * x + 1 = 0
        # x^3 - 1.5x^2 - 30x + 0.5
        # x^2(2x - 3) - (60x + 1) = 0
        # x^2(x - 1.5) - 30(x + 1/60) = 0
        # 3 * x ** 2 + 60 * x - 1 = 0
        # 3x(x + 20) - 1 = 0
        # x = 1/3
        # x = -20

        # 2 * x^3 = 0
        # x = 0
        # (|f`(x)| * |Xk-1 - Xk| / |1 - f`(x)| <= q/(q - 1) * |Xk-1 - Xk|
        xr = x
        print('')
        print("Problem solution")
        print("X is")
        print(x)
        # f = (1.5 * x ** 2 + 30 * x - 0.5) ** (1 / 3)
        f = 1.5 * math.pow(x, 2) + 30 * x - 0.5
        print("Before pow")
        print(f)
        sign = math.copysign(1, f)
        #f = math.pow(math.fabs(f), 1 / 3)
        f = math.fabs(f)
        f **= 1 / 3
        if (xr < 0):
            f = math.copysign(f, sign)
        # f = math.pow(1.5 * x ** 2 + 30 * x - 0.5, 1 / 3)
        # f = math.pow(f, round(1.0 / 3.0, self.accuracy))
        print("Before round")
        print(f)
        return round(f, self.accuracy)

    def makedafault(self):
        # self.range = [-4.8, -4.775, 0.015, 0.020, 6.24, 6.32]
        self.range = [-4.8, -4.775, 0, 0.020, 6.24, 6.32]
        # self.q = [4.775, 0.015, 6.32]
        i = 0
        while i < len(self.range):
            self.q.append(self.findmaxfi([self.range[i],self.range[i + 1]]))
            i += 2
        self.accuracy = 3
        pass

    def findmaxfi(self,interval):
        f1 = self.probleml(interval[0])
        f2 = self.probleml(interval[1])
        # f1 = 1 / (3 * ((1.5 * interval[0] ** 2 + 30 * interval[0] - 0.5) ** 2) ** (1 / 3))
        # f2 = 1 / (3 * ((1.5 * interval[1] ** 2 + 30 * interval[1] - 0.5) ** 2) ** (1 / 3))
        if (f1 > f2):
            return f1
        else:
            return f2

    def probleml(self,x):
        f = 1 / (3 * ((1.5 * x ** 2 + 30 * x - 0.5) ** 2) ** (1 / 3))
        return f

    def probleml0(self, x):
        f = 1 / (1 / math.pow(x, 3) - 30 / math.pow(x, 2))
        return f

    def stopfpi(self,x,xold,q):
        # f1 = round((math.fabs(self.probleml(x)) * math.fabs(xold - x)) / math.fabs(1 - self.probleml(x)), self.accuracy)
        # f2 = round((q / (q - 1)) * math.fabs(xold - x), self.accuracy)
        f1 = math.fabs(self.probleml(x)) * math.fabs(xold - x) / math.fabs(1 - self.probleml(x))
        f2 = (q / (q - 1)) * math.fabs(xold - x)
        if (f1 <= f2):
            return True
        else:
            return False

    def iteration(self, i):
        task = False
        k = i * 2
        # 0 - 1 2 - 3 4 - 5
        # xold = round((self.range[k] - self.range[k + 1]) / self.accuracy, self.accuracy)
        if (math.fabs(self.range[k]) > 1):
            xold = self.range[k] + 0.02
        else:
            xold = self.range[k] + 0.0002
        x = 0
        while (task == False):
            print("Previous step is:",xold)
            x = self.problem(xold)
            print("Result is:",x)
            task = self.stopfpi(x, xold, self.q[i])
            xold = x
            print('')
            print("Iteration result")
            print(x)
        print('')
        print("Final result is")
        print(x)