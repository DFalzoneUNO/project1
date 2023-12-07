import tkinter as tk
from typing import List

from accounts import Account


class Gui:
    def __init__(self, accounts: List[Account]):
        self._window = tk.Tk()
        self._window.title("Deposit Account Manager (Unprofessional Edition)")
        self._window.geometry("650x400")
        self._window.resizable(False, False)
        self._accounts = accounts

    def mainloop(self):
        self._window.mainloop()
