# just a quick function to parse all hashtags off popular hashtag lists
import os


myfile = open('./hashtags/musicdel.txt', 'r');
music = open('./hashtags/music.txt', 'a')

for line in myfile:
    music.write(line.replace('#', ''))