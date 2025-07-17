#!/bin/bash

a=$1
b=$2
c=$3

largest_number() {
  exp1=$(($1 * ($2 + $3)))
  exp2=$(($1 * $2 * $3))
  exp3=$(($1 + $2 * $3))
  exp4=$((($1 + $2) * $3))
  exp5=$(($1 + $2 + $3))
  
  largest=$exp1
  
  if [ $exp2 -gt $largest ] 
  then
    largest=$exp2
  fi
  
  if [ $exp3 -gt $largest ] 
  then
    largest=$exp3
  fi
  
  if [ $exp4 -gt $largest ] 
  then
    largest=$exp4
  fi
  
  if [ $exp5 -gt $largest ] 
  then
    largest=$exp5
  fi
  
  echo $largest
}

largest_number $1 $2 $3

