<<<<<<< HEAD
import tkinter as tk
from pytube import YouTube
import customtkinter
from tkinter import filedialog

def startDownload(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "hq":
            video = ytObject.streams.get_highest_resolution()
            file_path_hq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_hq)
        elif option == "lq":
            video = ytObject.streams.get_lowest_resolution()
            file_path_lq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_lq)
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
            file_path_audio = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])
            video.download(file_path_audio)
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        finishLabel.configure(text="Downloaded !!", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")

=======
import tkinter
from pytube import YouTube
from tkinter import *

app = Tk()
app.title("YOUTUBE VIDEO DOWNLOADER")
app.config(background="green")
app.geometry("600x400")

app.mainloop()
>>>>>>> 81f6ac77b30f05d2a547dfae03dff86cc8497363
