name = input("Qual o seu nome? ") #Pedindo entrada ao unsuário
last_name = input("Qual seu sobrenome? ")

print(name) #Exibindo a entrada exigida

#Parâmetros da função print

print(f"Seu nome é: {name}") #Concatenando texto com variáveis

print(name, last_name) #Exibindo ambas variáveis

print(name, last_name, sep="&") #Exibindo ambas variáveis e usando sep para mudar o separador

print(name, last_name, end="***\n") #Exibindo ambas variáveis mudando o final