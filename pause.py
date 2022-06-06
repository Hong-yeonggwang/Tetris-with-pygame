import tkinter as t
import tetris

def click_quit():
    tetris.stop = False
    window.quit()
    window.destroy()
    
def setDisplay():
    global window
    window = t.Tk()
    window.geometry('500x500')
    quit_button = t.Button(window, text = "이어서", command = click_quit)
    quit_button.place( x = 100, y = 100)
    window.mainloop()
