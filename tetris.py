import pygame
import random
from datetime import datetime
from datetime import timedelta

#테스트

class Block: #블록의 필수 정보. 블럭을 랜덤으로 생성한다.
    block = [] ## 0번지 블럭 모양 1번지 색깔
    btype= [[0,1,1,1,1,0,0,0,0],[1,1,0,0,1,1,0,0,0],[1,0,0,1,1,1,0,0,0,0],
    [0,0,1,1,1,1,0,0,0],[0,1,0,1,1,1,0,0,0],[1,1,1,1],[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]]
    def makeBlock(self):  ##랜덤으로 블록을 만듦
        shape = random.randint(0,6)      
        color = random.randint(0,5)
        block = []
        block.extend([shape,color])
        return block
    
class BlockG(Block): #게임안에서의 블록 
    block_size = 0  ##블록의 사이즈
    block_shape = [] ##블록의 모양이 저장된 1차원 배열
    block_position = [] # (블럭의 위치 정보
    block_color = 0
    def __init__(self): ## 생성자 생성시 Block에서 랜덤으로 블록을 만든후에 블럭의 모양과 사이즈를 결정함.
        b = Block()
        block = b.makeBlock()
        print(block)
        print("-----")
        print(self.block_position)
        if block[0] ==  0:
            self.block_size = 3
            self.block_shape = self.btype[0]
            self.block_position = [5,1]
            self.block_color = block[1]
        elif block[0] == 1:
            self.block_size = 3
            self.block_shape = self.btype[1]
            self.block_position = [5,1]
            self.block_color = block[1]
        elif block[0] == 2:
            self.block_size = 3
            self.block_shape = self.btype[2]
            self.block_position = [5,1]
            self.block_color = block[1]
        elif block[0] == 3:
            self.block_size = 3
            self.block_shape = self.btype[3]
            self.block_position = [5,1]
            self.block_color = block[1]
        elif block[0] == 4:
            self.block_size = 3
            self.block_shape = self.btype[4]
            self.block_position = [5,1]
            self.block_color = block[1]
        elif block[0] == 5:
            self.block_size = 2
            self.block_shape = self.btype[5]
            self.block_position = [5,1]
            self.block_color = block[1]
        else : 
            self.block_size = 4
            self.block_shape = self.btype[6]
            self.block_position = [5,1]
            self.block_color = block[1]
    def drawBlock(self,position): ## 실질적으로 화면에 블럭을 그려넣는 메소드.
        cnt = 0
        row_cnt = 0
        for i in range(len(self.block_shape)):
            if self.block_shape[i] == 1:
                pygame.draw.rect(screen,color[self.block_color],((cnt*20)+position[0],(row_cnt*20)+position[1],20,20),4)
                cnt += 1
                if cnt % self.block_size == 0:
                    row_cnt += 1
                    cnt = 0
            else:
                cnt += 1
                if cnt % self.block_size == 0:
                    row_cnt += 1
                    cnt = 0
    def turnBlock(self):
        tmp = [] 
        if self.block_size == 3:    
            tmp.append(self.block_shape[6])
            tmp.append(self.block_shape[3])
            tmp.append(self.block_shape[0])
            tmp.append(self.block_shape[7])
            tmp.append(self.block_shape[4])
            tmp.append(self.block_shape[1])
            tmp.append(self.block_shape[8]) 
            tmp.append(self.block_shape[5])
            tmp.append(self.block_shape[2])
            self.block_shape = tmp.copy()
        elif self.block_size == 4:
            tmp.append(self.block_shape[1])
            tmp.append(self.block_shape[2])
            tmp.append(self.block_shape[3])

            self.block_shape[1] = self.block_shape[4]
            self.block_shape[2] = self.block_shape[8]
            self.block_shape[3] = self.block_shape[12]
            self.block_shape[4] = tmp[0]
            self.block_shape[8] = tmp[1]
            self.block_shape[12] = tmp[2]
        elif self.block_size == 2:
            pass




