import tkinter as tk
import customtkinter
from pytube import YouTube
from tkinter import filedialog

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YOUTUBE DOWNLOADER")


def start_download(option):
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
            file_path_audio = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                           filetypes=[("Audio files", "*.mp3")])
            video.download(file_path_audio)
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        finishLabel.configure(text="Downloaded !!", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perecentage_of_completion = bytes_download / total_size * 100
    per = str(int(perecentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    progressbar.set(float(perecentage_of_completion) / 100)

title = customtkinter.CTkLabel(app, text="INSERT YOUTUBE LINK", font=("times new roman", 22), )
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=30, placeholder_text="paste video link here....",
                              textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady = 10)

download = customtkinter.CTkButton(app, text="DOWNLOAD HIGH QUALITY-mp4", corner_radius=20, hover_color="green",
                                   border_width=2,
                                   border_color="black", command=lambda: start_download("hq"))
download.pack(padx=10, pady=10)

download2 = customtkinter.CTkButton(app, text="DOWNLOAD low QUALITY-mp4", corner_radius=20, hover_color="green",
                                    border_width=2,
                                    border_color="black", command=lambda: start_download("lq"))
download2.pack(padx=10, pady=10)

download3 = customtkinter.CTkButton(app, text="DOWNLOAD mp3", corner_radius=20, hover_color="green", border_width=2,
                                    border_color="black", command=lambda: start_download("audio"))
download3.pack(padx=10, pady=10)

app.mainloop()
