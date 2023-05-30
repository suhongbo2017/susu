from pytube import * 
from pytube.cli import on_progress
from tkinter import *

win= Tk()
win.title('YTB_Download')
win.geometry('600x400+200+200')
win.config(bg='#5F9EA0')

lab_title= Label(win,text='YTB_Download',font='黑体 15',bg='#5F9EA0')
lab_title.pack(side=TOP)

lab_url= Label(win,text='输入地址:',bg='#5F9EA0')
lab_url.place(x=10,y=25)
ent_url= Entry(win,width=70)
ent_url.place(x=65,y=25)

lab_path= Label(win,text='输入地址:',bg='#5F9EA0')
lab_path.place(x=10,y=50)
ent_path= Entry(win,width=70)
ent_path.place(x=65,y=50)

progress= Label(text='')
progress.config(width=70)
progress.pack(side=BOTTOM)



def download_ytb():
    url= ent_url.get()
    path= ent_path.get()
    yt= YouTube(url,on_progress_callback=on_progress)
    try:
        streamyt=yt.streams.get_by_itag(22)
        if path == None:
            file_path= r'G:\youtube_download\mv'
            streamyt.download(file_path)
            pgs= yt.register_on_progress_callback(on_progress)
            progress.config(text=pgs)
        else:
            streamyt.download(path)
            pgs= yt.register_on_progress_callback(on_progress)
            progress.config(text=pgs)
    except:
        print('下载异常，稍后再试。')
        

btn_down= Button(text='下载',font='黑体 15',command= download_ytb)
btn_down.place(x=280,y=90)

win.mainloop()