from tkinter import *
from PIL import Image, ImageTk
names = []

class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
        background_color1="#f0dff2"
        background_color="#a3e4fa"

        self.title_image = Image.open("Title.png") #need to use Image if need to resize 
        self.title_image = self.title_image.resize((200, 100), Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(self.title_image)
        
        self.heading_label=Label(parent, image=self.title_image, border=0)
        self.heading_label.place(x=205, y=130) 
    
            #label for username
        self.user_label=Label(parent, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.place(x=120, y=260) 
    
            #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=230, y=320)
    
            #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="#fca8f9", command=self.name_collection)
        self.continue_button.place(x=260,y=360)


    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        #self.quiz_frame.destroy() #Destroy name frame then open the quiz runner




if __name__ == "__main__":
    root = Tk()
    root.title("General Knowledge Quiz") 
    root.geometry("600x500")
    bg_image = Image.open("Quiz.png") #need to use Image if need to resize 
    bg_image = bg_image.resize((600, 500), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l wi
    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear

