import tkinter as tk
from tkinter import messagebox
import time
from datatime import date

class PomodoroUyg:
    def __init__(self,master):
        self.master=master
        self.master.title("Pomodoro Uygulaması")

        self.calismaZamani=26*60
        self.molaZamani=5*60
        self.calisiyor= False
        self.kalanZaman= self.calismaZamani
        self.oturum={}
        