from banco.conta import Contas

class ContaPoupanca(Contas):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor deve ser inteiro')
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return
        self.saldo -= valor
        self.detalhe()
