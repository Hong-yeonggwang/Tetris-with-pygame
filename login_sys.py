import re

class User:
    id = ''
    pwd = ''
    score = 0

    def __init__(self,id,pwd,score = 0):
        self.id = id
        self.pwd = pwd
        self.score = score
        
    def changePwd(self,pwd):
        self.pwd = pwd
    def updateScore(self,score):
        self.score = score

def chk_id(id):
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, id):
        return False
    return True

def chk_password(pwd):
    reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$'
    if not re.search(reg, pwd):
        return False
    return True

def loadData():
    global user
    user = []
    inf = open('tetrisMember.txt', 'r')
    for line in inf.readlines():
        a = line.rstrip().split() #줄바꿈 \n을 없애고 구분자를 스페이스로 둠
        user.append(User(a[0],a[1],a[2]))     
    inf.close()         

def saveData():
    outf = open('tetrisMember.txt','w')
    for a in user:
        outs = a.id +' '+ a.pwd+' '+str(a.score)+'\n'
        outf.writelines(outs)
    outf.close()

        
def make_id(userInputId,userInPutPwd):
# 비밀번호 생성
    user.append(User(userInputId,userInPutPwd))
