# Organizer_Bot
A bot that works on the background moving all the files from the Downloads directory to the right directories based on the file type.

## Installation
Pass this lines on your terminal.
				# Instalation Steps
				wget ...
				crontab -e 
The first command downloads the bot file. The second opens your crontab. If its your first time in crontab, it will prompt to you to choose some text editor. Pick your favorite. Then pass the following line in the crontab.
				# Crontab line
				@reboot nohup python3 path/to/the/file/organizer_bot.py &
Don't forget to save before quit. This line will make the bot works on the backgrounds silently. Don't forget to reboot too.
## Possible Issues
### Does it works on Windows?
Not yet. 
### How I turn it off?
				#
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


<--### But the file extension is on the list and its not working...
Do you download and install by the method provided in this document?
### No, I...
Well, you should. The installation script take care of some possible bugs. If you are worried about my script, you can check it here: (Soon...)

### Yes, and still not working!
Oh my god! What did you did with my bot! 
Just kidding, please let me know whatever bug you find.__> 

## Thanks
Thanks to [Kalle Hallden](https://github.com/KalleHallden) for the inspiration to make this bot. He made a similar one in this [video](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=246s&ab_channel=KalleHallden) and I thought it was a great idea, but maybe a could code it in other way, I mean, with less resources. 

## License
This work was created by Almir Paulo and is under [Creative Commons License (CC-by)](https://creativecommons.org/licenses/by/4.0/).
