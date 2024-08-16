import random

tentativas = 0

while tentativas < 4:
	
	if tentativas == 1:
		print('Primeira Tentativa!')
		
	elif tentativas == 2:
		print('Segunda tentativa!')
		
	elif tentativas == 3:
		print('Última tentativa!')
	
	escolha = str(input('Escolha entre [Pedra, Papel ou Tesoura] \n'))
	
	if escolha == 'Pedra' or escolha == 'Papel' or escolha == 'Tesoura':
		
		escolhaComp = ['Pedra', 'Papel', 'Tesoura']
		
		comp = random.choice(escolhaComp)
		
		print(f'O Jogador 2 escolheu {comp}')
		
		if escolha == 'Pedra' and comp == 'Pedra':
			
			print('Ocorreu um empate! Nenhum jogador venceu!')
			
			tentativas += 1
			
		elif escolha == 'Papel' and comp == 'Papel':
			
			print('Ocorreu um empate! Nenhum jogador venceu!')
			
			tentativas += 1
			
		elif escolha == 'Tesoura' and comp == 'Tesoura':
			
			print('Ocorreu um empate! Nenhum jogador venceu!')
			
			tentativas += 1
			
		elif escolha == 'Pedra' and comp == 'Papel':
			
			print('Jogador 2 venceu! Papel vence de Pedra!')
			
			tentativas += 1
			
		elif escolha == 'Pedra' and comp == 'Tesoura':
			
			print('Jogador 1 venceu! Pedra vence de Tesoura!')
			break
			
		elif escolha == 'Papel' and comp == 'Pedra':
			
			print('Jogador 1 venceu! Papel vence de Pedra!')
			break
			
		elif escolha == 'Papel' and comp == 'Tesoura':
			
			print('Jogador 2 venceu! Tesoura vence de Papel!')
			
			tentativas += 1
			
		elif escolha == 'Tesoura' and comp == 'Pedra':
			
			print('Jogador 2 venceu! Pedra vence de Tesoura!')
			
			tentativas += 1
			
		else:
			print('Jogador 1 venceu! Tesoura vence de Papel!')
			break
	
	else:
	    if escolha != 'Pedra' or escolha != 'Papel' or escolha != 'Tesoura': 
		    print('Opção inexistente!')