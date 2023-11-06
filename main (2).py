#Algoritmo IMC
#Este algoritmo é capa de calcular o IMC da pessoa, e dizer se ela está abaixo do peso, No peso normal, acima do peso, marginalmente acima do peso, acima do peso ou obeso.
#Para o calaculo o algoritmo irá usar a seguinte fórmula IMC = Peso/(altura)^2
#Para o cálculo da altura o algoritmo irá utilizar a fórmula (altura)^2 = altura * altura 
#Receber input de sexo
#receber input de de peso 
#receber input de altura
#calcular o imc
#se o imc for menor que <19.1 para mulher e <20.7 para Homem esta ABAIXO DO PESO
#se o imc for entre <19.1-25.8 para mulher e 20.7-26.4 para Homem esta No PESO NORMAL
#se o imc for ENTRE 25.8-27.3 para mulher e 26.4-27.8 para Homem esta mARGINALMENTE ACIMA DO PESO
#se o imc for ENTRE 27.3-32.3 para mulher e 27.8-31.1 para Homem esta ACIMA DO PESO
#se o imc for >32.3 para mulher e >31.1 para Homem esta OBESO

# importando bibliotecas
#receber o input do sexo

sexo=str((input("Qual o seu sexo? (Digite F para Feminino ou M para Masculino.)")))
#receber o input de peso
peso=float(input("Qual o seu peso em KG:"))
#receber a altura
altura=float(input("Qual a sua altura: "))
#calcular o imc 
imc = peso/ (altura * altura )
print(imc)
#mostrar IMC

#se o imc for menor que <19.1 para mulher e <20.7 para Homem esta ABAIXO DO PESO 
 
if sexo == "f" or sexo == "F":
  if imc <= 19.1:
    print("Voce está abaixo do peso.")
  elif imc >= 19.1 and imc <= 25.8:
    print("Você está no peso normal.")
  elif imc >= 25.8 and imc <= 27.3:
    print("Marginalmente acima do peso.")
  elif imc >= 27.3 and imc <= 32.3:
    print("Você está acima do peso.")
  else: 
    print("Está obeso.")
else: 
  if imc < 20.7:
    print("Voce está abaixo do peso.")
  elif imc >= 20.7 and imc <= 26.4:
    print("Você está no peso normal.")
  elif imc >= 26.4 and imc <= 27.8:
    print("Marginalmente acima do peso.")
  elif imc >= 27.8 and imc <=31.1:
    print("Acima do peso.")
  else:
    print("Voce esta obeso.")
    
    


  
  