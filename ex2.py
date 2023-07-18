valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())


totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
valorTotal = totalHamburguer + totalBebida
troco = valorPago - valorTotal

print(f"O preço final do pedido é R$ {valorTotal:,.2f}. Seu troco é R$ {troco:,.2f}.")