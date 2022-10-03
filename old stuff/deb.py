import random
import re

# Criação do objeto Campo apenas para representar o campo minado,
# sendo assim possível criar um novo objeto de campo.

class Campo:
    def __init__(self, tamanho, num_bombas):
        # Os parâmetros do Campo serão úteis mais pra frente 
        self.tamanho = tamanho
        self.num_bombas = num_bombas

        # Criando uma função para ajudar nosso Campo
        
        self.campo = self.criar_novo_campo()
        self.aplicar_valores_campo()

        # Inicialização de um set pra saber quais localizações foram descobertas
        # row = linhas / col = colunas
        self.cavou = set() # Se cavarmos em 0,0, então self.cavou = {(0,0)}

    def criar_novo_campo(self):
        
        # Construção de um novo campo baseado no tamanho e nº de bombas

        # Geração de um novo campo
        campo = [[None for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        # Isso irá criar um Array do tipo:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [None, None, ..., None],
        #  [None, None, ..., None]]
        # Assim, é possível visualizar o campo.

        # Implantação das bombas
        bombas_plantadas = 0
        while bombas_plantadas < self.num_bombas:
            loc = random.randint(0, self.tamanho**2 - 1) # Retorna um aleatório inteiro N cujo a <= N <= b
            row = loc // self.tamanho  # Número de vezes que tamanho vai para a localização (loc) nos dizer para qual coluna (row) olharmos.
            col = loc % self.tamanho   # Irá dizer qual index na coluna (row) iremos ver
    

            if campo[row][col] == '*':
                # Isso significa que já foi plantada uma bomba ali, então, continue:
                continue

            campo[row][col] = '*' # Implantação da bomba
            bombas_plantadas += 1

        return campo

    def aplicar_valores_campo(self):
        # Agora que todas as bombas foram plantadas, vamos representar um número de 0 a 8 para todos os
        # espaços em branco, que irá representar quantas bombas vizinhas existem. 

        for r in range(self.tamanho):
            for c in range(self.tamanho):
                if self.campo[r][c] == '*':
                    # Se essa localização já for uma bomba, não iremos calcular nada, então, continue:
                    continue
                self.campo[r][c] = self.loc_bombas_vizinhas(r, c)

    def loc_bombas_vizinhas(self, row, col):
        # LOCALIZAÇÃO DAS BOMBAS VIZINHAS
        # vamos percorrer por cada uma das posições vizinhas e somar o número de bombas:

        # Esquerda de cima da bomba: (row-1, col-1)
        # Meio de cima da bomba: (row-1, col)
        # Direita de cima da bomba: (row-1, col+1)
        # Esquerda da bomba: (row, col-1)
        # Direita da bomba: (row, col+1)
        # Esquerda embaixo da bomba: (row+1, col-1)
        # Meio embaixo da bomba: (row+1, col)
        # Direita embaixo da bomba: (row+1, col+1)

        num_bombas_vizinhas = 0
        for r in range(max(0, row-1), min(self.tamanho-1, row+1)+1):
            for c in range(max(0, col-1), min(self.tamanho-1, col+1)+1):
                if r == row and c == col:
                    # Se r == row e c == col, é a nossa localização original, portanto, continue:
                    continue
                if self.campo[r][c] == '*':
                    num_bombas_vizinhas += 1

        return num_bombas_vizinhas

    def cavar(self, row, col):
        # Comando para cavar em tal localização
        # return True se cavou com sucesso, False se uma bomba for escavada.

        # Possíveis acontecimentos:
        # Atingiu uma bomba -> GAME OVER
        # Cavou uma localização sem bombas vizinhas -> continue cavando até encontrar bombas vizinhas
        # Cavou uma localização com bombas vizinhas -> termine de cavar o campo
      

        self.cavou.add((row, col)) # Mantendo registro do que já foi escavado

        if self.campo[row][col] == '*':
            return False
        elif self.campo[row][col] > 0:
            return True

        # self.campo[row][col] == 0
        for r in range(max(0, row-1), min(self.tamanho-1, row+1)+1):
            for c in range(max(0, col-1), min(self.tamanho-1, col+1)+1):
                if (r, c) in self.cavou:
                    continue # Se já foi escavado, você não irá cavar novamente o que já cavou. continue:
                self.cavar(r, c)

        # Caso nossa primeira escavada não acertou uma bomba:
        return True

    def __str__(self):
        # Retorna uma string que mostra o campo para o jogador.

        # Criando um array que representa o que o jogador irá ver:
        campo_visivel = [[None for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        for row in range(self.tamanho):
            for col in range(self.tamanho):
                if (row,col) in self.cavou:
                    if self.campo[row][col] == 0:
                        campo_visivel[row][col] = '-'
                    else:
                        campo_visivel[row][col] = str(self.campo[row][col])
                else:
                    campo_visivel[row][col] = '#'
        
        # Colocando tudo junto em uma string:
        string_rep = ''
        
        # Obtendo o máximo de espaços(widths) de colunas para printar:
        widths = []
        for idx in range(self.tamanho):
            columns = map(lambda x: x[idx], campo_visivel)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # Representação do jogo:
        indices = [i for i in range(self.tamanho)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(campo_visivel)):
            row = campo_visivel[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.tamanho)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# Inicializando o Campo Minado
def play(tamanho=10, num_bombas=10):
    # 1º Passo: criação do campo e implantação das bombas
    campo = Campo(tamanho, num_bombas)

    # 2º passo: Mostrar o campo pro usuário e perguntar onde ele gostaria de cavar
    # 3º passo: Se a localização for uma bomba, printar mensagem de GAME OVER 
    # 4º passo: Se a localização não for uma bomba, continuar cavando até cavar perto de uma
    # 5º passo: Repetir o 1º e 2º passo até não existirem mais lugares para cavar
    safe = True 

    while len(campo.cavou) < campo.tamanho ** 2 - num_bombas:
        print(campo)
        # 0,0 ou 0, 0 ou 0,    0
        user_input = re.split(',(\\s)*', input("Onde você gostaria de cavar? Insira no formato linha,coluna: "))  #Exemplo: '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= campo.tamanho or col < 0 or col >= tamanho:
            print("Localização inválida. Tente denovo.")
            continue

        # Se a localização for válida, iremos cavar
        safe = campo.cavar(row, col)
        if not safe:
            # vc cavou uma bomba!!!!!!
            break # Descanse em paz

    # 2 maneiras para terminar o loop:
    if safe:
        print("Parabéns, você venceu!.")
        print("*===================*")
        print("|      VICTORY      |")
        print("*===================*")

    else:
        print("Você cavou uma bomba.")
        print("*===================*")
        print("|    GAME   OVER    |")
        print("*===================*")
        
        # Revelando o campo inteiro, após o jogo terminar:
        campo.cavou = [(r,c) for r in range(campo.tamanho) for c in range(campo.tamanho)]
        print(campo)
        
# Chamando a função play, para agora realmente jogar o Campo minado:
if __name__ == '__main__': 
    play()