import tkinter as tk
from tkinter import ttk
class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()


        def scarpy(string1, string2, string3):
            print(string1 + string2 + string3)
 
        
        self.label1 = tk.Label(self.frame, text = 'Paste the FIRST part of the website:')
        self.label1.pack(pady= 15)

        FirstPartVar= tk.StringVar()
        self.firstEntry = tk.Entry(self.frame, width = 10, textvariable=FirstPartVar)
        self.firstEntry.pack(pady= 15)
        
        self.label2 = tk.Label(self.frame, text = 'Paste the LAST part of the website:')
        self.label2.pack(pady= 15)

        LastPartVar= tk.StringVar()
        self.lastEntry = tk.Entry(self.frame, width = 50, textvariable = LastPartVar)
        self.lastEntry.pack(pady= 15)
        
        self.label3 = tk.Label(self.frame, text = 'The output format is:')
        self.label3.pack(pady= 15)

        formatVar=tk.StringVar()
        self.formatEntry = tk.Entry(self.frame, width = 10, textvariable=formatVar)
        self.formatEntry.insert(0, ".jpg")
        self.formatEntry.pack(pady= 15)

        self.button1 = tk.Button(self.frame, text = 'Start Scarpying', width = 25, command = lambda: scarpy(FirstPartVar.get(), LastPartVar.get(), formatVar.get()))
        self.button1.pack(pady= 15)

        self.progress = ttk.Progressbar(self.frame, length=200, mode="determinate")
        self.progress.pack(pady= 15)
        
        self.ProgressEntry = tk.Listbox(self.frame, height = 10, width = 50)
        self.ProgressEntry.pack(pady= 15, side="left")

        self.progressscroll = tk.Scrollbar(self.frame)
        self.progressscroll.pack(pady= 15, side="right")

        
        


    
        
    # def new_window(self):
    #     self.newWindow = tk.Toplevel(self.master)
    #     self.app = Demo2(self.newWindow)

# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()

def main(): 
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Scarpy_0.01")
    app = Demo1(root)
    
    root.mainloop()

if __name__ == '__main__':
    main()