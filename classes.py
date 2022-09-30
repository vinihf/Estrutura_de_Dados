class Calculadora:
    def __init__(self, valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def soma(self):
        return (self.valor1+self.valor2)


c = Calculadora(1,2)
print(c.soma())