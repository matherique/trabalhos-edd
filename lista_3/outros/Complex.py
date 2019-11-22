class Complex:
    __slots__ = ['__real', '__imaginaria', '__letra']

    def __init__(self, real, imaginaria, letra='i'):
        self.__real = real
        self.__imaginaria = imaginaria
        self.__letra = letra

    def __str__(self):
        if self.imaginaria > 0:
            return "{} + {}{}".format(self.real, self.imaginaria, self.letra)
        else:
            return "{} {}{}".format(self.real, self.imaginaria, self.letra)

    def conjugado(self):
        return Complex(self.real, self.imaginaria * (-1), self.letra)

    @property
    def real(self):
        return self.__real

    @property
    def imaginaria(self):
        return self.__imaginaria

    @property
    def letra(self):
        return self.__letra

    def __add__(self, c2):
        parteReal = self.real + c2.real
        parteImaginaria = self.imaginaria + c2.imaginaria
        
        return Complex(parteReal, parteImaginaria)

    def __sub__(self, c2):
        parteReal = self.real - c2.real
        parteImaginaria = self.imaginaria - c2.imaginaria
        
        return Complex(parteReal, parteImaginaria)

    def __mul__(self, c2):
        parteReal = (self.real * c2.real) + (self.imaginaria * c2.imaginaria * (-1))
        parteImaginaria = (self.real * c2.imaginaria) + (self.imaginaria * c2.real)

        return Complex(parteReal, parteImaginaria)
    
    def __truediv__(self, c2):
        numerador = self * c2.conjugado() 
        denominador = (c2.real * c2.real) - (c2.imaginaria * c2.imaginaria * (-1))

        parteReal = numerador.real / denominador 
        parteImaginaria = numerador.imaginaria / denominador 

        return Complex(parteReal, parteImaginaria)
