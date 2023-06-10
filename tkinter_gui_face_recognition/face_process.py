import customtkinter
import customtkinter as ctk 
import cv2
from PIL import ImageTk, Image
import tkinter as tk
from face_detect import main


#this class process and predict the face 
class ProcessFace():
    def __init__(self, frame, closing_event=None):
        self.frame= frame
        self.cap= cv2.VideoCapture(0)

        self.top_frame=customtkinter.CTkToplevel(self.frame)
        self.top_frame.geometry("400x300")
        self.top_frame.resizable(False,False)
        self.top_frame.protocol("WM_DELETE_WINDOW", self.closing)
        self.top_frame.grab_set()
        self.closing_event = closing_event

        self.photo_frame= tk.Frame(self.top_frame)
        self.photo_frame.place(x=100, y=80, width=250, height=200)

        self.label1= tk.Label(self.photo_frame)
        self.check= False
        


        label= ctk.CTkButton(self.top_frame, text="click to start", command= self.recognizer)
        label.place(x=10, y=10)

        label2= ctk.CTkButton(self.top_frame, text="click to stop", command= self.stop_camera)
        label2.place(x=250, y=10)

    def closing(self):
        self.top_frame.destroy()
        if self.closing_event is not None:
            self.cap.release()
            self.closing_event()

    def to_pil(self,img, label):
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(img)
        pic = ImageTk.PhotoImage(image)
        self.label1.configure(image=pic)
        self.label1.image = pic
        
        self.label1.pack()

    def display(self):
    # while True:
        self.check, frame= self.cap.read()
        frame= cv2.resize(frame, (250,200))
  
        self.to_pil(frame, self.label1)
        # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
        self.label1.after(20, self.display)

    def stop_camera(self):
        # if self.check:
        self.cap.release()
        self.label1.destroy()

    #recognize
    def recognizer(self):
        # path= ctk.filedialog.askopenfile()
        path= "model/trained_model1.yml"
        # print(os.path.split(path))
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(path)
        cascadePath = "haar_face.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        id = 0
        # add the list of names of your dataset here
        names = ['None','emmy'] 
        frame, bbox=main(self.cap)
        frame= cv2.resize(frame, (200,250)) 
      

        # img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if bbox: 
            x,y,w,h= bbox[0][1]
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                            
            # If confidence is less than 100 ==> "0" : perfect match 
            # But in case of insufficient trainable data i use 150
            if (confidence < 150):
                id = names[id]
                confidence = f"  {round(confidence - 50)}%"
            else:
                id = "unknown"
                confidence = f"  {round(confidence - 50)}%"
                            
            cv2.putText(frame,
                                 str(id), 
                                    (x+5,y-5), 
                                    font, 1, (255,255,255),  2)



        self.to_pil(frame, self.label1)
        self.photo_frame.after(20, self.recognizer)


            
