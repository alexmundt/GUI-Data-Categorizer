import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()


pb = ttk.Progressbar(root, mode="determinate")
pb.grid()


def testprogress():
    global pb
    for i in range(100):
        # root.after(10)
        pb["value"] += 0.1
        time.sleep(0.01)
        print(pb["value"])

progButton = tk.Button(root, text="progress test", command=testprogress)
progButton.grid()

root.grid()

root.mainloop()
