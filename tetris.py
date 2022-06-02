import pygame
import random
from datetime import datetime
from datetime import timedelta
black = (1,1,1)

#테스트

class Block: #블록의 필수 정보.
    block = [] ## 0번지 블럭 모양 1번지 유형 3번지 블럭 색깔
    btype= [[0,1,0,1,1,0,1,0,0],[1,1,1,0,0,1,0,0,0],[1,1,1,1,0,0,0,0,0],
    [0,1,0,1,1,1,0,0,0],[0,0,0,1,1,1,0,1,0],[1,1,1,1],[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]]
    block_num = 0
    def makeBlock(self):  ##랜덤으로 블록을 만듦
        shape = random.randint(0,6)      
        color = random.randint(1,7)
        block = []
        block.extend([shape,color])
        return block
    
class BlockG(Block): #게임안에서의 블록 
    block_size = 0  ##블록의 사이즈
    block_shape = [] ##블록의 모양이 저장된 1차원 배열
    block_position = [] # (블럭의 위치 정보
    def __init__(self): ## 생성자 생성시 Block에서 랜덤으로 블록을 만든후에 블럭의 모양과 사이즈를 결정함.
        b = Block()
        block = b.makeBlock()
        print(block)
        print("-----")
        print(self.block_position)
        if block[0] ==  0:
            self.block_size = 3
            self.block_shape = self.btype[0]
            self.block_position = [8,1]
        elif block[0] == 1:
            self.block_size = 3
            self.block_shape = self.btype[1]
            self.block_position = [8,1]
        elif block[0] == 2:
            self.block_size = 3
            self.block_shape = self.btype[2]
            self.block_position = [8,1]
        elif block[0] == 3:
            self.block_size = 3
            self.block_shape = self.btype[3]
            self.block_position = [8,1]
        elif block[0] == 4:
            self.block_size = 3
            self.block_shape = self.btype[4]
            self.block_position = [8,1]
        elif block[0] == 5:
            self.block_size = 2
            self.block_shape = self.btype[5]
            self.block_position = [8,1]
        else : 
            self.block_size = 4
            self.block_shape = self.btype[6]
            self.block_position = [8,1]
    def drawBlock(self,position): ## 실질적으로 화면에 블럭을 그려넣는 메소드.
        cnt = 0
        row_cnt = 0
        for i in range(len(self.block_shape)):
            if self.block_shape[i] == 1:
                pygame.draw.rect(screen,(34,56,243),(self.block_position[0]+(cnt*15)+position[0],self.block_position[1]+(row_cnt*15)+position[1],15,15),1)
                cnt += 1
                if cnt % self.block_size == 0:
                    row_cnt += 1
                    cnt = 0
            else:
                cnt += 1
                if cnt % self.block_size == 0:
                    row_cnt += 1
                    cnt = 0
    def downBlock(sel,block):  ##블럭이 내려옴
        block[1] += 10
        block[0] += 50
    def turnBlock(self):
        if self.block_size == 3:    
            tmp = [] 
            tmp.append(self.block_shape[1])
            tmp.append(self.block_shape[2]) 
            tmp.append(self.block_shape[5])

            self.block_shape[1] = self.block_shape[3]
            self.block_shape[2] = self.block_shape[6]
            self.block_shape[5] = self.block_shape[7]
            
            self.block_shape[3] = tmp[0]
            self.block_shape[6] = tmp[1]
            self.block_shape[7] = tmp[2]
        elif self.block_size == 2:
            return

class Board:
    board = []

    def __init__(self):
        for i in range(25):
            if i == 0 or i == 24:
                Board.board.append([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]]) #19개 원소
            else : 
                Board.board.append([[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]])
    def drawboard(self,position):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] == 0:
                    pygame.draw.rect(screen,(0,255,0),(108+15*j,15*i,15,15),4)

                else:
                    if self.board[i][j][1] == 0:
                        pygame.draw.rect(screen,(255,0,0),(108+15*j,15*i,15,15),4)
                    elif self.board[i][j][1] == 1:
                        pygame.draw.rect(screen,(0,0,255),(108+15*j,15*i,15,15),4)
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
                self.board[row_cnt+block.block_position[1]][col_cnt+block.block_position[0]] = [1,1]
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

                

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
color = []
size = [500,500]
screen = pygame.display.set_mode(size)
done= False
clock= pygame.time.Clock()
last_moved_time = datetime.now()
block = []

def blockCreat():
    global block
    block.append(BlockG())
    block.append(BlockG())
    block.append(BlockG())

def blockDel():
    del block[0]
    block.append(BlockG())

def checkBlcok(self,block,board):
    pass 

# 4. pygame 무한루프
def runGame(): 
    global done

    screen.fill(WHITE)
    board = Board()
    blockCreat()
    board.insertBlockTOBoard(block[0])
    board.drawboard(block[0].block_position)
    pygame.display.update()  
    
    while not done:
        clock.tick(500)


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
                        blockDel()
                    board.drawboard(block[0].block_position)
                    print(block[0].block_position)
                    pygame.display.update() 
                elif event.key == pygame.K_UP:
                    board.delBlockToBoard(block[0])
                    block[0].turnBlock()
                    if board.insertBlockTOBoard(block[0]) == True:
                        block[0].turnBlock()
                        board.insertBlockTOBoard(block[0])
                    board.drawboard(block[0].block_position)
                    pygame.display.update() 
                elif event.key == pygame.K_LEFT: 
                    board.delBlockToBoard(block[0])
                    block[0].block_position[0] -= 1  
                    if board.insertBlockTOBoard(block[0]) == True:
                        block[0].block_position[0] += 1
                        board.insertBlockTOBoard(block[0])  
                    board.drawboard(block[0].block_position)      
                    pygame.display.update()
                elif event.key == pygame.K_RIGHT:  
                    board.delBlockToBoard(block[0])
                    block[0].block_position[0] += 1
                    if board.insertBlockTOBoard(block[0]) == True:
                        block[0].block_position[0] -= 1
                        board.insertBlockTOBoard(block[0])
                    board.drawboard(block[0].block_position)
                    pygame.display.update()
runGame()
pygame.quit()