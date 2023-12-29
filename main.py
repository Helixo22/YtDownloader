import tkinter
import customtkinter
from pytube import YouTube

# Global variable for %
percentage_of_completion = 0
update_interval = 100

# Function
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
        video.download()
        title.configure(text=yt_object.title, text_color="white")
        finish_label.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        finish_label.configure(text="YouTube link is invalid", text_color="red")
        print(f"Error: {e}")

# Progress bar function
def on_progress(stream, chunk, bytes_remaining):
    global percentage_of_completion
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    p_percentage.configure(text=per + '%')
    update_progress()

# Update progress bar
def update_progress():
    progress_bar.set(percentage_of_completion)
    app.after(update_interval, update_progress)

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YtDownloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link:")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress % bar
p_percentage = customtkinter.CTkLabel(app, text="0%")
p_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download button
download_button = customtkinter.CTkButton(app, text="Download", command=start_download)
download_button.pack(padx=10, pady=10)

# Run App
app.mainloop()
