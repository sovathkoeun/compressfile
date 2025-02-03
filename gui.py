import tkinter as tk
from compressmudule import compress, decompress


def compression(i,o):
    compress(i,o)


window = tk.Tk()
window.title("My First GUI Program")
window.geometry("800x500")

input_entery = tk.Entry(window)
output_entery = tk.Entry(window)

input_label = tk.Label(window, text="Input File")
output_label = tk.Label(window, text="Output File")


compress_button = tk.Button(window, text="Compress",command=lambda:compression(input_entery.get(),output_entery.get()))

input_label.grid(row=0, column=0)
input_entery.grid(row=0, column=1)
output_label.grid(row=1, column=0)
output_entery.grid(row=1, column=1)

compress_button.grid(row=2, column=1)


window.mainloop()