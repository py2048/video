#!/usr/bin/env python
import os

m3u8 = '/home/codespace/workspace/video/e37d02b7-73b1-40ec-9068-b94e8791a7d9.m3u8'
prefix = ''
file_name = 'file.mp4'

os.chdir('/home/codespace/workspace/video/temp')

with open(m3u8, 'r') as file_handle:
    lines = file_handle.read().splitlines()

i = 0
while True:
    if lines[i][0] != '#':
        break
    i += 1

l_file = ''
k = 0
for j in range(i, len(lines), 2):
    temp = prefix + lines[j]
    media = f'media_{k}.part'
    k += 1
    print('Downloading', media)
    os.system(f'curl -o {media} {temp}')
    l_file += media + ' '

os.system(f'cat {l_file} > all.part')
os.system(f'ffmpeg -i all.part -acodec copy -vcodec copy {file_name}')
os.system('rm *.part')
