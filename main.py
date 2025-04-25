import yt_dlp
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import sys

class MainWindow(QWidget) : 
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("YT downloader")
            self.setGeometry(100,100,400,200)

            self.layout= QVBoxLayout()
            self.input_link =  QLineEdit(self)
            self.input_link.setPlaceholderText ("Youtube Linki giriniz :")
            self.layout.addWidget (self.input_link) 

            self.input_filename= QLineEdit(self)
            self.input_filename.setPlaceholderText("Dosya ismini girin")
            self.layout.addWidget(self.input_filename)

            self.input_format = QLineEdit(self)
            self.input_format.setPlaceholderText("Dosya formatini girin : (mp3/mp4)")
            self.layout.addWidget(self.input_format)
        

            self.label = QLabel ("Sonuc buraya cikacak :", self)
            self.layout.addWidget(self.label)

            self.button =   QPushButton("Gonder",self)
            self.button.clicked.connect(self.on_button_click)
            self.layout.addWidget(self.button)

            self.setLayout(self.layout)

            
        def on_button_click(self) :
                link  = self.input_link.text()
                filename= self.input_filename.text()
                format = self.input_format.text() 

                if link and filename and format :
                    self.label.setText("Indiriliyor...")
                    self.DownloadAudio(link,filename,format)
                else: 
                     self.label.setText("Something went wrong.") 

        def DownloadAudio(elf, link, filename,format_choice):

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

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
