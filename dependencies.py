class tab:
    def __init__(self, victory):
        self.tab = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        self.victory = victory;
        self.x_count = 0
        self.y_count = 0
        
    def __str__(self) -> str:
        return str(self.tab)
    
    def getTab(self):
        return self.tab
    
    def setTab(self, tab):
        self.tab = tab
    
    def getVictory(self):
        return self.victory
    
    def setVictory(self, value):
        self.victory = value
        
    def input_x(self, x, y):
        self.x_count+=1;
        self.tab[x][y] = 1
        
    def input_y(self, x, y):
        self.y_count+=1;
        self.tab[x][y] = 2
        
    def check_victory(self) -> str:
        value = 0
        if self.x_count + self.y_count > 4: # Se teve mais de 4 entradas
            if self.tab[0][0] == self.tab[1][1] == self.tab[2][2]:
                value = self.tab[0][0]
            if  self.tab[2][0] == self.tab[1][1] == self.tab[0][2]:
                value = self.tab[0][0]
            
            for i in range(3):
                if self.tab[i][0] == self.tab[i][1] == self.tab[i][2]:
                    value = self.tab[i][0]
                if self.tab[0][i] == self.tab[1][i] == self.tab[2][i]:
                    value = self.tab[0][i]
        if self.x_count + self.y_count > 8:
            return "Z"
        match value:
            case 0:
                return ""
            case 1:
                self.setVictory = "X"
                return self.setVictory
            case 2:
                self.setVictory = "Y"
                return self.setVictory