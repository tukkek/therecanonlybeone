#!/bin/bash
./therecanonlybeone.py ~/músicas>scan.log
#sleep 2
nohup clementine -l playlist.m3u&
#sleep 10m
nice kwrite scan.log
