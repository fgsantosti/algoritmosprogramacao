import random

def jogar():
    # Lista de palavras para o jogo
    palavras = ["PYTHON", "PROGRAMACAO", "DESENVOLVEDOR", "COMPUTADOR", "LIGACAO", "TECNOLOGIA"]
    
    # Escolhe uma palavra aleatória da lista
    palavra_secreta = random.choice(palavras)
    
    # Cria uma lista com underscores (_) representando as letras ocultas
    letras_descobertas = ["_" for letra in palavra_secreta]
    
    chances = 6
    letras_erradas = []
    
    print("*************************************")
    print("       Bem-vindo ao Jogo da Forca!   ")
    print("*************************************")
    
    # Loop do jogo
    while chances > 0 and "_" in letras_descobertas:
        print("\nPalavra: ", " ".join(letras_descobertas))
        print(f"Chances restantes: {chances}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        # Pede uma letra ao jogador e formata para maiúsculo
        palpite = input("Digite uma letra: ").upper()
        
        # Validação: garante que o usuário digitou apenas uma letra
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
            
        # Verifica se a letra já foi jogada
        if palpite in letras_descobertas or palpite in letras_erradas:
            print("Você já tentou esta letra. Tente outra.")
            continue
            
        # Lógica de acerto ou erro
        if palpite in palavra_secreta:
            for indice, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[indice] = palpite
        else:
            letras_erradas.append(palpite)
            chances -= 1
            print(f"A letra '{palpite}' não está na palavra.")

    # Condições de vitória ou derrota
    if "_" not in letras_descobertas:
        print("\n🎉 Parabéns! Você venceu! A palavra era:", palavra_secreta)
    else:
        print("\n😢 Você perdeu! Suas chances acabaram.")
        print(f"A palavra secreta era: {palavra_secreta}")

# Executa o jogo
if __name__ == "__main__":
    jogar()

