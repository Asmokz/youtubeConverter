from pytube import YouTube
import pytube
import os
import moviepy
from moviepy.editor import *

def main():
    video_url = input("Entrez votre URL Youtube : ")


    path = os.getcwd()
    youtube_video=YouTube(video_url)
    name=youtube_video.title
    name = ''.join(filter(str.isalnum, name))+ '.mp3'
    stream = youtube_video.streams.get_by_itag(140)
    path = 'D:/Musique'
    print('Téléchargement...')
    stream.download(filename = name, output_path=path)
    print('OK')
    
    



if __name__ == '__main__':
    main()
