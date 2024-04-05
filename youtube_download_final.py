
from urllib import response
import pyshorteners as ps
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Indraneel's Mini Project")
Label(root,text = 'Youtube Video Link Converter/Downloader/Splitter', font ='arial 15 bold').pack()
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
def OpenNewWindow():
    url1 =YouTube(str(link.get()))
    newWindow = Toplevel(root)
    def Downloader1():
     
        url1 =YouTube(str(link.get()))
        video = url1.streams.all()
        video[3].download()
        Label(newWindow, text = 'DOWNLOADED', font = 'arial 20').place(x= 130 , y = 50)
         

    def Downloader2():
     
        url1 =YouTube(str(link.get()))
        video = url1.streams.all()
        video[22].download()
        Label(newWindow, text = 'DOWNLOADED', font = 'arial 20').place(x= 130 , y = 50)  

    def Downloader3():
     
     url1 =YouTube(str(link.get()))
     video = url1.streams.all()
     video[2].download()
     Label(newWindow, text = 'DOWNLOADED', font = 'arial 20').place(x= 130 , y = 50)  

    newWindow.geometry('500x300')
    newWindow.resizable(0,0)
    newWindow.title("Format Selection")
    Label(newWindow,text = 'Please select your preference',font = 'arial 20').pack()
    Button(newWindow,text='Only Video',font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader1).place(x=150 ,y = 200)
    Button(newWindow,text='Only Audio',font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader2).place(x=150 ,y = 150)
    Button(newWindow,text='Audio+Video',font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader3).place(x=150 ,y = 100)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = OpenNewWindow).place(x=180 ,y = 155)

def Converter():
    url2 = str(link.get())
    u = ps.Shortener().tinyurl.short(url2)
    disp = Entry(root,width = 38,font=('Arial',14))
    disp.pack(pady=2)
    disp.insert(0,f'{u}')
Button(root,text = 'CONVERT', font = 'arial 15 bold' ,bg='pale violet red', padx = 2, command = Converter).place(x=180 ,y = 110)

def splitter():
  from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

  url3 =YouTube(str(link.get()))
  title = url3.title
  required_video_file = title+".mp4"

  with open("times.txt") as f:
      times = f.readlines()

  times = [x.strip() for x in times] 

  for time in times:
      starttime = int(time.split("-")[0])
      endtime = int(time.split("-")[1])
      ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mp4")
Button(root,text = 'SPLIT', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = splitter).place(x=180 ,y = 200)
root.mainloop()

