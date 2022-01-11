from banco.cp import ContaPoupanca
from banco.cc import ContaCorrente

cp = ContaPoupanca(1234, 1235, 0)
cp.depositar(100)
cp.sacar(10)


print('###########################################')

cc = ContaCorrente(2222, 4422, 0)
cc.sacar(100)