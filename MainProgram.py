import tkinter as tk
import ProgBackend as bend
import Frontend as fend



root = tk.Tk()
root.title("My PLot")

be = bend.myBackend()
fe = fend.Plotall(root, (18,6),be)

root.mainloop()
