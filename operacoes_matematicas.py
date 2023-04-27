def calculadora() :
	n1 = input("Digite o primeiro número:   ")

	n2 = input("Digite o segundo número:    ")

	operacao = input("Digite a operação:   ")

	if operacao == "+" :

		resultado = int(n1) + int(n2)

		print(resultado)
	elif operacao == "-" :

		resultado = int(n1) - int(n2)

		print(resultado)
	elif operacao == "*" :

		resultado = int(n1) * int(n2)

		print(resultado)
	elif operacao == "/" :

		resultado = float(n1) / float(n2)

		print(resultado)
		
	else :
		print("Caractere inválido.")
		
calculadora()

continuar = input("Deseja continuar?   ")
while (continuar == "sim") :
	calculadora()
else :
	print("Ok, a operação parou.")
