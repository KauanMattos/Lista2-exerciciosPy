valor_produto = float(input("Insira o valor do produto: R$"))
quantidade_parcelas = float(input("Insira a quantidade de parcelas: "))
juros = valor_produto * 0.02 * quantidade_parcelas
valor_total = valor_produto + juros

print(f"O valor total a pagar é de: {valor_total:.2f}")