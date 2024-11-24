from conta import Conta
from cliente import Cliente
from contaExtrato import Conta as ContaExtrato

cliente1 = Cliente(123, 'Joao', 'Rua 1')
cliente2 = Cliente(345, 'Maria','Rua 2')

conta1 = Conta([cliente1,cliente2], 1,0)

conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente ("456", "Maria", "Rua W")
conta1 = ContaExtrato([cliente1, cliente2], 1, 2000)
conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)