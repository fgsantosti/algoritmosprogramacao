import random

def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    # 1. Jogada do Jogador
    print("Suas opções: 0-Pedra | 1-Papel | 2-Tesoura")
    escolha_idx = int(input("Escolha o número da sua jogada: "))
    
    if escolha_idx not in [0, 1, 2]:
        print("Jogada inválida! Tente novamente.")
        return
        
    jogador = opcoes[escolha_idx]
    
    # 2. Jogada do Computador
    computador = random.choice(opcoes)
    
    print(f"\nVocê escolheu: {jogador.capitalize()}")
    print(f"O computador escolheu: {computador.capitalize()}")
    
    # 3. Determinação do Vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print("Você Venceu!")
    else:
        print("Você Perdeu!")

jogar_jokenpo()
