from pathlib import Path
import os
import time
from tkinter import *
import pyscreenrec
import pyautogui
import datetime


root= Tk()
root.geometry('400x600')
root.title("Screen Recorder")


date= datetime.datetime
general_path= "C:/Users/75677/Desktop/screen recorder"


def start_rec():
    file=Filename.get()

    if not (general_path):
        os.mkdir(general_path)

    new_path=os.path.join(general_path,"Videos")
    if os.path.exists(new_path):
        os.chdir(new_path)
        rec.start_recording(str(file+ " .mp4"), 3)
    else:        
        os.mkdir(new_path)
        os.chdir(new_path)
        rec.start_recording(str(file+ " .mp4"), 3)

    status.set('Recording Start')

def pause_rec():
    rec.pause_recording()

    status.set('Recording Pause')

def resume_rec():
    rec.resume_recording()
    status.set("Recording Resume")

def stop_rec():
    rec.stop_recording()
    status.set('Recording stopped and saved')
    # new_path=os.path.join("Videos")
    # os.chdir(general_path)

def screenshot():
    d= date.now()
    d= d.strftime("%I-%S")
    d= str(d)
    print(d)
    new_path= os.path.join(general_path,"Screenshots")
    if not (general_path):
        os.mkdir(general_path)
    if os.path.exists(new_path):
        image= Filename.get()

        status.set("Waiting for five seconds before screenshot")
        time.sleep(2)
        # os.chdir(new_path)

        status.set("Waiting for five seconds before screenshot")
        path= f'{new_path}/{image}-{d}'
        pyautogui.screenshot(f'{path}.jpg')
        status.set("Screenshot taken and saved")
        # os.chdir(general_path)
    else:
        os.mkdir(new_path)
        # os.chdir(new_path)
        image= Filename.get()
        status.set("Waiting for five seconds before screenshot")
        time.sleep(2)
        path= f'{new_path}/{image}-{d}'
        image= pyautogui.screenshot(f'{path}.jpg')
        status.set("Screenshot taken and saved")
        # os.chdir(general_path)


        
rec= pyscreenrec.ScreenRecorder()


icon_img= PhotoImage(file='images/play.PNG')
root.config(bg="white")
root.resizable(False,False)
root.iconphoto(False, icon_img)
Filename= StringVar()

original_img= PhotoImage(file='images/logo2.png')

# original_img.zoom(30,30)
Label(root, image= original_img).place(x=-10, y=-10)

Label(root, text='Video Recorder', font='arial 20', fg='red').place(x=100, y=40)

Label(root, text="Type Your Video/Screenshot Name Below", fg='black', bg='#fff',font='arial 13').place(x=60, y=120)

text_entry= Entry(root, textvariable= Filename, font='arial 15', ) 
text_entry.place(x= 80, y= 180)

# start_img= PhotoImage(file='start.PNG')
start_btn=Button(root, text="START",  command= start_rec, bd=0, fg="red",bg="pink", activebackground='green')
start_btn.place(x=170, y=230)



start_btn=Button(root, text="SCREENSHOT",  command= screenshot, bd=0, activebackground='red', background="yellow")
start_btn.place(x=150, y=290)

# play_img= PhotoImage(file='play.PNG')
# play_btn= Button(root, text= "PLAY", )
# play_btn.place(x=40, y=400)


pause_img= PhotoImage(file='images/pause.PNG')
pause_btn= Button(root, text= "PAUSE",   command= pause_rec)
pause_btn.place(x=120, y=400)

# resume_img= PhotoImage(file='resume.PNG')
resume_btn= Button(root, text="RESUME",    command= resume_rec)
resume_btn.place(x= 190, y=400)

# stop_img= PhotoImage(file='stop.PNG')
stop_btn= Button(root, text= "STOP",  command= stop_rec)
stop_btn.place(x=270, y=400)

status= StringVar()
status.set("Press Start to start")
status_lbl=  Label(root, textvariable= status, font= 'arial 13', )
status_lbl.place(x=100,y=500)
# confirm.set('Press Start to Start')


root.mainloop()