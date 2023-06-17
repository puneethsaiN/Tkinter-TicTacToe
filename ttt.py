from tkinter import *

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player = 'X'
moves = 9

def checkWinnner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def isFull(board):
    c = 0
    for row in board:
        for col in row:
            if col == ' ':
                c+=1
    return c==0

def disableButtons():
    for i  in range(3):
            for j in range(3):
                btns[i][j]['state'] = DISABLED 

def setMove(x, y):
    global player
    btns[x][y].config(text=player)

    if(board[x][y]==' '):
        board[x][y] = player

    if checkWinnner(board, player)==True:
        print(player, 'won!')
        lbl.config(text='Game Over! player '+ player+' won')
        disableButtons()
        return
            
    if isFull(board)==True:
        lbl.config(text='Tie!')
        disableButtons() 
        return

    if player=='X':
        player = 'O'
        lbl.config(text='Current turn: O')
        
    else:
        player = 'X'
        lbl.config(text='Current turn: X')
   

m = Tk()
m.title('Tic Tac Toe')
m.geometry('360x375')
m.resizable()
btns = list()

for i in range(3):
    b = []
    for j in range(3):
        b.append(Button(m ,height=5,width=10, text=' ',background='yellow' ,command = lambda x=i, y=j : setMove(x,y)))   
    btns.append(b)
    
c = 0
for i  in range(3):
    for j in range(3):
        btns[i][j].grid(row=i, column=j,padx=15, pady=15)  
        c+=1

lbl = Label(text='Current turn : ')
lbl.grid(row=3,column=1)
m.mainloop()


    

    



