class Salary:
    def __init__(self, numero_funcionario: int, horas_trabalhadas: int, valor_hora: float):
        self._numero_funcionario = numero_funcionario
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora

    def calcular_salario(self) -> float:
        return self._valor_hora * self._horas_trabalhadas


    def return_salario(self) -> str:
        salario = self.calcular_salario()

        return f"SALARY = U$ {salario:.2f}"

    def return_number(self) -> str:
        return f"NUMBER = {self._numero_funcionario}"


resultado_obtido = Salary(7845, 10, 9.5)
print(resultado_obtido.return_salario())
print(resultado_obtido.return_number())
