bonus_2024 = 1000

# Solicite ao usuario que digite seu nome

nome = input("Digite seu nome: ")

# Solicite ao usuario que digite o valor do seu salário

salario = float(input("Digite seu salario: "))

# Solicite ao usuario que digite o valor do bônus recebido

bonus = float(input("Digite seu bonus: "))

# Calcule o valor do bônus final

final_bonus = (salario*bonus)

# Imprima o cálculo do KPI para o usuário
# Imprima a mensagem personalizada incluindo o nome do usuário, e o valor do bônus

kpi = str(bonus_2024 + final_bonus)
print( "Olá "+ nome +" seu KPI do bônus de 2024 é de " + kpi + " Reais")


