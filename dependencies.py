class Tab:
    def __init__(self):
        """ Cria um tabuleiro vazio e define o vencedor como vazio. """
        self.tab = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        self.winner = None
        self.victory = False
        self.velha = False
        self.x_count = 0
        self.y_count = 0

    def __str__(self) -> str:
        """ Retorna o tabuleiro em formato de string. """
        tabuleiro = "-----\n"
        for i in range(3):
            for j in range(3):
                if j == 0:
                    tabuleiro += "|"
                if self.tab[i][j] == 0:
                    tabuleiro += " _ "
                if self.tab[i][j] == 1:
                    tabuleiro += " X "
                if self.tab[i][j] == 2:
                    tabuleiro += " O "
            tabuleiro += " |\n"
        tabuleiro += "-----"
        return str(tabuleiro)

    def getTab(self) -> list:
        """ Retorna o tabuleiro. """
        return self.tab

    def setTab(self, tab):
        """ Define o tabuleiro. """
        self.tab = tab

    def getWinner(self):
        """ Retorna o vencedor da partida. """
    def setWinner(self, winner):
        """ Define o vencedor da partida."""
        self.winner = winner
    def getVictory(self) -> bool:
        """ Retorna o vencedor. """
        return self.victory

    def setVictory(self, victory):
        """ Define o vencedor. """
        self.victory = victory

    def getVelha(self) -> bool:
        """ Retorna se deu velha. """
        return self.velha

    def setVelha(self, velha):
        """ Define se deu velha. """
        self.velha = velha

    def input_x(self, x, y):
        """ Insere um X no tabuleiro. """
        self.x_count += 1
        self.tab[x][y] = 1

    def input_y(self, x, y):
        """ Insere um Y no tabuleiro. """
        self.y_count += 1
        self.tab[x][y] = 2

    def checkVictory(self) -> None:
        """ Verifica se houve vencedor e retorna o vencedor."""
        value = 0
        if (0 in [cell for row in self.tab for cell in row]):
            if (self.x_count + self.y_count > 4):
                # Só pode ter vitória se ao menos 5 jogadas foram feitas
                #Checa jogadas diagonais
                if self.tab[0][0] == self.tab[1][1] == self.tab[2][2] != 0:
                    value = self.tab[0][0]
                if self.tab[2][0] == self.tab[1][1] == self.tab[0][2] != 0:
                    value = self.tab[0][0]

                #Checa jogadas verticais e horizontais
                for i in range(3):
                    if self.tab[i][0] == self.tab[i][1] == self.tab[i][2] != 0:
                        value = self.tab[i][0]
                        break  # Já encontrei o vencedor. Não vou reescrever vitória
                    if self.tab[0][i] == self.tab[1][i] == self.tab[2][i] != 0:
                        value = self.tab[0][i]
                        break  # Já encontrei o vencedor. Não vou reescrever vitória
        if value:
            self.setVictory(True)
            if value == 1:
                self.setWinner("X")
            else:
                self.setWinner("Y")
            
        elif 0 not in [cell for row in self.tab for cell in row]:
            self.setVelha(True)
        
