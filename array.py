caes = ["boiadeiro australiano", "pastor alemão", "golden retriver", "catahoula cur", "cão da serra da estrela"]

for cao in caes :
	print(cao)
	
quant = len(caes)

print("A lista possui " + str(quant) + " raças de caẽs.")
	
raca = input("Digite uma raça de cão que não esta na lista:   ")

caes.append(raca)

for cao in caes :
	print(cao)
	
raca2 = input("Digite outra raça de cão que não esta na lista:   ")
for cao in caes :
	if raca2 == cao :
		print("Já esta na lista.")
		break
	else : 
		print("Não esta na lista.")
		break
		
