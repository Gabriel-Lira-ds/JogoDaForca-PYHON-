# Gabriel Lira
print('=~'*10)
print('|  \033[1;32mJOGO DA FORCA!\033[m  |')
print('=~'*10)
cont1 = ('''\033[1m
|------
|    |
|    
|      
|    
|       ''')
cont2 = ('''
|------
|    |
|    O
|       
|    
|        ''')
cont3 = ('''
|------
|    |
|    O
|    |    
|    
|       ''')
cont4 = ('''
|------
|    |
|    O
|   /|  
|    
|     ''')
cont5 = ('''
|------
|    |
|    O
|   /|\    
|    
|    ''')
cont6 = ('''
|------
|    |
|    O
|   /|\    
|    |
|    ''')
cont7 = ('''
|------
|    |
|    O
|   /|\    
|    |
|   /      ''')
cont8 = ('''
|------
|    |
|    O
|   /|\    
|    |
|   / \     ''')
cont = 1
#lista = ['T', 'E', 'R', 'E', 'S', 'I',  'N', 'A']
lista = list('JANEIRO')
oculto = (' _'*len(lista)).split()
print('DICA: Mês!')
print('PALAVRA: ', ' '.join(oculto))
print(' ')
while oculto != lista:
	print('=~'*10)
	palpite = str(input('Qual o seu palpete: ')).upper()
	print('=~'*10)
	if palpite in lista:
		oculto[lista.index(palpite)] = palpite
#		if cont == 0:
			#print(' '.join(oculto) )
	#		print(cont1, ' '.join(oculto))
		if cont == 1:
			print(cont1, ' '.join(oculto))
		elif cont == 2:
			print(cont2, ' '.join(oculto))
		elif cont == 3:
			print(cont3, ' '.join(oculto))
		elif cont == 4:
			print(cont4, ' '.join(oculto))
		elif cont == 5:
			print(cont5, ' '.join(oculto))
		elif cont == 6:
			print(cont6, ' '.join(oculto))
		elif cont ==7:
			print(cont7, ' '.join(oculto))
		elif cont == 8:
			print(cont8, ' '.join(oculto))
	else:
		cont += 1
		if cont == 1:
			print(cont1, ' '.join(oculto))
		elif cont == 2:
			print(cont2, ' '.join(oculto))
		elif cont == 3:
			print(cont3, ' '.join(oculto))
		elif cont == 4:
			print(cont4, ' '.join(oculto))
		elif cont == 5:
			print(cont5, ' '.join(oculto))
		elif cont == 6:
			print(cont6, ' '.join(oculto))
		elif cont ==7:
			print(cont7, ' '.join(oculto))
		elif cont == 8:
			print(cont8, ' '.join(oculto))	
			print('\033[1;31m: ( BURRA, PERDEL!\033[m')
			break
			