import tkinter as t
import tkinter.messagebox
import sys
from tkinter.tix import Tree
import login_sys as log
import tetris

now_user_id = ''
now_user_qwd = ''

def login():
    global now_user_id,now_user_qwd
    global login_cnt
    log.loadData()
    for a in log.user:
        if a.id == user_id.get() and a.pwd == user_pwd.get():
            slectWindow()
            now_user_id = user_id.get()
            now_user_qwd = user_pwd.get()
            window.destroy()
            return
    tkinter.messagebox.showerror("error","아이디와 비밀번호를 확인해주세요")
    login_cnt += 1
    if login_cnt == 3:
        sys.exit()
def join():
    if id_checkFlag == False:
        tkinter.messagebox.showerror("아이디 중복확인","아이디 중복확인을 해주세요")
    elif new_pwd.get() != check_pwd.get() and new_pwd.get() != None and check_pwd.get() != None:
        tkinter.messagebox.showerror("비밀번호 입력오류","비밀번호를 확인해주세요")
    elif log.chk_password(new_pwd.get()) == False:
        tkinter.messagebox.showerror("잘못된 형식","비밀번호 형식이 잘못됐습니다. 주의 사항을 확인해주세요.")
    else:
        log.make_id(new_id.get(),new_pwd.get())
        log.saveData()
        tkinter.messagebox.showinfo("환영합니다",f"{new_id.get()}님 반갑습니다!")
        joinWindow.quit()
        joinWindow.destroy()
def check_id():
    global id_checkFlag
    log.loadData()
    print(new_id.get())
    if log.chk_id(new_id.get()) == True:
        for a in log.user:
            if a.id == new_id.get():
                tkinter.messagebox.showerror("존재하는 아이디!",f" '{new_id.get()}' 은 이미 사용 중인 아이디 입니다.")
                return
    else:
        tkinter.messagebox.showerror("잘못된 형식","아이디 형식이 잘못됐습니다. 주의 사항을 확인해주세요.")
        return
    tkinter.messagebox.showinfo("","사용 가능한 아이디입니다.")
    id_checkFlag = True
    

def joinWindowdis():
    global new_id, new_pwd , check_pwd , id_checkFlag,joinWindow
    joinWindow = t.Tk()
    joinWindow.geometry("340x300")
    joinWindow.resizable(width = False, height = False)
    new_id, new_pwd , check_pwd = t.StringVar(), t.StringVar(), t.StringVar() 
    id_checkFlag = False
    t.Label(joinWindow, text = "  아이디" ).place(x = 53, y = 120)
    t.Label(joinWindow, text = "비밀번호").place(x = 50, y = 145)
    t.Label(joinWindow, text = "비밀번호 재확인").place(x = 10, y = 170)
    new_id = t.Entry(joinWindow, width = 15)
    new_id.place(x = 105, y = 120)
    new_pwd = t.Entry(joinWindow,width = 15)
    new_pwd.place(x = 105, y = 145)
    check_pwd = t.Entry(joinWindow,width = 15)
    check_pwd.place(x = 105, y = 170)
    t.Button(joinWindow, text = "아이디 중복확인", command = check_id).place(x = 225, y = 120)
    t.Button(joinWindow, text = "회원가입",width = 15,height = 2, command = join).place(x = 100, y = 200)
    t.Button(joinWindow, text = "회원가입 주의사항",width = 15, command = changePwd).place(x = 100, y = 250)
    joinWindow.mainloop()


def rule():
    tkinter.messagebox.showinfo("게임 규칙 설명", "1.블록을 쌓아 가로 1줄을 모두 채우게 되면 블록이 사라자면서 100점을 얻습니다.\n2.방향키를 통해 위치를 조정할 수 있습니다.\n3.위쪽으로는 블록을 이동시키지 못합니다.\n4.위쪽 방향키를 누르면 블럭을 회전할 수 있습니다.\n5.s를 통해 현재 블럭을 저장할 수 있고 d를 통해 저장된 블럭을 움직일 수 있습니다.\n 최대로 점수를 획득보세요! ")

