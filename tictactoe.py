from dependencies import *

def game(void) -> bool:
    tab = Tab()
    while tab.getWinner() is None:
        print(tab)
        print("Vez do X!")
        tab.input_x(input("Escreva o valor de X"), input("Escreva o valor de y"))
        print(tab)
        tab.checkVictory()
        print("Vez do O!")        
        tab.input_y(input("Escreva o valor de X"), input("Escreva o valor de y"))
        print(tab)
        tab.checkVictory()
        
        

    
if __name__ == "__main__":
    game()
        
            