import math
import matrix


class IM:

    def __init__(self,arg):
        self.am = matrix.Matrix(arg, "Initial matrix")
        self.im = matrix.Matrix(arg, "Initial and identity matrix")
        i = matrix.Matrix([],"Identity matrix")
        i.makedimatrix(self.am.len[0])
        self.im.join(i)
        self.aim = matrix.Matrix([], "Inverse matrix")
        pass

    def numberconversion(self, raw):
        print('')
        print("Number conversion...")
        num = self.im.getel(raw, raw)
        print("R", raw + 1, "/", num, ";")
        for i in range(raw, self.im.len[1]):
            print("Step #", i + 1)
            self.im.chel(raw, i, self.im.getel(raw, i) / num)
            self.im.showmatrix()
        print('End of number conversion')
        pass

    def rawsubtract(self, raw):
        print('')
        print("Row subtract...")
        print("R", raw + 1, ";")
        for k in range(raw + 1, self.im.len[0]):
            print("R", k + 1, "- R", k, "*", "R", k + 1, "[i,i - 1]")
            if math.copysign(1, self.im.getel(raw, raw)) == math.copysign(1, self.im.getel(k, raw)):
                #self.lm.chel(k, raw, self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = self.im.getel(k, raw) / self.im.getel(raw, raw)
                pass
            else:
                #self.lm.chel(k, raw, -1 * self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = +1 * self.im.getel(k, raw) / self.im.getel(raw, raw)
                pass
            # self.lm.chel(k,raw,self.um.getel(k,raw) / self.um.getel(raw,raw))
            # self.lm.chel(k,raw,self.um.getel(k,raw))
            self.im.chel(k, raw, 0)
            for j in range(raw + 1, self.im.len[1]):
                print("Step #", j + 1)
                self.im.chel(k, j, self.im.getel(k, j) - self.im.getel(raw, j) * num)
                self.im.showmatrix()
                pass
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

    def reversal(self, raw):
        print('')
        print("Reversal...")
        rawr = -(raw + 1)
        intervali = list(range(-self.im.len[0], rawr))
        intervalj = list(range(-self.im.len[1] + (self.im.len[1] - raw - 4), 0))
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
            print("R", k, "- R", k, "*", "R", k, "[i,i - 1]")
            #if math.copysign(1, self.im.getel(rawr, rawr)) == math.copysign(1, self.im.getel(k, rawr)):
            if math.copysign(1, self.im.getel(k, rawr - self.am.len[0])) > 0:
                # self.lm.chel(k, raw, self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = self.im.getel(k, rawr - self.am.len[0])
                # -1
                pass
            else:
                # self.lm.chel(k, raw, -1 * self.im.getel(k, raw) / self.im.getel(raw, raw))
                num = +1 * self.im.getel(k, rawr - self.am.len[0])
                pass
            # self.lm.chel(k,raw,self.um.getel(k,raw) / self.um.getel(raw,raw))
            # self.lm.chel(k,raw,self.um.getel(k,raw))
            self.im.chel(k, rawr - self.am.len[0], 0)
            j = -1
            while j > intervalj[-1]:
                print("Step #", j + 1)
                print("k:", k, "j:", j, "rawr:", rawr)
                print("Do:", self.im.getel(k, j), self.im.getel(rawr, j), num)
                self.im.chel(k, j, self.im.getel(k, j) - self.im.getel(rawr, j) * num)
                print("Result of subtraction: ", self.im.getel(k, j))
                self.im.showmatrix()
                j-=1
                pass
            k -= 1
        #while (k  self.im.len[0]):

        print('End of reversal')
        pass

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
        for raw in range(0, self.im.len[0]):
            self.reversal(raw)
            pass
        #self.im.reverseim()
        self.aim = self.im.copypart([0,self.im.len[0],self.im.len[0],self.im.len[1]])
        self.aim.rename("Result")
        self.aim.showmatrix()
        pass