def update_score():
    for a in log.user:
        if a.id == now_user_id:
            if int(a.score) < tetris.score:
                a.score = str(tetris.score)
                return True
def startGame():
    tetris.setscreen()
    tetris.runGame()
    tetris.pygame.quit()
    if update_score() == True:
        tkinter.messagebox.showinfo("신기록 갱신.",f"축하합니다. {tetris.score}점으로 신기록 경신했습니다.")
    user_select = tkinter.messagebox.askyesno("","다시 하시겠습니까?")
    if user_select == True:
        startGame()
    

def mainWindow():
    global user_id,user_pwd,login_cnt,window
    login_cnt = 0
    window = t.Tk()
    window.geometry("500x530")
    window.resizable(width = False, height = False) 
    user_id, user_pwd = t.StringVar(), t.StringVar()
    t.Label(window, text = "Username:").place(x = 110, y = 290)
    t.Label(window, text = "Password:").place(x = 110, y = 320)
    user_id = t.Entry(window)
    user_id.place(x = 200, y = 290)
    user_pwd = t.Entry(window)
    user_pwd.place(x = 200, y = 320)
    t.Button(window, text = "Login",width = 7, height = 2,command = login).place(x = 370, y = 295)
    t.Button(window, text = "회원가입", width = 15, height = 2, command = joinWindowdis).place(x = 200, y = 365)
    t.Button(window, text = "테트리스 규칙", width = 15, height = 2, command = rule).place(x = 200, y = 410)
    t.Button(window, text = "나가기", width = 15, height = 2, command=sys.exit).place(x = 200, y = 455)

    image = t.PhotoImage(file = "C:/python/Tetris-with-pygame/테트리스.png", master = window)
    t.Label(image = image).place(x = 70 , y = 0)


    window.mainloop()
def getUserScore():
    for a in log.user:
        if a.id == now_user_id:
            user_score = a.score
    return user_score

def userInfo():
    tkinter.messagebox.showinfo("개인정보 확인", f"1.id = {now_user_id}\n2.Password: {now_user_qwd}\n3.bestscore: {str(getUserScore())}")

def changePwd():
    for a in log.user:
        if a.id == now_user_id:
            if a.pwd == beforepassword.get():
                a.changePwd(afterpassword.get())
                tkinter.messagebox.showinfo("비밀번호 변경", "변경 성공")
                log.saveData()
                return            
    tkinter.messagebox.showerror("비밀번호 오류!", "기존 비밀번호를 확인해주세요")
    

def changePwdWindow(): 
    global beforepassword, afterpassword
    settingwindow = t.Tk() 
    settingwindow.geometry("500x500")
    settingwindow.resizable(width = False, height = False)
    beforepassword, afterpassword = t.StringVar(), t.StringVar() 
    t.Label(settingwindow, text = "변경 전 비밀번호:").place(x = 100, y = 210)
    t.Label(settingwindow, text = "변경 후 비밀번호:").place(x = 100, y = 240)
    beforepassword = t.Entry(settingwindow)
    beforepassword.place(x = 210, y = 210)
    afterpassword = t.Entry(settingwindow)
    afterpassword.place(x = 210, y = 240)
    t.Button(settingwindow, text = "변경", command = changePwd).place(x = 370, y = 220)
    settingwindow.mainloop()


def slectWindow():
    setWindow = t.Tk()
    setWindow.geometry("500x500") 
    setWindow.resizable(width = False, height = False) 
    t.Button(setWindow, text = "게임 시작", width = 15, height = 2, command = startGame).place(x = 200, y = 75)
    t.Button(setWindow, text = "회원 정보", width = 15, height = 2, command=userInfo).place(x = 200, y = 225)
    t.Button(setWindow, text = "비밀번호 변경", width = 15, height = 2, command = changePwdWindow).place(x = 200, y = 375)
    

mainWindow()

