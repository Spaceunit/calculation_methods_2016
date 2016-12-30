import math
import matrix


class IM:

    def __init__(self):
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
            "start": 10,
            "old": 11
        }
        pass

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

    def showHelp(self):
        print('')
        print("Help v0.001")
        self.showCommands()

    def showSourcelist(self):
        k = 0
        print('')
        print("Sourcelist...")
        self.am.showmatrix()

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

    def inputdata(self,arg,accuracy):
        self.accuracy = accuracy
        self.am = arg.copy()
        self.am.rename("Initial matrix")
        self.im = self.am.copy()
        self.im.rename("Initial and identity matrix")
        i = matrix.Matrix([], "Identity matrix")
        i.makedimatrix(self.am.len[0])
        self.im.join(i)
        self.aim = matrix.Matrix([], "Inverse matrix")
        pass

    def inputnewdata(self):
        task = 0
        self.am = matrix.Matrix([],"Initial matrix")
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
        self.im = self.am.copy()
        self.im.rename("Initial and identity matrix")
        i = matrix.Matrix([], "Identity matrix")
        i.makedimatrix(self.am.len[0])
        self.im.join(i)
        self.aim = matrix.Matrix([], "Inverse matrix")

    def inputmatrix(self,num):
        print('')
        i = 0
        task = 0
        nm = matrix.Matrix([],"new matrix")
        while (i < num):
            print("Enter matrix row (use spaces)")
            print("Row ",i + 1)
            while (task !=1 ):
                row = list(map(float, input("-> ").split()))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n" and len(row) == num):
                    task = 1
                    nm.appendnraw(row)
                elif(len(row) != num):
                    print('')
                    print("Incorrect input: count of items.")
            task = 0
            i += 1
        return nm




    def numberconversion(self, raw):
        print('')
        print("Number conversion...")
        num = self.im.getel(raw, raw)
        p = raw + 1
        print("R[", p, "]/R(", p, ",", p, ") where R(", p, ",", p, ") =", num, ";")
        print("Step #", raw + 1)
        for i in range(raw, self.im.len[1]):
            self.im.chel(raw, i, round(self.im.getel(raw, i) / num, self.accuracy))
        self.im.showmatrix()
        print('End of number conversion')
        pass

    def rawsubtract(self, raw):
        print('')
        print("Row subtract...")
        print("Step#", raw + 1, ";")
        for k in range(raw + 1, self.im.len[0]):
            print("R", k + 1, "- R", k, "*", "R(", k + 1, ",", raw + 1, ")")
            if math.copysign(1, self.im.getel(raw, raw)) == math.copysign(1, self.im.getel(k, raw)):
                #self.lm.chel(k, raw, self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = round(self.im.getel(k, raw) / self.im.getel(raw, raw), self.accuracy)
                pass
            else:
                #self.lm.chel(k, raw, -1 * self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = round(self.im.getel(k, raw) / self.im.getel(raw, raw), self.accuracy)
                pass
            # self.lm.chel(k,raw,self.um.getel(k,raw) / self.um.getel(raw,raw))
            # self.lm.chel(k,raw,self.um.getel(k,raw))
            self.im.chel(k, raw, 0)
            for j in range(raw + 1, self.im.len[1]):
                #print("Step #", j + 1)
                self.im.chel(k, j, round(self.im.getel(k, j) - self.im.getel(raw, j) * num, self.accuracy))
                pass
            self.im.showmatrix()
        print('End of raw subtract')
        pass

    def reversal0(self,raw):
        print('')
        print("Reversal...")
        rawr = -(raw + 1)
        intervali = list(range(-self.im.len[0],rawr))
        intervalj = list(range(-self.im.len[1]+(self.im.len[1] - raw - 4),0))
        intervali = intervali[::-1]
        intervalj = intervalj[::-1]
        print(intervali)
        print(intervalj)
        if (len(intervali)!=0):
            intervali.pop(0)

        #intervalj.pop(0)
        print("R", rawr, ";")
        for k in intervali:
            print("R", k, "- R", k, "*", "R", k, "[i,i - 1]")
            if math.copysign(1, self.im.getel(rawr, rawr)) == math.copysign(1, self.im.getel(k, rawr)):
                # self.lm.chel(k, raw, self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = self.im.getel(k, rawr - self.am.len[0])
                #-1
                pass
            else:
                # self.lm.chel(k, raw, -1 * self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = -1 * self.im.getel(k, rawr - self.am.len[0])
                pass
            # self.lm.chel(k,raw,self.um.getel(k,raw) / self.um.getel(raw,raw))
            # self.lm.chel(k,raw,self.um.getel(k,raw))
            self.im.chel(k, rawr, 0)
            for j in intervalj:
                print("Step #", j + 1)
                print("k:",k,"j:",j,"rawr:",rawr)
                print("Do:", self.im.getel(k, j), self.im.getel(rawr, j), num)
                self.im.chel(k, j, self.im.getel(k, j) - self.im.getel(rawr, j) * num)
                print("Result of subtraction: ",self.im.getel(k, j))
                self.im.showmatrix()
                pass
        #while (k  self.im.len[0]):

        print('End of reversal')
        pass

    def reversal1(self, raw):
        print('')
        print("Reversal...")
        rawr = -(raw + 1)
        intervali = list(range(-self.im.len[0], rawr))
        intervalj = list(range(-self.im.len[1] + (self.im.len[1] - raw - self.am.len[1]), 0))
        intervali = intervali[::-1]
        intervalj = intervalj[::-1]
        print(intervali)
        print(intervalj)
        #if (len(intervali) > 1):
            #intervali.pop(0)

        # intervalj.pop(0)
        print("R", rawr, ";")
        k= rawr - 1
        while k >= -self.im.len[0]:
            print("R", rawr + self.im.len[0], "- R",rawr + self.im.len[0] + 1, "*", "R", rawr + self.im.len[0], "[", k + self.im.len[0] + 1,",", k + self.im.len[0] + 2, "]")
            #if math.copysign(1, self.im.getel(rawr, rawr)) == math.copysign(1, self.im.getel(k, rawr)):
            print("test")
            print(rawr - self.am.len[0])
            print(self.im.getel(k, rawr - self.am.len[0]))
            if math.copysign(1, self.im.getel(k, rawr - self.am.len[0])) > 0:
                # self.lm.chel(k, raw, self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = self.im.getel(k, rawr - self.am.len[0])
                # -1
                pass
            else:
                # self.lm.chel(k, raw, -1 * self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = self.im.getel(k, rawr - self.am.len[0])
                pass
            # self.lm.chel(k,raw,self.um.getel(k,raw) / self.um.getel(raw,raw))
            # self.lm.chel(k,raw,self.um.getel(k,raw))
            self.im.chel(k, rawr - self.am.len[0], 0)
            j = -1
            while j >= intervalj[-1]:
                print("Step #", j)
                print("k:", k, "j:", j, "rawr:", rawr)
                print("Do:", self.im.getel(k, j),"-", self.im.getel(rawr, j),"*", num)
                self.im.chel(k, j, round(self.im.getel(k, j) - self.im.getel(rawr, j) * num, self.accuracy))
                print("Result of subtraction: ", self.im.getel(k, j))
                self.im.showmatrix()
                j-=1
                pass
            k -= 1
        #while (k  self.im.len[0]):

        print('End of reversal')
        pass

    def reversal(self):
        print("Back step ----->")
        i = self.im.len[0]
        while (i > 0):
            i -= 1
            k = i - 1
            e = k
            while (not k < 0):
                j = self.im.len[1] - 1
                print("Step #", self.im.len[0] - i, "Do: R", k + 1, "- R", i + 1, "* R(", k + 1, ",", i + 1, ")")
                while (j > e):
                    self.im.chel(k, j,
                                 round(self.im.getel(k, j) - self.im.getel(i, j) * self.im.getel(k, i), self.accuracy))
                    self.im.showmatrix()
                    j -= 1
                k -= 1
        print("End of back step <-----")

    def inversematrix0(self):
        print('')
        print("Number conversion...")
        for raw in range(0, self.im.len[0]):
            self.numberconversion(raw)
            self.rawsubtract(raw)
            pass
        self.aim = self.im.copy()
        self.aim.rename("Inverse matrix")
        self.aim.reverseim()
        for raw in range(0, self.im.len[0]):
            self.numberconversion(raw)
            self.rawsubtract(raw)
            pass
        pass

    def inversematrix(self):
        print('')
        print("Matrix inverse...")
        for raw in range(0, self.im.len[0]):
            self.numberconversion(raw)
            self.rawsubtract(raw)
            pass
        #self.im.reverseim()
        print('Prefinal result')
        self.im.showmatrix()
        #for raw in range(0, self.im.len[0]):
            #self.reversal(raw)
            #pass
        self.reversal()
        #self.im.reverseim()
        self.aim = self.im.copypart([0,self.im.len[0],self.im.len[0],self.im.len[1]])
        self.aim.rename("Result")
        self.aim.showmatrix()
        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Inverse matrix calculation v0.0002 betta")
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
                self.am.showmatrix()
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 9):
                self.makedafault()
                pass
            elif (task == 10):
                self.inversematrix()
                pass
            elif (task == 11):
                self.inversematrix()
                pass
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
        self.am = matrix.Matrix([[3.81, 0.25, 1.28, 1.75],
                                [2.25, 1.32, 5.58, 0.49],
                                [5.31, 7.28, 0.98, 1.04],
                                [10.39, 2.45, 3.35, 2.28]],
                               "Initial matrix")
        self.im = self.am.copy()
        self.im.rename("Initial and identity matrix")
        i = matrix.Matrix([], "Identity matrix")
        i.makedimatrix(self.am.len[0])
        self.im.join(i)
        self.aim = matrix.Matrix([], "Inverse matrix")
