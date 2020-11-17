from pathlib import Path
from time import sleep

#path variables
download = Path('/home/<PERSONAL_FOLDER>/Downloads')
doc_path = Path('/home/<PERSONAL_FOLDER>/Documents')
img_path = Path('/home/<PERSONAL_FOLDER>/Pictures')
audio_path = Path('/home/<PERSONAL_FOLDER>/Music')
video_path = Path('/home/<PERSONAL_FOLDER>/Videos')

#file types variables
#Todos os filetypes
img = ['.jpg']

doc = ['.txt']

video = ['.mp4']

audio = ['.mp3']

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

