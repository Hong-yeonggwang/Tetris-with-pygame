import tkinter as t
import tetris

def click():
    tetris.setscreen()
    tetris.runGame()
    tetris.pygame.quit()

root = t.Tk()
root.geometry('500x500')

idlabel = t.Label(root, text="아이디")
idlabel.place(x = 10, y = 10)

pwdlabel = t.Label(root, text = "비밀번호")
pwdlabel.place(x= 10, y = 35)

idBox = t.Entry(root)
idBox.place( x = 70, y = 10)
pwdBox = t.Entry(root)
pwdBox.place(x = 70,  y = 35)
 
enter = t.Button(root, text="ENTER" , command= click)
enter.place( x = 220 , y = 23)

root.mainloop()