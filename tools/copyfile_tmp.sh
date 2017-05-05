#!/bin/bash

data_dir_news = '/home/navallo/Documents/DATA/formalCompetition4/News_info_train/'
data_dit_pics = '/home/navallo/Documents/DATA/formalCompetition4/News_pic_info_train/'
selected_news = '/home/navallo/Documents/DATA/10000sohudata/News_info_train/'
selected_pics = '/home/navallo/Documents/DATA/10000sohudata/News_pic_info_train/'

minsize=$((1024*10))
maxsize=$((1024*1000))

for file in `ls $data_dit_pics`
do
        filesize=`ls -l $file | awk '{ print $5 }'` 
        if [ $filesize -lt $maxsize ] 
        then
                if [ $filesize -gt $minsize ]
                then
                        echo $filesize
                fi
        fi
done