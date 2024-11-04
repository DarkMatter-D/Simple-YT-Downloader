import customtkinter
from pytubefix import YouTube,Playlist
from pytubefix.exceptions import RegexMatchError


#appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
#main app
main_app = customtkinter.CTk()
main_app.geometry("400x300")
main_app.title("Youtube Downloader")
main_app.resizable(0,0)


#a bunch of labels
text_box = customtkinter.CTkLabel(main_app,text="Enter Video URL:",font=('Fira Code', 15,'bold'))
text_box.place(x=70,y=30)
error_label = customtkinter.CTkLabel(main_app, text="Invalid Url!",text_color="red",font=('Fira Code', 20, 'bold'),anchor="center")
downloading_label = customtkinter.CTkLabel(main_app,text="Downloaded!",text_color="white",font=('Fira Code', 20, 'bold'),anchor="center")


#the main download function
def main_download(url,mode):
    try:
        video = YouTube(url)
        error_label.destroy()
        downloading_label.place(relx=0.5, rely=0.5,x=-60,y=50)
    except RegexMatchError:
        error_label.place(relx=0.5, rely=0.5,x=-60,y=50)
    #mode checks "video" or "audio"
    if mode == "video":
        video.streams.first().download(output_path="output")
    elif mode == "audio":
        video.streams.filter(only_audio=True)
        video.streams.first().download(output_path="output",filename=video.title+".mp3")
#select all event for ctrl+a
def select_all(event=None):
    # select text
    url_input_box.select_range(0, 'end')
    # move cursor to the end
    url_input_box.icursor('end')


url_input_box = customtkinter.CTkEntry(master=main_app,width=250,height=35,placeholder_text="URL:",font=('Fira Code',15, 'bold'))
url_input_box.place(x=70,y=90)

#main audio and video buttons
audio_button = customtkinter.CTkButton(master=main_app,width=30,height=35,text="Download Audio",command=lambda : main_download(url_input_box.get(),"audio"),font=('Fira Code', 17))
audio_button.place(x=50,y=150)
video_button = customtkinter.CTkButton(master=main_app,width=30,height=35,text="Download Video",command=lambda : main_download(url_input_box.get(),"video"),font=('Fira Code', 17))
video_button.place(x=210,y=150)

#text placeholder for the history

main_app.bind('<Control-a>', select_all) #bind the ctrl+a key to be able to select all 

#mainloop
main_app.mainloop()


