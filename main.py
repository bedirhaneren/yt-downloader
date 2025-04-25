import yt_dlp
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QFormLayout
import sys

class MainWindow(QWidget) : 
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("YT downloader")
            self.setGeometry(600,300,500,300)   

            self.layout= QFormLayout()
            self.layout.setSpacing(15)
            
            self.input_link =  QLineEdit(self)
            self.input_link.setPlaceholderText ("Enter the video link ")
            self.layout.addWidget (self.input_link) 

            self.input_filename= QLineEdit(self)
            self.input_filename.setPlaceholderText("Enter the file name")
            self.layout.addWidget(self.input_filename)

            self.input_format = QLineEdit(self)
            self.input_format.setPlaceholderText("Enter the file format (mp3/mp4)")
            self.layout.addWidget(self.input_format)
        

            self.label = QLabel ("Sonuc buraya cikacak :", self)
            self.layout.addWidget(self.label)

            self.button =   QPushButton("Download",self)
            self.button.clicked.connect(self.on_button_click)
            self.layout.addWidget(self.button)

            self.setLayout(self.layout)

            self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f7;
                font-family: 'Segoe UI';
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QLabel {
                color: #2c3e50;
                font-weight: bold;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 8px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #2980b9;
                transform: scale(1.05);
            }
            QPushButton:pressed {
                background-color: #2ecc71;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
            
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
