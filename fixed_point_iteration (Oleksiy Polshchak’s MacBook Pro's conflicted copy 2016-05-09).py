import math

class FPI:
    def __init__(self):
        self.range = []
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
        i = 10
        while (i > -10):
            print(self.problem(i))
            i -= 0.125
        pass

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

    def problem(self, x):
        # Task 4 v15
        # 2 * x ** 3 - 3 * x ** 2 - 60 * x + 1 = 0
        f = ((3 * x ** 2 + 60 * x - 1)/2) ** (1/3)
        
        # return round(f, self.accuracy)
        return f

    def makedafault(self):
        self.range = [-1, 1]
        self.accuracy = 3
        pass