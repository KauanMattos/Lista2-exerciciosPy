# 2.Crie um Algoritmo que leia o valor em real e a cotação do dólar. Logo
# depois, escreva o valor correspondente em dólares. 

valor_real = float(input("Digite o valor: R$"))
cotacao_dolar = float(input("Digite a cotação do dolar: R$"))
valor_dolar = valor_real / cotacao_dolar

print(f"Valor correspondente em dólares: {valor_dolar:.2f} $")

# f"" → permite usar variável dentro do texto
# {} → onde entra a variável
# :.2f → limita casas decimais (Duas no caso)

url_fluxograma = "https://drive.google.com/file/d/10BG7DbKnv82e3ZzwJV5o50jfsHnSOo5y/view?usp=sharing"