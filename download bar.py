import tkinter as tk
from pytube import YouTube
import customtkinter
from tkinter import filedialog

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perecentage_of_completion = bytes_download / total_size * 100
    per = str(int(perecentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    # Update ProgressBar
    progressbar.set(float(perecentage_of_completion) / 100)
    # Progress Percentage
    progress = customtkinter.CTkLabel(app, text="0%")
    progress.pack()

    progressbar = customtkinter.CTkProgressBar(app, width=400)
    progressbar.set(0)
    progressbar.pack(padx=10, pady = 10)