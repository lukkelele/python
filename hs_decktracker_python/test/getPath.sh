#!/bin/bash

currentDir=$(pwd)
if [ $currentDir == "~/Code/python/hs_decktracker" ] ; then
  cd 'test'
fi
echo $HOME
