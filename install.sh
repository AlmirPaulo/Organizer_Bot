#! /bin/env bash

# Software: install.sh for Organizer_Bot
# Description: Install Organizer_Bot properly.
# Author: Almir Paulo <https://almirpaulo.github.io>
# Version: 0.2.0
# Webpage: https://github.com/AlmirPaulo/Organizer_Bot
# License: MIT



#Welcome message
echo '==========================================================================================================='
echo '  '
echo 'Welcome to the Organizer Bot installation!'
echo 'We need some information to set the bot properly.'


#Input variables

read -p "What is the name of the folder where you receive all your downloads? (Must be inside your home directory) " DOWNLOADS 

read -p "What is the name of the folder that will receive text files? (Must be inside your home directory) " DOCS

read -p "What is the name of the folder that will receive image files? (Must be inside your home directory) " PICS

read -p "What is the name of the folder that will receive video files? (Must be inside your home directory) " VIDEOS

read -p "What is the name of the folder that will receive audio files? (Must be inside your home directory) " AUDIOS


#Asking for permission and setting bot
echo "If you have answered wrong to any of these questions we can start this again."
while true 
do
	read -p "Do you want to restart? " ANSWER
	case "$ANSWER" in
		[nN] | [nN][oO] )
            #criar um diretorio oculto para o bot
            mkdir ~/.Organizer_Bot
            FOLDER= "${USER}/.Organizer_Bot/"

            wget https://raw.githubusercontent.com/AlmirPaulo/Organizer_Bot/main/organizer_bot.py

            mv organizer_bot.py ${FOLDER}

			sed -i  "s/PERSONAL_FOLDER/${USER}/" ${FOLDER}
            sed -i "s/Downloads/$DOWNLOADS/" ${FOLDER}
			sed -i  "s/Documents/$DOCS/" ${FOLDER}
			sed -i  "s/Pictures/$PICS/" ${FOLDER}
			sed -i  "s/Videos/$VIDEOS/" ${FOLDER}
			sed -i  "s/Music/$AUDIOS/" ${FOLDER}

			echo "It's Alive!" 
			echo "Don't forget to set it in your crontab."
			echo 'read about it in the README.md'
			echo ̈́'https://github.com/AlmirPaulo/Organizer_Bot/blob/main/README.md'
			echo 'Contact-me on Github if you need any help'
			echo 'Cheers'
			break;;
		[yY] | [yY][eE][sS])

            read -p "What is the name of the folder where you receive all your downloads? (Must be inside your home directory) " DOWNLOADS 

			read -p "What is the name of the folder that will receive text files? (Must be inside your home directory) " DOCS

			read -p "What is the name of the folder that will receive image files? (Must be inside your home directory) " PICS

			read -p "What is the name of the folder that will receive video files? (Must be inside your home directory) " VIDEOS

			read -p "What is the name of the folder that will receive audio files? (Must be inside your home directory) " AUDIOS
			;;
	esac
done
