# Organizer_Bot
A bot that works on the background moving all the files from the Downloads directory to the right directories based on the file type.

## Requirements
Of course you need Python installed. 

## Installation
Pass this lines on your terminal.
				
				cd /etc/init.d 
				wget https://raw.githubusercontent.com/AlmirPaulo/Organizer_Bot/main/organizer_bot.py
This first command leads you to the directory where we gonna install the bot. And the other one downloads the bot file. 
The next command will download and run the installation script. This script ensures that the bot will recognize the correct paths to the folders in your system.

			sh -c $(wget -O- https://raw.githubusercontent.com/AlmirPaulo/Organizer_Bot/main/install.sh)

Now is time to set the bot in the crontab. Start with this line.
				
				crontab -e
If its your first time on crontab, it will prompt to you to choose some text editor. Pick your favorite, then pass the following line in the crontab.

				@reboot nohup python3 path/to/the/file/organizer_bot.py &
Don't forget to save before quit. This line will make the bot works on the backgrounds silently. Don't forget to reboot too.
## Possible Issues
### Does it works on Windows?
Not yet. 
### How I turn it off?
				
				ps ax| grep organizer_bot.py 
				(pick the process id then...)
				kill -9 process_id_here(its a number)


### Its not working with some kinds of files.
The bot recognizes a specific list of file extensions. I made it in a way that only works with open formats. Just to be sure that its all legal. I also focused in the most used of this formats. If you miss any file format, please let me know. So here is a list of file extensions the bot should recognize.

**Text:**
* TXT
* MD
* PDF
* HTML
* ODT
* FODT
* ODG
* FODG
* ODP
* FODP
* ODS
* FODS
* EPUB


**Imaging:**
* PNG
* JPG
* JPEG
* SVG

**Video:**
* MKV

**Audio:**
* MP3
* OGG

## Thanks
Thanks to [Kalle Hallden](https://github.com/KalleHallden) for the inspiration to make this bot. He made a similar one in this [video](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=246s&ab_channel=KalleHallden) and I thought it was a great idea, but maybe a could code it in other way, I mean, with less resources. 

## License
This work was created by Almir Paulo and is under [Creative Commons License (CC-by)](https://creativecommons.org/licenses/by/4.0/).
