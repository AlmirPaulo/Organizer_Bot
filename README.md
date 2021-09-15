# Organizer Bot
*A Project by [Almir Paulo](https://almirpaulo.github.io)*

A bot that works in the background moving all the files from the Downloads directory to the right directories based on the file type.

## Requirements
* Python3
* wget (for the installation)

## Installation Guide
Pass this lines on your terminal.
	
	sh -c "$(wget -O- https://raw.githubusercontent.com/AlmirPaulo/Organizer_Bot/main/install.sh)" 

This  command will download and run the installation script. This script ensures that the bot will recognize the correct paths to the folders in your system.

Now it's time to set the bot in the crontab. Start with this line.
				
	crontab -e

If it's your first time on crontab, it will prompt to you to choose some text editor. Pick your favorite, then pass the following line in the crontab.

	@reboot nohup python3 path/to/the/file/organizer_bot.py &

Don't forget to save before quit. This line will make the bot works in the backgrounds silently. Don't forget to reboot too.
<!--### For Windows Users
-->
## Possible Issues
### Does it works in Windows/Mac?

Yes! In theory... I never test it... Let me know if you do, please. 

### How I turn it off?
				
    ps ax| grep organizer_bot.py 
    (pick the process id then...)
    kill -9 (process id here)


### It's not working with some kinds of files.
The bot recognizes a specific list of file extensions. I made it in a way that only works with open formats. Just to be sure that it's all legal. I also focused in the most commonly used of this formats. If you are missing any file format, please let me know. 
So here is a list of file extensions the bot should recognize.

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
### But the file extension is on the list and it's not working...
Do you download and install by the method provided in this document?
### No, I...
Well, you should. The installation script takes care of some possible bugs. If you are worried about my script, you can check it here: 
	
	https://github.com/AlmirPaulo/Organizer_Bot/blob/main/install.sh

### Yes, and still not working!
OH MY GOD! WHAT DID YOU DID WITH MY BOT! 
Just kidding :grin:, please let me know whatever bug you find.
## Thanks
Thanks to [Kalle Hallden](https://github.com/KalleHallden) for the inspiration to make this bot. He made a similar one in this [video](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=246s&ab_channel=KalleHallden) and I thought it was a great idea, but maybe a could code it in other way, with less resources. 

## Contribute
If this bot make your life easier or make you happy in some way, consider once in a while buy me a coffee, just to encourage me to keep working on projects like this. 

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C26878E)


