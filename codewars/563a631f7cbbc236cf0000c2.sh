#!/bin/bash

position=$1
roll=$2

new_position() {
  roll_double=$(($2 * 2))
  echo $(($1 + roll_double))
}

new_position $1 $2

