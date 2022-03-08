print("Olá! Controle de caixa v1.0")

saldo = float(100)
vendaDiaria = float(0)
vendaInit = int(0)

print("Seu saldo é: R$ " + str(saldo))
while True:
    print("Para iniciar uma venda digite 1")
    print("Para saber o saldo digite 2")
    vendaInit = int(input())
    if vendaInit == 2:
        print("Seu saldo é: R$ " + str(saldo))
    elif vendaInit == 1:
        print("Digite o valor da venda:")
        vendaAtual = float(input())
        saldo += vendaAtual
        vendaDiaria += vendaAtual
        print("Venda realizada! Valor: R$ " + str(vendaAtual))

