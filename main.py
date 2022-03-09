print("Olá! Este é um controle de caixa básico!")
print("========================================")

saldo = float(0)
vendaDiaria = float(0)
escolha = int(0)
clear = "\n" * 300

while True:
    print("Para iniciar uma venda digite [1]")
    print("¬")
    print("Para saber o saldo digite [2]")
    print("¬")
    print("Para verificar as vendas diárias digite [3]")
    print("¬")

    escolha = int(input())

    if escolha == 1:
        print("Digite o valor da venda:")
        vendaAtual = input()
        vendaAtual = vendaAtual.replace(",", ".")
        vendaAtual = float(vendaAtual)
        if vendaAtual <= 0:
            print("[ERRO] Impossível inserir um valor igual a Zero ou Negativo!")
            print("Valor inserido incorretamente: [" + str(vendaAtual) + "]")
            continue
        else:
            saldo += vendaAtual
            vendaDiaria += vendaAtual
            print(clear)
            print("[Venda realizada! Valor: R$ " + str(vendaAtual) + "]")
            print("¬")

    elif escolha == 2:
        print(clear)
        print("[Seu saldo é: R$ " + str(saldo) + "]")
        print("¬")

    elif escolha == 3:
        print(clear)
        print("¬")
        if vendaDiaria == 0:
            print("[Nenhuma venda até o momento]")
            print("¬")
        else:
            print("Vendas diárias: R$ " + str(vendaDiaria))
            print("¬")
