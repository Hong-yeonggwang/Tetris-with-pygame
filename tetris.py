import pygame
import random
from datetime import datetime
from datetime import timedelta

#테스트

class Block: #블록의 필수 정보.
    block = [] ## 0번지 블럭 모양 1번지 색깔
    btype= [[0,1,0,1,1,0,1,0,0],[1,1,1,0,0,1,0,0,0],[1,1,1,1,0,0,0,0,0],
    [0,1,0,1,1,1,0,0,0],[0,0,0,1,1,1,0,1,0],[1,1,1,1],[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]]
    block_num = 0
    def makeBlock(self):  ##랜덤으로 블록을 만듦
        shape = random.randint(0,6)      
        color = random.randint(0,5)
        block = []
        block.extend([shape,color])
        # block.append([color])
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
            self.block_position = [8,1]
            self.block_color = block[0]
        elif block[0] == 1:
            self.block_size = 3
            self.block_shape = self.btype[1]
            self.block_position = [8,1]
            self.block_color = block[0]
        elif block[0] == 2:
            self.block_size = 3
            self.block_shape = self.btype[2]
            self.block_position = [8,1]
            self.block_color = block[0]
        elif block[0] == 3:
            self.block_size = 3
            self.block_shape = self.btype[3]
            self.block_position = [8,1]
            self.block_color = block[0]
        elif block[0] == 4:
            self.block_size = 3
            self.block_shape = self.btype[4]
            self.block_position = [8,1]
            self.block_color = block[0]
        elif block[0] == 5:
            self.block_size = 2
            self.block_shape = self.btype[5]
            self.block_position = [8,1]
            self.block_color = block[0]
        else : 
            self.block_size = 4
            self.block_shape = self.btype[6]
            self.block_position = [8,1]
            self.block_color = block[0]
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
                Board.board.append([[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0]]) #19개 원소
            else : 
                Board.board.append([[2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[2,0]])
    def __del__(self):
        Board.board = []
    def drawboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] == 0:
                    pygame.draw.rect(screen,(128,128,128),(108+15*j,15*i,15,15),4)

                else:
                    if self.board[i][j][1] == 0:
                        pygame.draw.rect(screen,(0,0,0),(108+15*j,15*i,15,15),4)
                    else:
                        pygame.draw.rect(screen,color[self.board[i][j][1]],(108+15*j,15*i,15,15),4)
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
   

# pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
color = [[255,0,0],[255,50,0],[255,255,0],[0,0,255],[0,255,0],[100,0,255],[255,255,255]] #빨주노초파남보 컬러코드
size = [500,500]
# screen = pygame.display.set_mode(size)
# done= False
clock= pygame.time.Clock()
Move_INTERVAL = timedelta(seconds=0.5)
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

def checkBlock(board):
    for i in range(1,len(board.board)):
            check = 0
            for j in range(1,len(board.board[i])):
                if board.board[i][j][0] == 1:
                    check += 1
                elif check == 17:
                    del board.board[i]
                    board.board.insert(1,[[2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[2,0]]) 

def setscreen():
    pygame.init()
    global screen 
    screen = pygame.display.set_mode(size)
    
    
# 4. pygame 무한루프
def runGame(): 
    global done,Move_INTERVAL,last_moved_time

    done= False

    screen.fill(WHITE)
    board = Board()
    blockCreat()
 
    
    while not done:
        clock.tick(500)
        board.insertBlockTOBoard(block[0])
        board.drawboard()
        pygame.display.update() 

        if Move_INTERVAL < datetime.now() - last_moved_time:
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
            last_moved_time = datetime.now()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                del board
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


# setscreen()
# runGame()
# pygame.quit()