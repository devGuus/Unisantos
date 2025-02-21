def calcularNota(totalNota, pcg):
    total = (totalNota/2)*0.9+(pcg*0.1) # Deve mudar para o formato correto de cada materia
    return total

pergunta_notas = int(input("Houveram quantas provas? "))
pergunta_pcg = float(input("Qual a nota do PCG? "))

soma = 0
for i in range(pergunta_notas):
    nota = float(input(f"Digite o valor da nota da p{i+1} "))
    soma = soma + nota

print(f"O resultado da soma das provas = {calcularNota(soma, pergunta_pcg)}")