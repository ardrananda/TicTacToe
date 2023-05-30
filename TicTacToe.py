#importing modules
import pygame,sys
from pygame.locals import *

pygame.init()

#screen dimensions
screen_width=300
screen_height=300

#display screem
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Tic-Tac-Toe')

#define colors
green=(0,255,0)
blue=(0,0,255)

#variables
line_width=6
pos=[]
winner=None
draw=None
empty=None
game_over=False
x=1
o=2
player=x
board=[[None]*3,[None]*3,[None]*3]

clock=pygame.time.Clock()

#upload image
x_img=pygame.image.load('X.png')
o_img=pygame.image.load('O.png')

#scaling images according to the size of block available
x_img=pygame.transform.scale(x_img,(80,80))
o_img=pygame.transform.scale(o_img,(80,80))


#drawing grid
def draw_grid():
    bg=pygame.Color(255,255,210)
    grid=(50,50,50)
    screen.fill(bg)
    for i in range(1,3):
        pygame.draw.line(screen,grid,(0,i*100),(screen_width,i*100),line_width) #horizontal line
        pygame.draw.line(screen,grid,(i*100,0),(i*100,screen_height),line_width) #vertical line
        

#to print the result on screen
def result():
    global draw,winner,pos,game_over
    msg=""
    if winner:
        if winner==1:
            msg="   X won:)"
        elif winner==2:
            msg="   O won:)"
    if draw:
        msg="   Draw:("
    font=pygame.font.SysFont(None,40)
    text=font.render(msg,True, blue)
    pygame.draw.rect(screen,green,(screen_width//2-100,screen_height//2-60,160,50))
    screen.blit(text,(screen_width//2-100,screen_height//2-50))

    #to play again
    again_rect=Rect(screen_width//2-80,screen_height//2,160,50)
    again_txt="Play Again?"
    again_img=font.render(again_txt,True,blue)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img,(screen_width//2-80,screen_height//2+10))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if game_over==true:
                pos=pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    reset()
                

#to reset variables for new game
def reset():
    global game_over,pos,player,winner,draw,board
    game_over=False
    pos=[0,0]
    player=x
    winner=None
    draw=None
    board=[[None]*3,[None]*3,[None]*3]
    


#to check for the winner and draw a line to indicate the win
def Won():
    global board,winner,player
    f=0 #flag variable
    #checking in rows
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2] and board[row][0]!=empty:
            winner=board[row][0]
            pygame.draw.line(screen,(250,0,0),(0,(row+1)*100-(300/6)),(300,(row + 1)*100-(300/6)),4)
            f=1
            break
    
    #checking in columns
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!=empty:
            winner=board[0][col]
            pygame.draw.line(screen,(250,0,0),((col + 1)*100-(300/6),0),((col+1)*100-(300/6),300),4)
            f=1
            break

    #chechking primary diagonal
    if board[0][0]==board[1][1]==board[2][2]!=empty:
        winner=board[0][0]
        pygame.draw.line(screen,(250,0,0),(50,50),(250,250),4)
        f=1

    #checking secondary diagonal
    if board[0][2]==board[1][1]==board[2][0]!=empty:
        winner=board[0][2]
        pygame.draw.line(screen,(250,0,0),(50,50),(250,250),4)
        f=1
    
    game_over=True    
    if f==1:
        return True
    elif f==0:
        return False
        

#to check draw
def Draw():
    global board,winner,draw
    for i in range(3):
        for j in range(3):
            if board[i][j]==empty:
                draw=False
                return draw
    game_over=True
    draw=True
    return draw

#to update the state
def update():
    if Won():
        result()
    if Draw():
        result()


#to render the image at the clicked position
def get_img(row,col):
    global player,board
    if row==1:
        posy=15
    if row==2:
        posy=100+15
    if row==3:
        posy=200+15
    if col==1:
        posx=15
    if col==2:
        posx=100+15
    if col==3:
        posx=200+15
    #assigning the block on board its value
    board[row-1][col-1]=player
    #X's turn
    if player==x:
        screen.blit(x_img,(posx,posy))
        player=o
    #O's turn
    else:
        screen.blit(o_img,(posx,posy))
        player=x
    pygame.display.update()
        

#to get the position of coordinates of the clicked position to assign the
#respective sign at the clicked position
def input_block():
    pos=pygame.mouse.get_pos()
    x_pos=pos[0]
    y_pos=pos[1]

    #checking boundaries to determine the definite coordinate

    #assigning columns
    if x_pos<100:
        col=1
    elif x_pos<200:
        col=2
    elif x_pos<300:
        col=3
    else:
        col=None

    #assigning rows
    if y_pos<100:
        row=1
    elif y_pos<200:
        row=2
    elif y_pos<300:
        row=3
    else:
        row=None

    if(row and col and board[row-1][col-1] is None):
        get_img(row,col) #place image in the row and column determined
        update()

draw_grid()
while True:
 
    #adding event handlers
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            input_block()               
            
            
    pygame.display.update()
    clock.tick(30)

