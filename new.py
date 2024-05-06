import tkinter
import customtkinter
from pytube import YouTube

# UI Design and Settings
customtkinter.set_appearance_mode("System") # Set the appearance based on the system
customtkinter.set_default_color_theme("green")

# Frame Settings
application = customtkinter.CTk() # Initialize the application
application.geometry("800x400")
application.title("YouTube Video Downloader")

# Add in UI elements
title = customtkinter.CTkLabel(application, text="Paste a YouTube video link")
title.pack(padx=15, pady=15)

def startDownload():
    try:
        linkToDownload = youtubeLink.get()
        youTubeVideoObject = YouTube(linkToDownload, on_progress_callback=inProgress)
        video = youTubeVideoObject.streams.get_highest_resolution()
        video.download()
        videoTitle = youTubeVideoObject.title
        statusMessageText = customtkinter.CTkLabel(application, text="The video:" + videoTitle + " is downloaded!", text_color="green")
        statusMessageText.pack(padx=25, pady=25)
    except:
        statusMessageText = customtkinter.CTkLabel(application, text="The link:" + linkToDownload + " is invalid!", text_color="red")
        statusMessageText.pack(padx=25, pady=25)

def inProgress(stream, chunk, bytes_remaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentageOfCompletion = bytesDownloaded / totalSize * 100
    percentageOfCompletion = str(int(percentageOfCompletion))
    # Update Percentage
    progressPercentage.configure(text=percentageOfCompletion + "%")
    progressPercentage.update()
    #Update Progress Bar
    progressBar.set(float(percentageOfCompletion) / 100)

# Textbox input
youtubeURL = tkinter.StringVar()
youtubeLink = customtkinter.CTkEntry(application, width=400, height=50, textvariable=youtubeURL)
youtubeLink.pack()

# Progress Percentage
progressPercentage = customtkinter.CTkLabel(application, text="0%")
progressPercentage.pack()

# Progress Bar
progressBar = customtkinter.CTkProgressBar(application, )
progressBar.set(0)
progressBar.pack(padx=15, pady=15)

# Download Button
downloadButton = customtkinter.CTkButton(application, text="Download", command=startDownload)
downloadButton.pack(padx=15, pady=15)

application.mainloop()