class Board:
    board = []

    def __init__(self):
        for i in range(22):
            if i == 0 or i == 21:
                Board.board.append([[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0]]) #19개 원소
            else : 
                Board.board.append([[2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[2,0]])
    def __del__(self):
        Board.board = []
    def drawboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] == 0:
                    pygame.draw.rect(screen,(128,128,128),(130+20*j,20*i,20,20),4)

                elif self.board[i][j][0] == 2:
                    pygame.draw.rect(screen,(0,0,0),(130+20*j,20*i,20,20),4)
                else:
                    pygame.draw.rect(screen,color[self.board[i][j][1]],(130+20*j,20*i,20,20),4)
    def insertBlockTOBoard(self,block):  
        col_cnt = 0
        row_cnt = 0
        for i in range(len(block.block_shape)):
            if block.block_shape[i] == 1:
                if self.board[row_cnt+block.block_position[1]][col_cnt+block.block_position[0]][0] == 0 :
                    col_cnt += 1
                    if col_cnt % block.block_size == 0:
                        row_cnt += 1
                        col_cnt = 0
                else : 
                    return True
            else:
                col_cnt += 1
                if col_cnt % block.block_size == 0:
                    row_cnt += 1
                    col_cnt = 0
        col_cnt = 0
        row_cnt = 0
        for i in range(len(block.block_shape)):
            
            if block.block_shape[i] == 1:
                self.board[row_cnt+block.block_position[1]][col_cnt+block.block_position[0]] = [1,block.block_color]
                col_cnt += 1
                if col_cnt % block.block_size == 0:
                    row_cnt += 1
                    col_cnt = 0
            else:
                col_cnt += 1
                if col_cnt % block.block_size == 0:
                    row_cnt += 1
                    col_cnt = 0

    def delBlockToBoard(self,block):
        col_cnt = 0
        row_cnt = 0
        for i in range(len(block.block_shape)):
            if block.block_shape[i] == 1:
                self.board[row_cnt+block.block_position[1]][col_cnt+block.block_position[0]] = [0,0]
                col_cnt += 1
                if col_cnt % block.block_size == 0:
                    row_cnt += 1
                    col_cnt = 0
            else:
                col_cnt += 1
                if col_cnt % block.block_size == 0:
                    row_cnt += 1
                    col_cnt = 0

def blockCreat():
    block.append(BlockG())
    block.append(BlockG())
    block.append(BlockG())

def blockDel():
    del block[0]
    block.append(BlockG())

def checkBlock(board):
    global score
    for i in range(1,len(board.board)):
            check = 0
            for j in range(1,len(board.board[i])):
                if board.board[i][j][0] == 1:
                    check += 1
                elif check == 10:
                    del board.board[i]
                    board.board.insert(1,[[2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[2,0]]) 
                    score += 100
def checkGameOver(block):
    global done
    if block.block_position[1] == 1:
        done = True

def setscreen():
    pygame.init()
    global screen,size
    size = [500,500]
    screen = pygame.display.set_mode(size)
def drawNextBlock():
    if block[1].block_size == 3:
        block[1].drawBlock([405,55])
    elif block[1].block_size == 2:
        block[1].drawBlock([415,65])
    else:
        block[1].drawBlock([425,45])

    if block[2].block_size == 3:
        block[2].drawBlock([405,165])
    elif block[2].block_size == 2:
        block[2].drawBlock([415,175])
    else:
        block[2].drawBlock([425,155])


def drawSaveBlock(save):
    if len(save) == 0:
        pass
    else:
        if save[0].block_size == 3:
            save[0].drawBlock([35,115])
        elif save[0].block_size == 2:
            save[0].drawBlock([45,125])
        else:
            save[0].drawBlock([55,105])

def saveBlock(board,save):
    if len(save) == 0:
        save.append(block[0])
        board.delBlockToBoard(block[0])
        block[0].block_position = [5,1]
        blockDel()
    else:
        pass

def pullBlock(board,save):
    if len(save) == 0:
        pass
    else:
        board.delBlockToBoard(block[0])
        block[0].block_position = [5,1]
        block.insert(0,save[0])
        del save[0]

def drawbackground():
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),(20,100,90,90),4)
    pygame.draw.rect(screen,(0,0,0),(390,40,90,90),4)
    pygame.draw.rect(screen,(0,0,0),(390,150,90,90),4)
    font = pygame.font.SysFont("arial",30,True,True)
    text = font.render(str(score),True,(0,0,0))
    screen.blit(text,(10,10))

