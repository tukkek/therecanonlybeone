#!/usr/bin/python3
import mutagen,glob,sys,os,random

if len(sys.argv)<2:
  print('Usage: ./therecanonlybeone.py collectionFolder')
  sys.exit(1)

collection={}

def scan():
  print('Scanning collection...')
  collection.clear()
  for f in glob.glob( f'{sys.argv[1]}/**', recursive=True):
    if(os.path.isdir(f)):
      #print(f)
      continue
    try:
      metadata=mutagen.File(f)
    except mutagen.mp3.HeaderNotFoundError as e:
      print('Error: '+f)
      print(e)
      continue
    if not metadata:
      continue
    artist=False
    for key in ['artist','TPE1']:
      if key in metadata:
        artist=metadata[key]
        if key=='TPE1':
          artist=artist.text
        if isinstance(artist,list):
          artist=artist[0]
        break
    if artist:
      collection[os.path.abspath(f)]=artist.lower()
    else:
      print('No artist: '+f)
  print(str(collection),file=open('collection.db','w'))

def generateplaylist():
  print('Generating playlist...')
  files=list(collection.keys())
  random.shuffle(files)
  artists=set()
  playlist=open('playlist.m3u','w')
  for f in files:
    artist=collection[f]
    if not artist in artists:
      #print(artist)
      artists.add(artist)
      print(f,file=playlist)

scanlater=True
if os.path.isfile('collection.db'):
  collection=eval(open('collection.db').read())
else:
  scan()
  scanlater=False
generateplaylist()
if scanlater :
  scan()
