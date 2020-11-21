from pathlib import Path
from time import sleep

#path variables
download = Path('/home/PERSONAL_FOLDER/Downloads')
doc_path = Path('/home/PERSONAL_FOLDER/Documents')
img_path = Path('/home/PERSONAL_FOLDER/Pictures')
audio_path = Path('/home/PERSONAL_FOLDER/Music')
video_path = Path('/home/PERSONAL_FOLDER/Videos')

#file types variables
doc = ['.txt', '.md', '.pdf', 
        '.html', '.odt', '.fodt', 
	'.odg', '.fodg','.ods', 
	'.fods', '.odp','.fodp',
	'.epub', '.TXT', '.MD', 
	'.PDF', '.HTML', '.ODT'
       '.FODT','.OGD','.FOGD', 
       '.ODS','.FODS', '.ODP',
       '.FODP','.EPUB']

img = ['.jpg', '.jpeg', '.png', '.svg' 
       '.JPG', '.JPEG', '.PNG', '.SVG']

video = ['.mkv', '.MKV']

audio = ['.mp3', '.ogg', '.OGG', '.MP3']

#loop
while True:
    for file in download.glob('*'):
        if file.suffix in doc:
            string = str(doc_path)+'/'+str(file.name)
            dest = Path(string)
            file.rename(dest)
        elif file.suffix in img:
            string = str(img_path)+'/'+str(file.name)
            dest = Path(string)
            file.rename(dest)
        elif file.suffix in audio:
            string = str(audio_path)+'/'+str(file.name)
            dest = Path(string)
            file.rename(dest)
        elif file.suffix in video:
            string = str(video_path)+'/'+str(file.name)
            dest = Path(string)
            file.rename(dest)
    sleep(1)
 