def gameover():
    gameover_font = pygame.font.SysFont("arial",70,True,True)
    conti_font = pygame.font.SysFont("arial",35,True,True)
    gameover = gameover_font.render("GAME OVER",True,(10,10,10),(255,255,255))
    conti = conti_font.render("press Any key",True,(10,10,10),(255,255,255))    
    screen.blit(gameover,(60,200))
    screen.blit(conti,(120,300))
    pygame.display.update()
    
def runGame(): 
    global done,Move_INTERVAL,last_moved_time,stop,block,gOver,color,size,score
    done= False
    color = [[255,0,0],[0,0,255],[0,255,0],[255,255,0],[255,51,153],[227,53,255]] 

    clock= pygame.time.Clock()
    Move_INTERVAL = timedelta(seconds=0.5)
    last_moved_time = datetime.now()
    block = []
    save = []
    score = 0
    stop = False
    gOver = True

    board = Board()
    blockCreat()

    while not done:
        drawbackground()
        clock.tick(500)
        board.insertBlockTOBoard(block[0])
        board.drawboard()
        drawNextBlock()
        drawSaveBlock(save) 
        pygame.display.update() 

        if Move_INTERVAL < datetime.now() - last_moved_time:
            board.delBlockToBoard(block[0])
            block[0].block_position[1] += 1
            if board.insertBlockTOBoard(block[0]) == True:
                block[0].block_position[1] -= 1
                board.insertBlockTOBoard(block[0])
                checkBlock(board)
                checkGameOver(block[0])
                blockDel()
            board.drawboard()
            print(block[0].block_position)
            pygame.display.update() 
            last_moved_time = datetime.now()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    board.delBlockToBoard(block[0])
                    block[0].block_position[1] += 1
                    if board.insertBlockTOBoard(block[0]) == True:
                        block[0].block_position[1] -= 1
                        board.insertBlockTOBoard(block[0])
                        checkBlock(board)
                        blockDel()
                    board.drawboard()
                    print(block[0].block_position)
                    pygame.display.update() 
                elif event.key == pygame.K_UP:
                    board.delBlockToBoard(block[0])
                    block[0].turnBlock()
                    if board.insertBlockTOBoard(block[0]) == True:
                        for i in range(3):
                            block[0].turnBlock()
                        board.insertBlockTOBoard(block[0])
                    board.drawboard()
                    pygame.display.update() 
                elif event.key == pygame.K_LEFT: 
                    board.delBlockToBoard(block[0])
                    block[0].block_position[0] -= 1  
                    if board.insertBlockTOBoard(block[0]) == True:
                        block[0].block_position[0] += 1
                        board.insertBlockTOBoard(block[0])  
                    board.drawboard()      
                    pygame.display.update()
                elif event.key == pygame.K_RIGHT:  
                    board.delBlockToBoard(block[0])
                    block[0].block_position[0] += 1
                    if board.insertBlockTOBoard(block[0]) == True:
                        block[0].block_position[0] -= 1
                        board.insertBlockTOBoard(block[0])
                    board.drawboard()
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    saveBlock(board,save)
                    drawSaveBlock(save)
                    pygame.display.update()
                elif event.key == pygame.K_d:
                    pullBlock(board,save)
                    pygame.display.update()
                elif event.key == pygame.K_ESCAPE:
                    stop = True
                    if stop == True:
                        import tetrisPause
                        tetrisPause.displayWindow()
    while gOver:
        gameover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gOver = False
            elif event.type == pygame.KEYDOWN:
                gOver = False

                        
# setscreen()
# runGame()
# pygame.quit()