from banco.conta import Contas

class ContaCorrente(Contas):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    @property
    def limite(self):
        return self._limite
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            raise ValueError('Saldo insuficiente')

        self.saldo -= valor
        self.detalhe()