#!/bin/bash

#activate virtual environment
source ../env/bin/activate

use_file=false
while getopts "m:f:" opt
do
	case $opt in
	m)
		name=${OPTARG}
		;;
	f)
		filename=${OPTARG}
		use_file=true
		;;
	esac
done

if [ $use_file = false ]
then
	#Run Script
	python scraper.py <<<$name

	#Create filename to save links
	filename=$( echo $name | sed -e "s/\b\(.\)/\u\1/g"| tr " " _)
	
	#Create directory to save images
	mkdir -p  $SCRAPER_DIRECTORY/$filename

	#Move the links file to created directory
	mv $filename $SCRAPER_DIRECTORY/$filename/

	#Download the images in created directory
	wget --user-agent="" --continue --directory-prefix=$SCRAPER_DIRECTORY/$filename/ --input-file=$SCRAPER_DIRECTORY/$filename/$filename

else
	while read name
	do 
		echo Processing $name
		#Run Script
		python scraper.py <<<$name
		
		#Create filename to save links
		filename=$( echo $name | sed -e "s/\b\(.\)/\u\1/g"| tr " " _)
		
		#Create directory to save images
		mkdir -p  $SCRAPER_DIRECTORY/$filename

		#Move the links file to created directory
		mv $filename $SCRAPER_DIRECTORY/$filename/

		#Download the images in created directory
		wget --user-agent="" --continue --directory-prefix=$SCRAPER_DIRECTORY/$filename/ --input-file=$SCRAPER_DIRECTORY/$filename/$filename


	done < $filename
fi
