#!/bin/bash

#activate virtual environment
source ../env/bin/activate

#Get Model Name 
name=$1

#Run Script
python scraper.py <<<$name

filename=$( echo $name | sed -e "s/\b\(.\)/\u\1/g"| tr " " _)
mkdir -p  $SCRAPER_DIRECTORY/$filename
mv $filename $SCRAPER_DIRECTORY/$filename/

wget --user-agent="" --continue --directory-prefix=$SCRAPER_DIRECTORY/$filename/ --input-file=$SCRAPER_DIRECTORY/$filename/$filename
