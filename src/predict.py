import roboflow
import customtkinter as ctk
from tkinter import filedialog
import pathlib as pl

class App(ctk.CTk):
    def __init__(self, API_KEY):
        super().__init__()
        self.title("VSV_Cabel_Control")
        self.geometry("500x500")
        self.resizable(False, False)
        
        self.API_KEY = API_KEY
        
        self.__5_padding = {'padx': 5, 'pady': 5}
        
        self.font = ctk.CTkFont(family="Helvetica", size=16)
        
        
        self.title_label = ctk.CTkLabel(self,
                                        text="VSV Cabel Control",
                                        font=("Helvetica", 20))
        self.title_label.pack(**self.__5_padding)
        

        self.load_butt = ctk.CTkButton(self, 
                                       text="Browse file", 
                                       width=120,
                                       command=lambda: self.upload_img())
        self.load_butt.pack(**self.__5_padding)
        
        self.file_label = ctk.CTkLabel(self,
                                        text="File path:",
                                        font=("Helvetica", 16))
        self.file_label.pack(**self.__5_padding)
        
        self.file_name_label = ctk.CTkLabel(self,
                                        text="",
                                        font=("Helvetica", 16))
        self.file_name_label.pack(**self.__5_padding)
        
        self.predict_butt = None
        self.result = None
        self.confidence = None
        
        
    def upload_img(self):
        # open dialog window
        file_types = [('PNG files', '*.png'), ('JPG files', '*.jpg, *jpeg'), ('All files', '*')]
        tmp_file_path = filedialog.askopenfilename(title='Open a file', filetypes=file_types)

        if tmp_file_path == '':
            return
        else:
            self.file_path = tmp_file_path
        
        # update labels
        self.file_name_label.configure(text=self.file_path)
        
        if self.predict_butt is None:
            self.predict_butt = ctk.CTkButton(self, 
                                        text="Predict", 
                                        width=120,
                                        command=lambda: self.predict())
            self.predict_butt.pack(**self.__5_padding)
            
    def predict(self):
        rf = roboflow.Roboflow(api_key=self.API_KEY)

        project = rf.workspace().project("vsvcabelcontrol")
        model = project.version("1").model

        # optionally, change the confidence and overlap thresholds
        # values are percentages
        model.confidence = 50

        # predict on a local image
        prediction = model.predict(pl.Path(self.file_path))

        # Plot the prediction in an interactive environment
        
        pred_json = prediction.json()
        # print(pred_json['predictions'][0]['top'])
        # print(pred_json['predictions'][0]['confidence'])
        
        res = pred_json['predictions'][0]['top']
        conf = pred_json['predictions'][0]['confidence']
        
        if res == 'Pass':
            clr = "green"
        else:
            clr = "red"
        
        if self.result is None:
            self.result = ctk.CTkLabel(self,
                                        text=pred_json['predictions'][0]['top'],
                                        font=self.font,
                                        text_color=clr)
            self.result.pack(**self.__5_padding)
            self.confidence = ctk.CTkLabel(self,
                                        text=pred_json['predictions'][0]['confidence'],
                                        font=self.font,
                                        text_color=clr)
            self.confidence.pack(**self.__5_padding)
        else:
            self.result.configure(text=res, 
                                  font=self.font, 
                                  text_color=clr)
            self.confidence.configure(text=conf, 
                                      font=self.font, 
                                      text_color=clr)
            
        prediction.plot()
        
           
if __name__ == "__main__":
    app = App("!!API_KEY_HERE!!")
    app.mainloop()
    
    
    
    