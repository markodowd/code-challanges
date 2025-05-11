#!/bin/bash

countToTwenty() {
  i=1
  
  while [ $i -le 20 ]
  do
    echo "Count: $i"
    ((i++))
  done
}

countToTwenty

