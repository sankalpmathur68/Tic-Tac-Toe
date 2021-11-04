import pygame
from pygame import rect
import time
from pygame.constants import MOUSEBUTTONDOWN, QUIT, RESIZABLE 
#initialization of library
pygame.init()
screen_x,screen_y = (720,480)
pygame.display.set_caption('TIC TAC TOE')
display_surface = pygame.display.set_mode((screen_x,screen_y),0,32)
black = (0,0,0)
font_any = pygame.font.SysFont('stencilstdopentype',30)
sound_pick = pygame.mixer.Sound('sound_pick.wav')
sound_pick.set_volume(0.1)
bg_music = pygame.mixer.Sound('sound_BGsong.wav')
bg_music.play(-1)
global XO
XO = 'x'
global locations
locations = [[None,None,None],[None,None,None],[None,None,None]]
x_img = pygame.image.load('x.png')
x_img_rect = x_img.get_rect()
o_img = pygame.image.load('o.png')
o_img_rect = o_img.get_rect()
# fonts 
def welcome_text():
    welcome_massage_lst = ['WELCOME','IN','THE','GAME','X','can','start']
    massages =[]
    loc = []
    for text in welcome_massage_lst:
        i =1
        welcome_massage = font_any.render(text,(0,0,0),(222,111,245))
        welcome_massage_rect = welcome_massage.get_rect()
        welcome_massage_rect.center =(screen_x-screen_x//8, screen_y//3 + i)
        loc.append(welcome_massage_rect)
        massages.append(welcome_massage)
    for i in range(7):
        display_surface.blit(massages[i],(screen_x-screen_x//4+10, screen_y//3 + i*40))
    pygame.display.update()
def print_msg(massage):
    display_surface.fill((255,255,255),(screen_x-screen_x//4,0,screen_x,screen_y))
    mssg_1 = font_any.render(massage,True,(0,0,0))
    mssg_rect = mssg_1.get_rect()
    mssg_rect.center = (screen_x-screen_x//8,screen_y//2-100)
    mssg_2 =font_any.render('Turn',True,(0,0,0))
    mssg_2_rect = mssg_2.get_rect()
    mssg_2_rect.center = (screen_x-screen_x//8,screen_y-screen_y//3)
    display_surface.blit(mssg_1,mssg_rect)
    display_surface.blit(mssg_2,mssg_2_rect)
    pygame.display.update()
def dsg():
    screen_x,screen_y = display_surface.get_size()
    white =(255,255,255) 
    green =(100,255,0) 
    display_surface.fill(white)
    pygame.draw.line(display_surface,black,(screen_x//4,0),(screen_x//4,screen_y),5)
    pygame.draw.line(display_surface,black,(screen_x//2,0),(screen_x//2,screen_y),5)
    pygame.draw.line(display_surface,green,((screen_x-screen_x//4),0),(screen_x - screen_x//4,screen_y),5)
    pygame.draw.line(display_surface,black,(0,screen_y//3),(screen_x-screen_x//4,screen_y//3),5)
    pygame.draw.line(display_surface,black,(0,screen_y-screen_y//3),(screen_x-screen_x//4,screen_y-screen_y//3),5)
def update_score(col,row):
    if  XO == 'o':
        locations[row-1][col-1] = 'cross'
    if XO == 'x':
        locations[row-1][col-1] = 'circle'
    check_winner()
def check_winner():
    winner = None
    for win in range(3):
        if locations[win][0] == locations[win][1] == locations[win][2] and locations[win][0] != None:
            winner = locations[win][0]

    for win_col in range(3):
        if locations[0][win_col] == locations[1][win_col] == locations[2][win_col] and locations[0][win_col] != None:
            winner = locations[win_col][0]

    if locations[0][0] == locations[1][1] ==  locations[2][2] and locations[1][1]!= None:
        winner = locations[1][1]

    if locations[0][2] == locations[1][1] ==  locations[2][0] and locations[1][1]!= None:
        winner = locations[1][1]

    for chk1 in range(3):
            if locations[0][chk1] != None and winner ==None:
                draw_match = True 
                
            else:
                draw_match = False
                
                break
    for chk2 in range(3):
            if locations[1][chk2] != None and winner ==None and draw_match==True:
                draw_match = True 
                
            else:
                draw_match = False
                
                break
    for chk3 in range(3):
            if locations[2][chk3] != None and winner ==None and draw_match==True:
                draw_match = True 
                
            else:
                draw_match = False
                
                break
    if draw_match == True:
        time.sleep(1)
        display_surface.fill((255,255,255))
        draw_msg = font_any.render("It's a draw",True,(0,0,0) )
        draw_msg_rect =draw_msg.get_rect()
        draw_msg_rect.center =(screen_x//2,screen_y//2)
        display_surface.blit(draw_msg,draw_msg_rect) 
        pygame.display.update()
        time.sleep(1)
        refresh()
    if winner != None and not draw_match:
        display_surface.fill((255,255,255),(screen_x-screen_x//4,0,screen_x,screen_y))
        msg = font_any.render(winner,True,(0,123,255))
        msg_1 = font_any.render('is the ',True,(0,123,255))
        msg_2 = font_any.render('winner ',True,(0,123,255))
        display_surface.blit(msg,(screen_x-screen_x//4,screen_y//2))
        display_surface.blit(msg_1,(screen_x-screen_x//4,screen_y//2+50))
        display_surface.blit(msg_2,(screen_x-screen_x//4,screen_y//2+100))
        pygame.display.update() 
        time.sleep(1)   
        refresh()
def draw(col,row):
    global XO
    for clm in range(4):
        for rw in range(4):
            copy_col = col
            copy_row = row
            if (clm,rw) == (col,row) and XO == 'x' :
                if copy_col ==3:
                    copy_col = 4
                if copy_col ==1:
                    copy_col = 0
                if copy_row == 3:
                    copy_row = 4
                if copy_row ==1:
                    copy_row = 0
                display_surface.blit(x_img,(screen_x//16 + copy_col*screen_x//8 ,screen_y//12 + copy_row*screen_y//6))
                sound_pick.play()

            if (clm,rw) == (col,row) and XO == 'o' :
                if copy_col ==3:
                    copy_col = 4
                if copy_col ==1:
                    copy_col = 0
                if copy_row == 3:
                    copy_row = 4
                if copy_row ==1:
                    copy_row = 0
                display_surface.blit(o_img,(screen_x//16 + copy_col*screen_x//8 ,screen_y//12 + copy_row*screen_y//6))
                sound_pick.play()

    if XO=='x':
        print_msg("O's")
        XO = 'o'
    else:
        print_msg("X's")
        XO ='x'
    update_score(col,row)
    pygame.display.update()
def clicked():
    x,y = event.pos
    screen_x,screen_y = display_surface.get_size()
    if x<screen_x//4 :
        col =1
    elif x<screen_x//2 :
        col = 2
    elif x<(screen_x-screen_x//4):
        col = 3
    if x<(screen_x-screen_x//4) and y<screen_y//3:
        row = 1
    elif x<(screen_x-screen_x//4) and y<screen_y-screen_y//3:
        row = 2
    elif x<(screen_x -screen_x//4) and y<screen_y:
        row = 3
    if locations[row-1][col-1] == None:
        draw(col,row)
def refresh():
    global locations,XO
    display_surface.fill((255,255,255))
    wait_msg = font_any.render('Wait for RESET',True,(0,0,0))
    wait_msg_rect = wait_msg.get_rect()
    wait_msg_rect.center =(screen_x//2,screen_y//2)
    display_surface.blit(wait_msg,wait_msg_rect)
    pygame.display.update()

    time.sleep(3)
    dsg()
    locations =[[None,None,None],[None,None,None],[None,None,None]]
    welcome_text()
    XO = 'x'
lines =True
welcome = True
for pos in locations:
    for i in pos:
        if i!= None:
            welcome = False
while True:
    # display_surface.fill((0,0,0),(screen_x-screen_x//4,0,screen_x,screen_y))
    for pos in locations:
        for i in pos:
            if i!= None:
                welcome = False
    if welcome == True:
        welcome_text()
    if lines:
        dsg()
        lines=False
    screen_x,screen_y = display_surface.get_size()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] < screen_x-screen_x//4:
                clicked()
    pygame.display.update()
    
    
    
