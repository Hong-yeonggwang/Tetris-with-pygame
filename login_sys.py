import re
import sys

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
class QMessageBox:
    pass


def main():
    global user
    # user = []
    loadData()

    while True:
        print('-----------------------')
        print('1. 로그인')
        print('2. 회원가입')
        print('3. 비밀번호 변경')
        print('4. 프로그램 종료')
        print('-----------------------')

        select_no = int(input('옵션을 선택하세요. : '))

        if select_no == 1:
            cnt = 0

            while True:
                userInputId = str(input('아이디를 입력하세요 : '))
                userInputPwd = str(input('비밀번호를 입력하세요 : '))
                for a in user:
                    if a.id == userInputId and a.pwd == userInputPwd:
                        print('로그인 성공, 환영합니다!')
                        break
                    else:
                        cnt = cnt + 1
                        print('로그인 {}회 실패'.format(cnt))

                if cnt >= 3:
                    print('로그인 3회 실패로 인해 프로그램을 종료합니다!')
                    sys.exit()

                print()

        if select_no == 2:
            make_id()
            print('회원가입을 성공하였습니다. 환영합니다.\n')


        # if select_no == 3:
        #     uid = str(input('회원 아이디 : '))
        #     if uid in user:
        #         print(f'{uid} / {user[uid]}')
        #         n_pwd = edit_password(uid, user[uid])
        #         user[uid] = n_pwd
        #         print('비밀번호가 변경되었습니다.\n')
        #     else:
        #         print('등록된 아이디가 아닙니다.\n')
        #         continue

        if select_no == 4:
            saveData()
            print('프로그램을 종료합니다.')
            break

# main()