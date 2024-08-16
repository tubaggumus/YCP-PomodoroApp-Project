import tkinter as tk
from tkinter import messagebox
import time
from datetime import date

class PomodoroUyg:
    def __init__(self,master):
        self.master=master
        self.master.title("Pomodoro Uygulaması")

        self.calismaZamani=25*60
        self.molaZamani=5*60
        self.calisiyor= False
        self.kalanZaman= self.calismaZamani
        self.oturum={}

        #grafik arayüz kısmı
        self.label=tk.Label(master, text="25.00", font=("Times New Roman",48 ), foreground="purple", background="pink")
        self.label.pack(pady=20)
        
        self.baslatButonu= tk.Button(master, text="Pomodoroyu Başlat", foreground="purple", command=self.zamanıBaslat)
        self.baslatButonu.pack(pady=10)

        self.durdurButonu=tk.Button(master, text="Durdur", foreground="purple", command=self.zamanıDurdur)
        self.durdurButonu.pack(pady=10)

        self.raporButonu= tk.Button(master, text="Geçmiş Raporu", command=self.raporuGoster)
        self.raporButonu.pack(pady=10)
    
    def zamanıBaslat(self):
        self.calisiyor=True
        self.baslatButonu.config(state=tk.DISABLED)
        self.durdurButonu.config(state=tk.NORMAL)
        self.sayac()
    
    def zamanıDurdur(self):
        self.calisiyor=False
        self.baslatButonu.config(state=tk.NORMAL)
        self.durdurButonu.config(state=tk.DISABLED)
    
    #sayacı calıstırma
    def sayac(self):
        if self.calisiyor:
            if self.kalanZaman > 0:
                dakika, saniye= divmod(self.kalanZaman, 60)
                zaman=f"{dakika:02d}:{saniye:02d}"
                self.label.config(text=zaman)
                self.kalanZaman-=1
                self.master.after(1000, self.sayac)
            else:
                self.oturumuKaydet()
                messagebox.showinfo("Pomodoro başarıyla tamamlandı, çalışma süresi bitti.")
                self.zamanıDurdur()
                self.kalanZaman= self.calismaZamani
                self.label.config(text="25:00")
    
    def oturumuKaydet(self):
        today= date.today().strftime("%A")
        try:
            self.oturum[today]=self.oturum.get(today, 0)+ 25/60
        except Exception as e:
            print(f" Hata oluştu: {e}")

    def raporuGoster(self):
        rapor= "Haftalık Çalışma Raporu: \n"
        for day, hours in self.oturum.items():
            rapor+= f"{day} : {hours} saat\n"
        messagebox.showinfo("Haftalık Raporunuz", rapor)

def main():
        root=tk.Tk()
        app=PomodoroUyg(root)
        root.mainloop()

if __name__ == "__main__":
    main()