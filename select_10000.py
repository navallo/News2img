import os
import shutil
import re

data_dir_news = '/home/navallo/Documents/DATA/formalCompetition4/News_info_train/'
data_dit_pics = '/home/navallo/Documents/DATA/formalCompetition4/News_pic_info_train/'
selected_news = '/home/navallo/Documents/DATA/1000sohudata/News_info_train/'
selected_pics = '/home/navallo/Documents/DATA/1000sohudata/News_pic_info_train/'

files = os.listdir(data_dit_pics)

RAND = 3
flag = 1 + RAND
#count = 0
for pic in files:
    if flag == (10 + RAND):
        flag = 1 + RAND
    else:
        flag = flag + 1
        continue
    if(10240<(os.path.getsize(data_dit_pics+pic))<1024000):
#        print(pic)
        id = re.split('\.',str(pic))[0]
#        print(id)
        news = id + '.txt'

        shutil.copy(data_dit_pics+pic, selected_pics+pic)
        shutil.copy(data_dir_news+news, selected_news+news)
#        count = count + 1
#print(count)