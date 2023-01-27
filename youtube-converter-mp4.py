from pytube import YouTube

def main(link = input("Put your youtube link here!! URL: ")):
    link = input("Put your youtube link here!! URL: ")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path="D:\Vidéos")
    except:
        print("There has been an error in downloading your youtube video")
    print("This download has completed! Yahooooo!")


if __name__ == '__main__':
    main()