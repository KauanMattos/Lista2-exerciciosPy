quantidade_dias = int(input("Digite a quantidade de dias trabalhados: "))
salario_bruto = quantidade_dias * 150
inss = salario_bruto * 0.07
ir = salario_bruto * 0.15
salario_liquido = salario_bruto - inss - ir

print(f"Valor final a ser pago: {salario_liquido:.2f} R$")