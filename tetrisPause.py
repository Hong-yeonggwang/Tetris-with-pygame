import tkinter as t
import tetris
import sys

def quit():
    tetris.stop = False
    window.quit()
    window.destroy()
    
def displayWindow():
    global window
    window = t.Tk() 
    window.geometry("200x180") 
    window.resizable(width = False, height = False) 
    b7 = t.Button(window, text = "이어서", width = 15, height = 2 , command= quit)
    b7.place(x = 40, y = 30)
    b8 = t.Button(window, text = "게임 종료", width = 15, height = 2, command= sys.exit)
    b8.place(x = 40, y = 100)

    window.mainloop()

displayWindow()


