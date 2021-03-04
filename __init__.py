from pybrazil.errors import *

class CPF:
    def __init__(self, number):
        self.cpf = str(number)
        self.remove_char()
        if len(self.cpf) < 11:
            raise InvalidLength(11, "CPF")
        if not self.validate():
            print("CPF is invalid")
            self.cpf = None

    def remove_char(self):
        char = ['*', ' ', '\n', '\t', '.', ',', '-', '_', '>', '<']
        for c in char:
            self.cpf.replace(c, "")

    def get_format(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[7:10]}-{self.cpf[10:]}"

    def get_numbers(self):
        return self.cpf

    def validate(self):
        soma = 0
        mult = 10
        num = self.cpf[:len(self.cpf)-2]
        for i in range(len(num)):
            soma += mult * int(num[i])
            mult -= 1
        rest = soma % 11
        if rest >= 2:
            num += str(11 - rest)
        else:
            num += "0"

        soma = 0
        mult = 11
        for i in range(len(num)):
            soma += mult * int(num[i])
            mult -= 1
        rest = soma % 11
        if rest >= 2:
            num += str(11 - rest)
        else:
            num += "0"
        if num[10:] == self.cpf[10:]:
            return True
        else:
            return False
        