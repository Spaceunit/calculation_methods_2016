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

    def problem(self, x, i):
        f = x - (2 * math.pow(x, 3) - 3 * math.pow(x, 2) - 60 * x + 1) / self.q[i]
        return f

    def makedafault(self):
        # self.range = [-4.8, -4.775, 0.015, 0.020, 6.24, 6.32]
        self.range = [-4.8, -4.775, 0, 0.020, 6.24, 6.32]
        # self.q = [4.775, 0.015, 6.32]
        self.M = []
        i = 0
        while i < len(self.range):
            self.q.append(self.findmaxfi([self.range[i],self.range[i + 1]]))
            i += 2
        self.accuracy = 3
        pass

    def findmaxfi(self,interval):
        f1 = self.probleml(interval[0])
        f2 = self.probleml(interval[1])
        if (f1 > f2):
            return f1
        else:
            return f2

    def probleml(self,x):
        f = 1 / (3 * ((1.5 * x ** 2 + 30 * x - 0.5) ** 2) ** (1 / 3))
        return f

    def stopfpi(self,x,xold,q):
        pass

    def iteration(self, i):
        pass