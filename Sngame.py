import pygame
import numpy as np
import time
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

white = (255, 255, 255)
black = (0, 0, 0)


sn = []
length = 5
head = [0,0]

pain = 2
poin = 1
low = 0.5
point = 0

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def gos(x = 0,y = 0):
    print("\033[H\033[J")
    # print(f"\033[{x};{y}H",end="")
    # os.system("cls")
    # print()

def display(maps, point = 0):
    gos()
    pizz = ("#" * (maps.shape[0]+2 ))+ "\n#"
    for y in maps:
        for x in y:
            a = " "
            # a = "□"
            if x == 0:
                a = " "
            elif x > 0 and x < 1:
                a = "■"
            elif x == 1:
                a = "▤"
            else:
                a = "$"
            pizz+= a
        pizz+= "#\n#"
    pizz += ("#" * (maps.shape[0]+1 ))+ f"\n {point}"
    
    print(pizz)
def ful_up(na, pix = 10):
    xf =[]
    yf =[]
    for y in na:
        for i in range(pix):
            for x in y:
                for i in range(pix):
                    xf.append(x)
            yf.append(xf)
            xf =[]
    return yf

def len_sp(sn, lens:int):
    sn = sn[::-1][:lens][::-1]
    return sn

def Nuton(maps):
    # print(maps[1]+1)
    y=np.random.randint(0, maps.shape[0])
    x=np.random.randint(0, maps.shape[1])
    return [y,x]

def wig(poin = [0,0], poins = 0, maps = [], sn = [], nus = [], lens = 5 , point = 0):
    if poins == 1:
        a = [poin[0]+1,poin[1]]
    elif poins == 2:
        a = [poin[0],poin[1]+1]
    elif poins == 3:
        a = [poin[0]-1,poin[1]]
    elif poins == 0:
        a = [poin[0],poin[1]-1]
    # print(a)        
    try:
        for i in sn:
            if i == a:
                print("tail_Touch")
                raise
        if maps[a[0],a[1]] == 1:
            return False, a, lens, point
        if a[0] < 0 or a[1] < 0:
            raise
        if a[0] > maps.shape[0] or a[1] > maps.shape[1]:
            raise
        # print(nus[0])
        if nus[0] == a[0] and nus[1] == a[1]: 
            # print("apple")
            nus = Nuton(maps)
            lens += 1
            point += 1
            # print("apple")
    except:
        return False, a, nus, lens, point
    return True, a, nus, lens, point
_ = True
mapi = np.zeros([20,20])
nu = Nuton(mapi)

head = [10,10]
clock = pygame.time.Clock()
_ = True
while _:
    maps = mapi.copy()
    for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                poin = 0
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                poin = 3
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                poin = 2
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                poin = 1
                print(poin)
    
    _,head,nu, length, point = wig(head, poin, maps, sn, nus = nu, lens = length,point= point)
    
    screen.fill(black)
    pygame.draw.rect(screen, white, (head[1]*32, head[0]*32,32,32))
    # print(head)
    print((head[0]*32, head[1]*32,32,32))
    
    for heads in sn:
        pygame.draw.rect(screen, white, (heads[1]*32, heads[0]*32,32,32))
    pygame.draw.rect(screen, (255,0,0), (nu[1]*32, nu[0]*32,32,32))

    sn.append(head)
    sn = len_sp(sn, length)
    # pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    pygame.display.update()
    clock.tick(5)
    
    # time.sleep(1)

sys.exit()
