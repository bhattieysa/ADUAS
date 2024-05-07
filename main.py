from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from addFamilyMember import FamilyMember
from faceRecognition import FaceRecognition
import argparse
import datetime
import cv2
import os
import time


class MainPage:
    def __init__(self, master):
        self.heading=Label(master,height=2,text="Automatic Door Unlock & Alert System",relief="solid",font=("arial",15,"bold"),bg="royalblue",fg="white")
        self.heading.pack(fill=BOTH,pady=5,padx=5)

        #............menubar.....................

        self.menu=Menu(master)
        master.config(menu=self.menu)

        self.subm1=Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label="File",menu=self.subm1)
        self.subm1.add_command(label="Exit",command=self.Exit)

        self.subm2=Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label="Option",menu=self.subm2)
        self.subm2.add_command(label="About",command=self.about)

        #...........Body..............
        self.faceRecognition=Button(master,command=self.faceRecognition,text="Face Recognition",relief=RIDGE,font=("arial",10,"bold"),bg="brown",fg="black")
        self.faceRecognition.place(x=15,y=90)
        self.members=Button(master,command=self.familyMembers,text="Add Family Members",relief=RIDGE,font=("arial",10,"bold"),bg="brown",fg="black")
        self.members.place(x=300,y=90)
        
        # face=FaceRecognition()


#..........functions......

    def faceRecognition(self):
        face=FaceRecognition()
    
    def familyMembers(self):
        member=FamilyMember()
        
    
    def Exit(self):
        exit()
    
    def about(self):
        messagebox.showinfo("ADUAS","Developed By Eysa Azhar Contact No:- 03009603634")


def main():
    win=Tk()
    b=MainPage(win)
    win.title("ADUAS")
    win.geometry("640x480+80+50")
    win.config(background="#FFFFFF")
    win.resizable(False,False)
    win.mainloop()
if __name__=="__main__":
    main()


