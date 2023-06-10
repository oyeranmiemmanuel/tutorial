import cv2
import time, os
import tkinter
from tkinter import DISABLED, StringVar, NORMAL, IntVar 
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import messagebox
from face_detect import main as mn
from face_detect import img_bbox
import numpy as np 
from face_process import ProcessFace
import customtkinter
import cv2
import numpy as np
import mediapipe as mp



class App(ctk.CTk):
    def __init__(self,geometry=('900x600')):

        self.root= ctk.CTk()
        self.root.geometry(geometry)
        self.root._set_appearance_mode("dark")
        self.frame_1 = ctk.CTkFrame(master=self.root, width=400, height=70)
        self.frame_2 = ctk.CTkFrame(master=self.root, width=400, height=300) #fg_color='red'
        self.frame_3 = ctk.CTkFrame(self.root, width=300, height=350)
        self.frame_1.grid(padx=20, pady=20, row=0, column=1, sticky="nsew")
        self.frame_2.grid(padx=20, pady=80, row=0, column=1, sticky="nsew")
        self.frame_3.grid(padx=500, pady=150, row=0, column=1, sticky="nsew")
        self.toplevel_window = None
        self.img= cv2.VideoCapture("face1.mp4")
        self.delay= 1
        self.cap= cv2.VideoCapture(0)
        self.is_not_open= True
        self.Id= StringVar()
        self.name= StringVar()
        self.sampleNum=0

        # self.frame, self.bbox= mn('face1.mp4')
        



    #main frame that display
    def main(self):
        self.folder_path= StringVar()
        
        countries = ['Single Face', 'Multiple Face']
        self.variable = tkinter.StringVar()
        self.variable.set('Single Face')
        self.toplevel_window = None


        change_bg_color= ctk.CTkButton(self.root, text="change background", command= lambda: customtkinter.set_appearance_mode("dark"))
        change_bg_color.place(x=500, y=10)

        label1= ctk.CTkLabel(self.frame_1, corner_radius=20, font=('Arial', 30, 'bold'), \
                                                    text_color='red', text='New Era Technology')
        info_label= ctk.CTkLabel(self.frame_2, text="Select a  Person Id and Name; If Pics already taken", font=('Times', 15))
        info_label.place(x=50, y=10)
        label1.place(x=50, y=10)

        self.width, self.height= 300, 350

        self.optionmenu_1 = ctk.CTkOptionMenu(self.frame_2, variable=self.variable, values=countries)
        self.optionmenu_1.place(x=400, y=10)

        self.recog_btn= ctk.CTkButton(self.frame_2, text="Start Recognizer", command= self.open_toplevel)
        self.recog_btn.place(x=600, y=10)


        self.train_no_labels= ctk.CTkLabel(self.frame_2, font=("Arial", 18))
        

        id_label= ctk.CTkLabel(self.frame_2, text="Enter Id: ", font=ctk.CTkFont("Times", 18, weight="bold", slant="italic", underline=True))

        self.label1 = tkinter.Label(self.frame_3)
        self.label1.grid(row=0, column=0)


        self.id_entry= ctk.CTkEntry(self.frame_2, width=150, textvariable=self.Id)
        # self.id_entry = tkinter.Entry(self.frame_2, validate="key", width=20, border=1)
        # self.id_entry['validatecommand'] = (self.id_entry.register(self.testVal),'%P','%d')	
        self.id_entry.place(x=200, y=50)


        id_label.place(x=20, y=50)
        
        name_label= ctk.CTkLabel(self.frame_2, text="Enter Name: ", font=ctk.CTkFont("Times", 18, weight="bold", slant="italic", underline=True))
        self.name_entry= ctk.CTkEntry(self.frame_2, validate="key" , textvariable=self.name,  width=150)

        name_label.place(x=20, y=100)
        self.name_entry.place(x=200, y=100)

        select_folder_btn= ctk.CTkButton(self.frame_2, corner_radius=2, height=30, border_width=0, text="Select Folder",
                                fg_color="#228da8", command=self.open_folder)
        select_folder_btn.place(x=20, y=150)

        select_folder_btn= ctk.CTkButton(self.frame_2, corner_radius=2, height=30, border_width=0, text="Stop Camera",
                                fg_color="#228da8", command=self.stop_camera)
        select_folder_btn.place(x=250, y=150)



        self.take_images_btn= ctk.CTkButton(self.frame_2, corner_radius=2, height=30, border_width=0, text="Take Images",
                                fg_color="#228da8", command=self.display ) 
        self.take_images_btn.place(x=20, y=210)

        train_image_btn= ctk.CTkButton(self.frame_2, corner_radius=2, height=30, border_width=0, text="Train Images",
                                fg_color="#228da8", command=self.trainimg) 
        train_image_btn.place(x=250, y=210)

        self.folder_path_entry= ctk.CTkEntry(self.frame_2, textvariable=self.folder_path, width= 400, state=DISABLED)
        self.folder_path_entry.place(x=20, y=250)

        self.notification_label= ctk.CTkLabel(self.frame_2, font=('Arial', 26), text_color='green')


        self.root.mainloop()
        
        

    #convert images to Pillow image and display it on the given label 
    def to_pil(self,img, label):
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(img)
        pic = ImageTk.PhotoImage(image)
        label.configure(image=pic)
        label.image = pic
        
        label.pack()


    #show the frame for getting images 
    def display(self):
    # while True:
        # frame, bbox=mn(self.cap) 
        frame, bbox=mn(self.cap) 
  
        self.to_pil(frame, self.label1)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if bbox: 
            if self.sampleNum < 401:
                self.write_to_file('dataset',img, bbox[0][1], self.name_entry.get(), self.id_entry.get())
            else:
                self.notification_label.place(x=20, y=280)
                self.notification_label.configure(text='Its 400')
        self.label1.after(20, self.display)

    #check if id_entry is only a digit
    def testVal(self, inStr,acttyp):
        if acttyp == '1': #insert
            if not inStr.isdigit():
                return False
        return True
            
    # open directory
    def open_folder(self):
        folder= ctk.filedialog.askdirectory()
        self.folder_path.set(folder)

    #wrtie image to path_name folder
    def write_to_file(self, path_name, img, roi, Name, Id):
        if self.name_entry.get():
            if self.check_path(path_name):
                # gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                x,y,w,h= roi
                roi= img[y-10:y + h+10, x-10:x + w+10]
                cv2.imwrite(f"{path_name}/" + Name + "." + Id + '.' + str(self.sampleNum) + ".jpg", roi)
                # incrementing sample number
                self.sampleNum+=1
                print(self.sampleNum)

    # checks if a peron name already exist,but we're not using it
    def check_name(self, name):
        all_name=os.listdir("dataset")
        for i in all_name:
            if name in i:
                return "Exists"
        else:
            return "Not_Exists"

    # check if a path already exist
    def check_path(self, path_name):
        if os.path.exists(path_name):
            return True
        else:
            os.mkdir(path_name)
            return True


    #generate numpy images and their coresponding label
    # returns faceSamples, Ids, number 
    def getImagesAndLabels(self):

        # create empth face list
        all_name= []
        faceSamples = []
        number= []  
        Ids = [] 
        path= "dataset"
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        if self.variable.get() =='Single Face':
            try: 

                spec_name= self.name_entry.get()
                spec_id= int(self.id_entry.get())
                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

                if spec_name and spec_id:
                    if os.path.exists(path):
                            # create empty ID list
                            
                        spec_path=os.path.split(imagePaths[0])
                        spec= spec_path[1].split('.')

                        if spec_name==spec[0] and str(spec_id)==spec[1]:
                            
                            # now looping through all the image paths and loading the Ids and the images
                            # print(toge)
                            for imagePath in imagePaths:
                                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                                name = os.path.split(imagePath)[-1].split(".")[0]
                                # loading the image and converting it to gray scale
                                #but already a gray
                                # pilImage = Image.open(imagePath).convert('L')
                                pilImage = Image.open(imagePath)
                                # Now we are converting the PIL image into numpy array
                                imageNp = np.array(pilImage, 'uint8')

                                # getting the Id from the image
                                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                                #getting the image number 
                                identity= int(os.path.split(imagePath)[-1].split(".")[2])

                                # extract the face from the training image sample
                                faces = detector.detectMultiScale(imageNp)

                                for (x, y, w, h) in faces:
                                    faceSamples.append(imageNp[y:y + h, x:x + w])
                                    number.append(identity)
                                    Ids.append(Id)

                            # print(len(faceSamples), len(Ids), len(number))


                            self.train_no_labels.place(x=20, y=280)
                            self.train_no_labels.configure(text=f"There are {len(number)} trainable Images")
                            return faceSamples, Ids, number

                            # print(faceSamples, Ids, number)

                        else:
                            messagebox.showerror("error", "invalid Id or Name")
            except TypeError:
                pass                     


                    

        else:
            if self.folder_path.get():
                imageP= self.folder_path.get()
                imagePaths= [os.path.join(imageP, f) for f in os.listdir(imageP)]
                # print(imagePaths)
                
                for imagePath in imagePaths:
                    # loading the image and converting it to gray scale
                    pilImage = Image.open(imagePath).convert('L')
                    # Now we are converting the PIL image into numpy array
                    imageNp = np.array(pilImage, 'uint8')
                    # getting the Id from the image

                    Id = int(os.path.split(imagePath)[-1].split(".")[1])
                    identity= int(os.path.split(imagePath)[-1].split(".")[2])

                    # extract the face from the training image sample
                    faces = detector.detectMultiScale(imageNp)
                    # faces= main(imageNp)
                    # If a face is there then append that in the list as well as Id of it
                    for (x, y, w, h) in faces:
                        faceSamples.append(imageNp[y:y + h, x:x + w])
                        number.append(identity)
                        Ids.append(Id)
                        # print(Ids, faceSamples, number)


                self.train_no_labels.place(x=20, y=280)
                self.train_no_labels.configure(text=f"There are {len(number)} trainable Images")
                

                return faceSamples, Ids, number, "multiple"
                # print(faceSamples, Ids, number)

            else:
                messagebox.showerror("error", "Please specify a folder PATH")




    # get the numpy images and label, trains it and save it in the model dir
    def trainimg(self):

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        global detector
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        global faces,Id
        faces, Id, number, multiple = self.getImagesAndLabels()
        ask= messagebox.askyesno("Confirm", message=f"do you want to continue with {len(number)} trainable images")
        
        if ask:
            try:
                if multiple:
                    recognizer.train(faces, np.array(Id)) 
                    path= "model"
                    self.check_path(path)
                                
                    recognizer.save(f"{path}/trained_model {multiple}.yml")
                    res = "Model Trained"  # +",".join(str(f) for f in Id)
                    self.train_no_labels.configure(text=res,  width=50, font=('times', 18, 'bold'))
                    # self.notification_label.place(x=20, y=350)



                Ids= Id[0]
                if Ids:
                    recognizer.train(faces, np.array(Id)) 
                    path= "model"
                    self.check_path(path)
                            
                    recognizer.save(f"{path}/trained_model {Ids}.yml")
                    res = "Model Trained"  # +",".join(str(f) for f in Id)
                    self.train_no_labels.configure(text=res,  width=50, font=('times', 18, 'bold'))
                    # self.notification_label.place(x=20, y=350)

                else:
                    messagebox.showerror("Error", "Please specify an Id Number")


            except Exception as e:
                q='An Error Occur'
                self.train_no_labels.configure(text=q,  width=50, font=('times', 18, 'bold'))
                self.notification_label.place(x=20, y=350)
        else:
            pass




    #stops the camera feed
    def stop_camera(self):
        self.cap.release()
        self.label1.destroy()
        



    def open_toplevel(self):
        if self.toplevel_window is None:  # create toplevel window only if not already open
            self.toplevel_window= ProcessFace(self.root, closing_event= self.toplevel_close_event)

    def toplevel_close_event(self):
        self.toplevel_window = None









if __name__=='__main__':
    app= App()
    app.main()
    