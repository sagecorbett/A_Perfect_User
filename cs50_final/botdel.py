# just a quick function to remove all hashtags off popular hashtag lists
import os

myfile = open('./hashtags/del.txt', 'r');
music = open('./hashtags/popular.txt', 'a')

for line in myfile:
    music.write(line.replace('#', ''))