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
        return (idade * 365) + (meses * 30) + dias

    def exercicio05(self, eleitores, brancos, nulos, validos):
        totalVotos = brancos + nulos + validos
        if totalVotos == eleitores:
            return "Total de eleitores: {}\nPercentual brancos: {}%\nPercentual nulos: {}%\nPercentual validos: {}%".format(eleitores, (eleitores * brancos) /100, (eleitores * nulos) / 100, (eleitores * validos) / 100)
        else:
            return "Quantidade de votos não bate com total de eleitores. Tente novamente."

    def exercicio06(self, salario, reajuste):
        salarioNovo = salario + (salario * reajuste) / 100
        return "Seu salário reajustado é: R${}".format(salarioNovo)

    def exercicio07(self, custoFabrica, percentualDistribuidor, percentualImposto):
        totalImposto = percentualDistribuidor / 100 + percentualImposto / 100
        custoFinal = custoFabrica + (custoFabrica + totalImposto)
        return "O custo final ao consumidor é: R${}".format(custoFinal)

    def exercicio08(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3) / 3

    def exercicio09(self, macas):
        if macas < 12:
            return macas * 1.30
        else:
            return macas * 1.00

    def exercicio10(self, num):
        pass

    def exercicio11(self, salario, vendas):
        if vendas < 1:
            return("Impossível calcular com vendas negativas.")
        if vendas <= 1500.00:
            totalVendas = (vendas * 3) /100
            novoSalario = totalVendas + salario
            return novoSalario
        else:
            vendasExtras = vendas - 1500.00
            vendasExtras = (vendasExtras * 5) / 100
            totalVendas = (vendas * 3) / 100
            novoSalario = totalVendas + vendasExtras + salario
            return novoSalario
    def exercicio12(self, conta, saldo, debito, credito):
        saldoAtual = saldo - debito + credito
        if saldoAtual < 0:
            return("Saldo atual é: R${}\nSaldo é negativo.".format(saldoAtual))
        else:
            return("Saldo atual é: R${}\nSaldo é positivo.".format(saldoAtual))

    def exercicio13(self, num):
        if (num > 0) & (num < 11):
            msg = ""
            for i in range(11):
                msg = msg + "\n{} * {} = {}".format(num, i, num * i)
            return msg
        else:
            return "Número inválido."

    def exercicio14(self, n):
        for x in range(1, n + 1):
            print(x)

    def exercicio15(self):
        numNegativo = 0
        for i in range(0, 10):
            print("Informe um número:")
            num = int(input())
            if num < 0:
                numNegativo = numNegativo + 1
        return "Houve {} número(s) negativo(s).".format(numNegativo)

    def exercicio16(self):
        guardarNum = 0
        for i in range(0, 10):
            print("Informe um número:")
            num = int(input())
            if num < 40:
                guardarNum = guardarNum + num
        return "O total somado é: {}".format(guardarNum)

    def exercicio17(self):
        media = 58 * 115 / 85
        return "A média aritmética do intervalo de 15 e 100 é: {}".format(media)

    def exercicio18(self):
        pass

    def exercicio19(self):
        contarNota = 0#contador que guarda as notas inseridas para calcular a média
        maiorNota = 0#contador que guarda as notas superiores a media da sala
        for i in range(0, 20):
            print("Informe a nota:")
            nota = float(input())
            contarNota = contarNota + nota
            media = contarNota / 20
            if nota > media:
                maiorNota = maiorNota + 1
        return "A média da sala é: {}.\nHouveram {} notas acima da média.".format(media, maiorNota)
