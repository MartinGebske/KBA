import tkinter as tk
import ProgBackend as bend
import Frontend as fend

## Programmstart

# Hier wird das tkinter Root definiert
root = tk.Tk()
root.title("K.B.A. Neuzulassungen: Alternative Antriebe")

# Die Verknüpfung zwischen Frontend und Backend (wird instanziert)
be = bend.myBackend()
fe = fend.Plotall(root, (18, 6), be)

root.mainloop()
