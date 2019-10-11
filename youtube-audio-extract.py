#!/usr/bin/python3

# to run this script, install the following modules:
# pip3 install youtube_dl
# pip3 install mutagen

# https://stackoverflow.com/questions/38110384/convert-any-audio-file-to-mp3-with-python#
# https://github.com/jiaaro/pydub/blob/master/API.markdown
# https://github.com/rg3/youtube-dl
# https://www.programcreek.com/python/example/63462/mutagen.mp3.EasyMP3
# https://docs.python.org/2/library/argparse.html

from __future__ import unicode_literals
import youtube_dl
import os
import sys
import glob
import  mutagen
from mutagen.easyid3 import EasyID3
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                 description="Extract audio from a youtube video.",
                                 epilog="Example:\nyoutube-audio-extract.py https://www.youtube.com/watch?v=ZTdOMV-yTRg Marillion Lavender")
parser.add_argument('url', action='store', default='https://www.youtube.com/watch?v=ZTdOMV-yTRg', help='URL of the video (default: https://www.youtube.com/watch?v=ZTdOMV-yTRg).')
parser.add_argument('artist', action='store', default='Marillion', help='Artist of the song (default: Marillion)')
parser.add_argument('title', action='store', default='Lavender', help='Title of the song (default: Lavender)')
parser.add_argument('--workpath', action='store', default='/home/'+os.getlogin()+'/Musik/', help='Storage location (default: Musik-sub-dir in home-dir; must exist !)')
args = parser.parse_args()
if os.path.isdir(args.workpath):
  print('workpath exists.')
else:
  print('No place found to store the file. Consider using the optional --workpath <path> argument.')
  quit()

mp3final = args.artist+'_'+args.title+'.mp3'
mp3path =  args.workpath+'/'+mp3final

#arguments = sys.argv[1:]
#argcount = len(arguments)
#program_name = sys.argv[0]
#ydl_url = sys.argv[1]
#ARTIST = sys.argv[2]
#TITLE = sys.argv[3]

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(args.url, download=False)
    mp3wild = '*'+meta['id']+'.mp3'
    print('Downloading to: ', args.workpath)
    result = ydl.download([args.url])
    print('Renaming file to: ', mp3path)
    mp3glob = glob.glob(mp3wild)
    os.rename(mp3glob[0], mp3path)
    
print('Tagging the file with: Artist="'+args.artist+'", Title="'+args.title+'"')
try:
    tag = EasyID3(mp3path)
except:
    tag = mutagen.File(mp3path, easy=True)
    tag.add_tags()

tag['artist'] = args.artist
tag['title'] = args.title
tag.save()

