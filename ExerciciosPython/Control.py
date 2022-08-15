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
        self.macas = 0

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

    def getMacas(self):
        return self.macas

    def setMacas(self, macas):
        self.macas = macas

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
            "10. Exercício 10\n" +
            "11. Exercício 11\n" +
            "12. Exercício 12\n" +
            "13. Exercício 13\n" +
            "14. Exercício 14\n" +
            "15. Exercício 15\n" +
            "16. Exercício 16\n" +
            "17. Exercício 17\n" +
            "18. Exercício 18\n" +
            "19. Exercício 19\n" +
            "20. Exercício 20\n" +
            "0. Sair")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()
            if self.opcao == 0:
                print("Obrigado!!")
            elif self.opcao == 1:
                print("EXERCÍCIO 1")
                print("A: 10\n""B: 20")
                print(self.model.exercicio01())
            elif self.opcao == 2:
                print("EXERCÍCIO 2")
                print("Digite um número: ")
                self.setC(int(input()))
                print("O antecessor é: {}".format(self.model.exercicio02(self.getC())))
            elif self.opcao == 3:
                print("EXERCÍCIO 3")
                print("Digite a base:")
                self.setBase(int(input()))
                print("Digite a altura:")
                self.setAltura(int(input()))
                print("A área é: {}".format(self.model.exercicio03(self.getBase(), self.getAltura())))
            elif self.opcao == 4:
                print("EXERCÍCIO 4")
                print("Digite sua idade:")
                self.setIdade(int(input()))
                print("Digite seus meses:")
                self.setMeses(int(input()))
                print("Digite seus dias:")
                self.setDias(int(input()))
                print("Sua idade em dias é: {}".format(self.model.exercicio04(self.getIdade(), self.getMeses(), self.getDias())))
            elif self.opcao == 5:
                print("EXERCÍCIO 5")
                print("Digite o total de eleitores")
                eleitores = float(input())
                print("Digite o total de votos brancos: ")
                brancos = float(input())
                print("Digite o total de votos nulos: ")
                nulos = float(input())
                print("Digite o total de votos validos: ")
                validos = float(input())
                print(self.model.exercicio05(eleitores, brancos, nulos, validos))
            elif self.opcao == 6:
                print("EXERCÍCIO 6")
                print("Informe o salário:")
                salario = float(input())
                print("Informe o percentual de reajuste:")
                reajuste = float(input())
                print(self.model.exercicio06(salario, reajuste))
            elif self.opcao == 7:
                print("EXERCÍCIO 7")
                print("Informe o custo de fabrica:")
                custoFabrica = float(input())
                print("Informe o percentual do distribuidor:")
                percentDistribuidor = float(input())
                print("Informe o percentual de impostos:")
                percentImpostos = float(input())
                print(self.model.exercicio07(custoFabrica, percentDistribuidor, percentImpostos))
            elif self.opcao == 8:
                print("EXERCÍCIO 8")
                print("Digite a primeira nota:")
                nota1 = float(input())
                print("Digite a segunda nota:")
                nota2 = float(input())
                print("Digite a terceira nota:")
                nota3 = float(input())
                print("A média é: {}".format(self.model.exercicio08(nota1, nota2, nota3)))
            elif self.opcao == 9:
                print("EXERCÍCIO 9")
                print("Digite o total de maças compradas:")
                self.setMacas(float(input()))
                print("o total a pagar é: {}".format(self.model.exercicio09(self.getMacas())))
            elif self.opcao == 10:
                pass
            elif self.opcao == 11:
                print("EXERCÍCIO 11")
                print("Informe o salário fixo do funcionário:")
                salario = float(input())
                print("Informe o número de vendas:")
                vendas = float(input())
                print(self.model.exercicio11(salario, vendas))
            elif self.opcao == 12:
                print("EXERCÍCIO 12")
                print("Informe o número da sua conta:")
                conta = int(input())
                print("Informe o saldo atual:")
                saldo = float(input())
                print("Informe o valor de débito :")
                debito = float(input())
                print("Informe o valor de crédito :")
                credito = float(input())
                print(self.model.exercicio12(conta, saldo, debito, credito))
            elif self.opcao == 13:
                print("EXERCICIO 13")
                print("Digite um número:")
                num = int(input())
                print(self.model.exercicio13(num))
            elif self.opcao == 14:
                print("EXERCÍCIO 14")
                print("Digite um número:")
                n = int(input())
                print(self.model.exercicio14(n))
            else:
                print("Opção inválida!")