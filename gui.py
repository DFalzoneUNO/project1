import tkinter as tk
from typing import List

from accounts import Account


class VarLabel:
    def __init__(self, frame: tk.Frame, content: str = ""):
        self._content = tk.StringVar(frame, content)
        self._label = tk.Label(frame, textvariable=self._content)

    @property
    def content(self) -> str:
        return self._content.get()

    def set(self, new_value: str):
        self._content.set(new_value)


class ErrorMessageView:
    def __init__(self, window: tk.Tk):
        self._frame = tk.Frame(window)
        self._frame.anchor("center")
        self._message = tk.StringVar(self._frame, value="default error message")
        self._label = tk.Label(self._frame, textvariable=self._message)
        self._button = tk.Button(self._frame, text="Ok", command=self.hide)
        self._label.anchor("n")
        self._button.anchor("s")
        self._label.pack()
        self._button.pack()

    def show_error_message(self, error_message: str):
        self._message.set(f"Error: {error_message}")
        self._frame.pack()

    def hide(self):
        self._frame.pack_forget()


class AccountView:
    def __init__(self, window: tk.Tk):
        self._frame = tk.Frame(window)
        self._frame.anchor("center")
        self._account_holder_name = tk.StringVar(self._frame, "default account holder name")
        self._account_holder_label = tk.Label(self._frame, textvariable=self._account_holder_name)


class Gui:
    def __init__(self, accounts: List[Account]):
        self._window = tk.Tk()
        self._window.title("Deposit Account Manager (Unprofessional Edition)")
        self._window.geometry("650x400")
        self._window.resizable(False, False)
        self._accounts = accounts
        self._error_message_view = ErrorMessageView(self._window)

    def mainloop(self):
        self.view_error("foo")
        self._window.mainloop()

    def view_error(self, error_message: str):
        self._error_message_view.show_error_message(error_message)


    #def view_account(self, name: str):

