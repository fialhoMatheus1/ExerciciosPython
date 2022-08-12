from Model import Model

class Control:
    #metodo construtor:
    def __init__(self):
        self.model = Model()
        self.opcao = -1
        self.c = 0
        self.base = 0
        self.altura = 0
        self.idade = 0
        self.meses = 0
        self.dias = 0

    def getC(self):
        return self.c

    def setC(self, c):
        self.c = c

    def getBase(self):
        return self.base

    def setBase(self, base):
        self.base = base

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def getMeses(self):
        return self.meses

    def setMeses(self, meses):
        self.meses = meses

    def getDias(self):
        return self.dias

    def setDias(self, dias):
        self.dias = dias

    def menu(self):
        print("")
        print("Escolha uma das opções abaixo:\n\n" +
            "1. Exercício 1\n" +
            "2. Exercício 2\n" +
            "3. Exercício 3\n" +
            "4. Exercício 4\n" +
            "5. Exercício 5\n" +
            "6. Exercício 6\n" +
            "7. Exercício 7\n" +
            "8. Exercício 8\n" +
            "9. Exercício 9\n" +
            "0. Sair")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()
            if self.opcao == 0:
                print("Obrigado!!")
            elif self.opcao == 1:
                print("EXERCÍCIO 1:")
                print("A: 10\n"
                      "B: 20")
                print(self.model.exercicio01())
            elif self.opcao == 2:
                print("EXERCÍCIO 2:")
                print("Digite um número: ")
                self.setC(int(input()))
                print("O antecessor é: {}".format(self.model.exercicio02(self.getC())))
            elif self.opcao == 3:
                print("Digite a base:")
                self.setBase(int(input()))
                print("Digite a altura:")
                self.setAltura(int(input()))
                print("A área é: {}".format(self.model.exercicio03(self.getBase(), self.getAltura())))
            elif self.opcao == 4:
                print("Digite sua idade:")
                self.setIdade(int(input()))
                print("Digite seus meses:")
                self.setMeses(int(input()))
                print("Digite seus dias:")
                self.setDias(int(input()))
                print("Sua idade em dias é: {}".format(self.model.exercicio04(self.getIdade(), self.getMeses(), self.getDias())))

            else:
                print("Opção inválida!")