#!/bin/bash

laLigaGoals=$1
copaDelReyGoals=$2
championsLeagueGoals=$3

goals() {
  sum=$(($1 + $2 + $3))
  echo $sum
}

goals $1 $2 $3

