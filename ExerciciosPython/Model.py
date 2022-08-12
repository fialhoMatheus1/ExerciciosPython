class Model:
    #metodo construtor:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.aux = 0

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b

    def getAux(self):
        return self.aux

    def setAux(self, aux):
        self.aux = aux

    def exercicio01(self):
        self.getAux = self.getA
        self.getA = self.getB
        self.getB = self.getAux
        return "Os valores trocados são: \nA: {}\nB: {}".format(self.getA(), self.getB())

    def exercicio02(self, c):
        return c - 1

    def exercicio03(self, base, altura):
        return base * altura

    def exercicio04(self, idade, meses, dias):
        return idade * 365 + meses * 30 + dias

