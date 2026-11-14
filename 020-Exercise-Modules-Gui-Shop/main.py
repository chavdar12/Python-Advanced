import tkinter as tk
from tkinter import messagebox

import storage

root = tk.Tk()
root.title("GUI Shop")
root.geometry("500x400")
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)


def clear():
    for widget in frame.winfo_children():
        widget.destroy()


def form(fields, submit_text, on_submit, back=None):
    clear()
    entries = {}
    for row, (label, show) in enumerate(fields):
        tk.Label(frame, text=label).grid(row=row, column=0, sticky="w")
        entries[label] = tk.Entry(frame, show=show)
        entries[label].grid(row=row, column=1)
    tk.Button(frame, text=submit_text, command=lambda: on_submit({k: e.get() for k, e in entries.items()})).grid(
        row=len(fields), column=1, pady=10)
    if back:
        tk.Button(frame, text="Back", command=back).grid(row=len(fields), column=0)


def show_start():
    clear()
    tk.Button(frame, text="Login", width=20, command=show_login).pack(pady=5)
    tk.Button(frame, text="Register", width=20, command=show_register).pack(pady=5)


def show_login():
    def submit(values):
        if storage.login(values["Username"], values["Password"]):
            show_products(values["Username"])
        else:
            messagebox.showerror("Error", "Invalid username/password")

    form([("Username", ""), ("Password", "*")], "Login", submit, back=show_start)


def show_register():
    def submit(values):
        try:
            storage.register(values["Username"], values["Password"], values["First name"], values["Last name"])
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return
        show_login()

    form([("First name", ""), ("Last name", ""), ("Username", ""), ("Password", "*")], "Register", submit,
         back=show_start)


def show_products(username):
    clear()
    for col, product in enumerate(storage.list_products()):
        tk.Label(frame, text=product["name"]).grid(row=0, column=col, padx=10)
        tk.Label(frame, text=f"Left: {product['count']}").grid(row=1, column=col)
        state = tk.NORMAL if product["count"] > 0 else tk.DISABLED
        tk.Button(frame, text="Buy", state=state, command=lambda pid=product["id"]: buy(username, pid)).grid(
            row=2, column=col)


def buy(username, product_id):
    try:
        storage.buy(username, product_id)
    except ValueError as error:
        messagebox.showerror("Error", str(error))
    show_products(username)


if __name__ == "__main__":
    show_start()
    root.mainloop()
