import pygame
import random
import copy
from sys import exit
width,height=250,500
grid=25
pygame.init()
win=pygame.display.set_mode((width,height))
win2=pygame.display.set_mode((width,height))
font = pygame.font.Font(None, 30)
speed=60
speed2=150
RED = (255, 0, 0)
GRAY = (0,0,0)
ml=[]
phy = False
x1=0
r=0
sc=0
user_text=''
def over():
    print(ml)
    for i in range(100):
        if [i,0] in ml:
            return True


def score():
    scoresur=font.render('Score:'+str(sc),True,(1,1,200))
    scorerect=scoresur.get_rect(center= (60,40))
    win.blit(scoresur,scorerect)
    pygame.display.flip()

def newblock(l1):
    win.fill(GRAY)
    for i in l1:
        pygame.draw.rect(win, RED, (i[0] * grid, (i[1] ) * grid, grid, grid))
    for i in ml:
        pygame.draw.rect(win, RED, (i[0] * grid, (i[1] ) * grid, grid, grid))
    return True
def rot(r):
    if r==3:
        r=0
    else:
        r=r+1
    return r

def clearck(b):
    c=False
    for i in range(20):
        for j in range(10):
            if [j,i] in b:
                c=True
            else:
                c=False
                break
        if c==True:
            break
    if c:
        global sc
        sc=sc+5
        u=[]
        for k in b:
            if k[1]==i:
               u.append(k)
        for k in u:
            b.remove(k)
        for k in b:
            if k[1]<i:
                k[1]+=1

def xmove(l1,n,x1,ml):
    x=False
    if n==1:
        for i in range(len(l1)):
            if [l1[i][0]+1,l1[i][1]] in ml or l1[i][0]+1==10:
                x=False
                break
        else:
                x=True


    elif n==-1:
        for i in range(len(l1)):
            if [l1[i][0]-1,l1[i][1]] in ml or l1[i][0]-1==-1:
                x=False
                break
        else:
                x=True
                print(l1)

    else:
           pass

    if x:
        x1 += n
        for i in l1:
            i[0] += x1
        return x1
def move(z,b,y1):
    x=False
    for i in range(len(z)):
        if [z[i][0],z[i][1]+1] in b or z[i][1]*grid>=height-grid:
            x=True
            break
        else:
            x=False
    if x:
        global ml
        global phy
        ml=b+z
        l1,z=[],[]
        phy=False

    else:
        win.fill(GRAY)
        y1+=1
        for i in range(len(z)):
            z[i][1]+=y1
            pygame.draw.rect(win, RED, (z[i][0] * grid, z[i][1]* grid, grid, grid))
        for i in b:
            pygame.draw.rect(win, RED, (i[0] * grid, i[1]* grid, grid, grid))
    return y1

def but1():
    red_button = pygame.Surface((100, 50))
    red_button.fill((255, 0, 0))
    text = font.render('Click Me!', True, (255, 255, 255))
    red_button.blit(text, (5, 5))
    win2.blit(red_button, (100, 200))
    pygame.display.flip()
def main():
    score()
    global phy
    clock=pygame.time.Clock()
    run=True
    while run:
        score()
        clock.tick(speed)
        pygame.time.wait(speed2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xmove(l1, 1,x1,ml)
                if event.key == pygame.K_LEFT:
                    xmove(l1,-1,x1,ml)
                if event.key == pygame.K_UP:
                    r=rot(r)
                    l1 = lo[r]
                if event.key == pygame.K_DOWN:
                    move(l1,ml,y1)


        win.fill(GRAY)
        clearck(ml)

        if phy==False:
            r=0
            lo=copy.deepcopy(l)
            lo=random.choice(lo)
            l1=lo[r]
        if phy:
            l1=lo[r]

            move(l1,ml,y1)
        else:
            l1=lo[r]

            phy=newblock(l1)
            move(l1,ml,y1)

        pygame.display.flip()
        score()
        if over():
            run=False
            pygame.display.flip()
    run2=True
    run=False
    user_text = ''

    while run2:
        win.fill(GRAY)
        lead = font.render('Enter name:', True, (1, 1, 200))
        board = lead.get_rect(center=(80, 40))
        win2.blit(lead, board)
        name = font.render(user_text, True, (1, 1, 200))
        board2 = lead.get_rect(center=(80, 100))
        win2.blit(name, board2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run2=False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    user_text = user_text[:-1]

                elif event.key==pygame.K_RETURN:
                    run2=False
                else:
                    user_text += event.unicode
    run3=True
    while run3:
        win2.fill(GRAY)
        lead = font.render('Leaderboard:', True, (1, 1, 200))
        board = lead.get_rect(center=(80, 40))
        win2.blit(lead, board)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run3=False




Square=[[[5,0], [6,0], [5,1], [6,1]],[[5,0], [6,0], [5,1], [6,1]],[[5,0], [6,0], [5,1], [6,1]],[[5,0], [6,0], [5,1], [6,1]]]

Line=[[[4,0], [5,0], [6,0], [7,0]],[[4,0], [4,1], [4,2], [4,3]],[[4,0], [5,0], [6,0], [7,0]],[[4,0], [4,1], [4,2], [4,3]]]

Green_block=[[[5,0], [6,0], [4,1], [5,1]],[[5,0], [5,1], [6,1], [6,2]],[[5,0], [6,0], [4,1], [5,1]],[[5,0], [5,1], [6,1], [6,2]]]

Red_Block=[[[4,0], [5,0], [5,1], [6,1]],[[6,0], [5,1], [6,1], [5,2]],[[4,0], [5,0], [5,1], [6,1]],[[6,0], [5,1], [6,1], [5,2]]]

Orange_L=[[[6,0], [4,1], [5,1], [6,1]],
[[5,0], [5,1], [5,2], [6,2]],
[[4,0], [5,0], [6,0], [6,1]],
[[4,0], [5,0], [5,1], [5,2]]]

Blue_L=[[[4,0], [4,1], [5,1], [6,1]],
[[5,0], [6,0], [5,1], [5,2]],
[[4,0], [5,0], [6,0], [6,1]],
[[5,0], [5,1], [4,2], [5,2]]]

Purple_block=[[[5,0], [4,1], [5,1], [6,1]],
[[5,0], [5,1], [6,1], [5,2]],
[[4,0], [5,0], [6,0], [5,1]],
[[5,0], [4,1], [5,1], [5,2]]]

l=[Line,Square,Orange_L,Blue_L,Purple_block,Green_block,Red_Block]
main()