import time
import datetime
import threading
import customtkinter as ctk
from ntp import NTPClient

VERSION = "v1.0.1"
FONT_TYPE = "meiryo"
env = {"ntp": "ntp.nict.jp"}

ntp = NTPClient(env["ntp"])

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.running = True
        self.geometry("700x400")
        self.minsize(350, 200)
        self.title(f"NTP Clock {VERSION}")
        self.font = ctk.CTkFont(FONT_TYPE, 8)
        self.SetupForm()
        self.bind("<Configure>", self.TextRisize)
        self.protocol("WM_DELETE_WINDOW", self.Quit)

    def Quit(self):
        global thread1
        self.running = False
        thread1.join()
        self.destroy()

    def TextRisize(self, event):
        if not ((event.type != "configure") and (event.widget != self)):
            self.font.configure(size=max(int(event.width / 15), 30))

    def SetupForm(self):
        self.label1 = ctk.CTkLabel(self, font=self.font, text="Loading...")
        self.label1.pack(expand=True, fill=ctk.BOTH)

    def UpdateTime(self):
        start = time.perf_counter()
        ntptime = ntp.get_nowtime()
        gettime = time.perf_counter() - start
        ntptime += datetime.timedelta(seconds=gettime)
        while self.running:
            self.label1.configure(text=ntptime.strftime("%Y/%m/%d %H:%M:%S"))
            ntptime += datetime.timedelta(seconds=1)
            time.sleep(1)

app = App()
thread1 = threading.Thread(target=app.UpdateTime)
thread1.start()
app.mainloop()
