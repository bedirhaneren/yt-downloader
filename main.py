import yt_dlp
import os


def DownloadAudio(link, filename,format_choice):

    if format_choice == 'mp3': 

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',   # 'm4a', 'wav' gibi başka formatlar da olabilir
                'preferredquality': '192',
            }],
            'outtmpl': filename + '.%(ext)s',
        }
    elif format_choice=='mp4': 
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': filename + '.%(ext)s',
            'merge_output_format': 'mp4',
        }
    else: 
        print("Unable format selected.")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([link])
            print("Ses başarıyla indirildi.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    filename= input("Please enter the filename : ")
    format = input ("Please enter the file format :")


    DownloadAudio(link,filename,format)


