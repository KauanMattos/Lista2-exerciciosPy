# Uma empresa contrata um pedreiro com a diária de R$150,00. 
# Crie um Algoritmo que leia a quantidade de dias trabalhados e logo depois exiba o valor 
# a ser pago com o desconto de 7% do INSS e 15% do IR

quantidade_dias = int(input("Digite a quantidade de dias trabalhados: "))
salario_bruto = quantidade_dias * 150
inss = salario_bruto * 0.07
ir = salario_bruto * 0.15
salario_liquido = salario_bruto - inss - ir

print(f"Valor final a ser pago: {salario_liquido:.2f} R$")

url_fluxograma = "https://drive.google.com/file/d/11PxImYuKZxOALBeggQ3eQgmLH9hXboSi/view?usp=sharing"