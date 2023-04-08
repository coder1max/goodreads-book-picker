import random
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

df = pd.read_csv(file_path)
liste = list(df[df['Bookshelves'] == 'to-read']['Title'])
print("Ta prochaine lecture sera : " + random.choice(liste))
