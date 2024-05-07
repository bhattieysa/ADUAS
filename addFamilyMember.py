
from imutils.video import VideoStream
from tkinter import messagebox
from face_dataset import FaceScan

import cv2
import numpy as np

import PIL.Image
import os


import argparse
import time

from tkinter import *

class FamilyMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("480x320+80+50")
        self.config(background="#FFFFFF")
        self.resizable(False,False)
        self.title("ADUAS")
        
        self.menu=Menu(self)
        self.config(menu=self.menu)

        self.subm1=Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label="File",menu=self.subm1)
        self.subm1.add_command(label="Exit",command=self.Exit)

        self.subm2=Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label="Option",menu=self.subm2)
        self.subm2.add_command(label="About",command=self.about)

        #...........Body..............
        
        
        self.heading=Label(self,height=2,text="Automatic Door Unlock & Alert System",relief="solid",font=("arial",15,"bold"),bg="royalblue",fg="black")
        self.heading.pack(fill=BOTH,pady=5,padx=5)
        
        self.id=Label(self,text="Unique ID",font="ariel 15",fg="White",bg="blue")
        self.id.place(x=50,y=60)
        
        self.enter_id=Entry(self,width=30,bd=4)
        self.enter_id.place(x=170,y=60)
        
       
        
       
        
        self.scan=Button(self,text="Scan",command=self.Scan,relief=RIDGE,font=("arial",10,"bold"),bg="brown",fg="black")
        self.scan.place(x=190,y=200)
        
        self.train=Button(self,text="Training",command=self.Train,relief=RIDGE,font=("arial",10,"bold"),bg="brown",fg="black")
        self.train.place(x=190,y=260)
    def Exit(self):
        exit()
    
    def about(self):
        messagebox.showinfo("ADUAS","Developed By Eysa Azhar Contact No:- 03009603634",parent=self)
        
    def Scan(self):
        u_id=self.enter_id.get()
        
        
        if u_id=="":
            messagebox.showinfo("ADUAS","Unique Id Can't be Blank",parent=self)
           
        else:
            scan=FaceScan(u_id)
    def Train(self):
        path = 'dataset'
        

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

        # function to get the images and label data
        def getImagesAndLabels(path):

            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
            faceSamples=[]
            ids = []

            for imagePath in imagePaths:

                PIL_img = PIL.Image.open(imagePath).convert('L') # convert it to grayscale
                img_numpy = np.array(PIL_img,'uint8')

                id = int(os.path.split(imagePath)[1].split(".")[1])
                faces = detector.detectMultiScale(img_numpy)

                for (x,y,w,h) in faces:
                    faceSamples.append(img_numpy[y:y+h,x:x+w])
                    ids.append(id)

            return faceSamples,ids
        
                
        #messagebox.showinfo("ADUAS","[INFO] Training faces. It will take a few seconds. Wait ...",parent=self)
        
        faces,ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        # recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
        recognizer.save('trainer/trainer.yml')

        # Print the numer of faces trained and end program
        messagebox.showinfo("ADUAS","\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))),parent=self)
        
        
        
        
        
        
        
        


        
        
        
        
   
        

    




