import tkinter
from tkinter.ttk import Progressbar
import customtkinter
from pytube import YouTube


#global variable for %
percentage_of_completion = 0
update_interval = 100

#function
def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
        video.download()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        finishLabel.configure(text="YouTube link is invalid", text_color="red")
        print(f"Error: {e}")

#Progress bar function
def on_progress(stream, chunk, bytes_remaining):
    global percentage_of_completion
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')

#Update progress bar 
def update_progress():
    progressBar["value"] = percentage_of_completion
    app.after(update_interval, update_progress)




#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YtDownloader")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link:")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#progress % bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)



#download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run App 
app.mainloop()
