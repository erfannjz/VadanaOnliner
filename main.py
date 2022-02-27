import tkinter as tk
import webbrowser as wb
from time import strftime
from utils.Onliner import Vadana

proc = None

class Panel(tk.Tk):
    btn_state, time_state = False, False

    def __init__(self):
        super().__init__()

        # window center config
        self.app_width = 300
        self.app_height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2) - 40

        # window config
        self.title('VadanaOnliner')
        self.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.configure(bg='#2b2e37')
        self.resizable(0, 0)
        self.iconbitmap('images/azaduni.ico')
    

    def label(self):
        self.label1 = tk.Label(self, text='VadanaOnliner', font=('MADESoulmazeBrush', 25),
        background='#2b2e37', foreground='#d8dbe4')
        self.label1.place(x=50, y=50)
        self.label2 = tk.Label(self, text='__________________________________', background='#2b2e37', foreground='#d8dbe4')
        self.label2.place(x=58, y=90)
        self.label3 = tk.Label(self, text='Developed by: erfannjz | Ver: 1.0', background='#2b2e37', foreground='#d8dbe4')
        self.label3.place(x=60, y=110)


    def btns(self):
        
        def on_enter1(ctx):
            if Panel.btn_state == False:
                self.btn1['background'], self.btn1['foreground'] = '#03fc41', '#2b2e37'
            
            else:
                self.btn1['background'], self.btn1['foreground'] = '#fc0328', '#2b2e37'

        def on_leave1(ctx):
            if Panel.btn_state == False:
                self.btn1['background'], self.btn1['foreground'] = '#2b2e37', '#03fc41'
            
            else:
                self.btn1['background'], self.btn1['foreground'] = '#2b2e37', '#fc0328'

        def on_enter2(ctx):
            self.btn2['background'], self.btn2['foreground'] = '#e8fc03', '#2b2e37'

        def on_leave2(ctx):
            self.btn2['background'], self.btn2['foreground'] = '#2b2e37', '#e8fc03'

        def about():
            wb.open('https://github.com/erfannjz')

        def time_checker():
            global proc
            if (strftime('%H:%M') == Vadana.class_time) and (Panel.time_state == True):
                proc = Vadana()
                proc.onliner()
                Panel.time_state = False
            window.after(1000, time_checker)

        def start_stop():
            global proc
            if Panel.btn_state == False:
                self.btn1.configure(text='S T O P', fg='#fc0328', bg='#2b2e37',
                activebackground='#fc0328', activeforeground='#2b2e37')
                Panel.btn_state, Panel.time_state = True, True
                time_checker()
               
            elif Panel.btn_state == True:
                self.btn1.configure(text='S T A R T', fg='#03fc41', bg='#2b2e37',
                activebackground='#03fc41', activeforeground='#2b2e37')
                Panel.btn_state = False
                try:
                    proc.offliner()
                except:
                    pass
                window.after_cancel(window)


        self.btn1 = tk.Button(self, text='S T A R T', bg='#2b2e37', fg='#03fc41',
        activebackground='#03fc41', activeforeground='#2b2e37', border=0, width=42, height=2, command=start_stop)
        self.btn2 = tk.Button(self, text='A B O U T', bg='#2b2e37', fg='#e8fc03',
        activebackground='#e8fc03', activeforeground='#2b2e37', border=0, width=42, height=2, command=about)


        self.btn1.bind('<Enter>', on_enter1)
        self.btn1.bind('<Leave>', on_leave1)
        self.btn2.bind('<Enter>', on_enter2)
        self.btn2.bind('<Leave>', on_leave2)
        self.btn1.place(x=0, y=190)
        self.btn2.place(x=0, y=230)



if __name__ == '__main__':
    window = Panel()
    window.label()
    window.btns()
    window.mainloop()
