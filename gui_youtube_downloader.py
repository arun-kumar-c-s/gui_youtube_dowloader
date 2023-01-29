from tkinter import *
from tkinter import font
import os, sys, re, subprocess
from time import time

def runcmd(command,folder):
    '''command and folder are str '''
    if not os.path.exists('D:\\YTD\\'+folder+'\\'):
        os.makedirs('D:\\YTD\\'+folder+'\\')
    os.chdir('D:\\YTD\\'+folder+'\\')
    filename = 'ytdl_log'+str(time()).split('.')[0]+'.txt'
    f = open(filename,'w+')
    subprocess.Popen(command,stderr=sys.stderr,  stdout=sys.stdout, shell=True, bufsize=1)

def video():
    ''' get contents of textbox'''
    link = linkentry.get()
    if len(link)<60: link = link
    elif 'playlist' in link:
        return playlist()      ######## don't know if it's a good idea
    elif '?list=' in link:
        link = re.findall("(.*)\?list",link)
    elif '&list=' in link:
        link = re.findall("(.*)&list",link)
    command = 'youtube-dl ' + link[0]
    print(link)
    runcmd(command, 'Video')

def music():
    ''' get contents of textbox'''
    link = linkentry.get()
    if len(link)<60:
        link = link
    elif 'playlist' in link:
        return playlist()      ######## don't know if it's a good idea
    elif '?list=' in link:
        link = re.findall("(.*)\?list",link)
    elif '&list=' in link:
        link = re.findall("(.*)&list",link)
    command = 'youtube-dl -x --audio-format mp3 ' + link[0]
    print(link)
    runcmd(command, 'Music')


def playlist():
    ''' get contents of textbox'''
    link = linkentry.get()
    if len(link)<60:
        return video()
    elif 'playlist' in link:
        plid = re.findall("playlist\?list(.*)",link)
    elif '?list=' in link:
        plid = re.findall("\?list(.*)",link)
    elif '&list=' in link:
        plid = re.findall("&list(.*)",link)
    else: print('Error')
    link = 'https://www.youtube.com/playlist?list'+plid[0]
    command = 'youtube-dl -o "%(playlist_index)2d - %(title)s.%(ext)s" ' + link
    print(link)
    print(command)
    runcmd(command, 'Playlist')


root = Tk()
root.title("Youtube Downloader")
Label(root, text = 'YT Link :').grid(row=0,column=0)
helv = font.Font(family='Helvetica', size=14, weight='bold')


linkentry = Entry(root, width = 50)
linkentry.grid(row=0,column=1)

getbtn = Button(root,text = "▶", font = helv, padx=5, pady=2, command = video)
getbtn.grid(row=0,column=2,sticky=W)

musbtn = Button(root,text = "♪", padx=5, pady=2, font = helv, command = music)
musbtn.grid(row=0,column=3)

playbtn = Button(root,text = "📃", padx=5, pady=2, font = helv, command = playlist)
playbtn.grid(row=0,column=4)

root.mainloop()
