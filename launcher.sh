#!/bin/bash
./therecanonlybeone.py ~/músicas>scan.log &
sleep 2
clementine -l playlist.m3u&
sleep 10m
kwrite scan.log
