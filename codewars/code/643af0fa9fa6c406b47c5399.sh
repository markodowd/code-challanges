#!/bin/bash

if [ $1 -ge 1 ]; then
  if [ $2 -ge 1 ]; then
    echo 1
  else
    echo 4
  fi
fi

if [ $1 -le -1 ]; then
  if [ $2 -ge 1 ]; then
    echo 2
  else
    echo 3
  fi
fi

