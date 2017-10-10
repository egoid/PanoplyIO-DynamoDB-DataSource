#!/bin/bash

if [[ $# -eq 3 ]] ; then
  mkdir tables
  AWS_KEY=$1
  AWS_SECRET=$2
  TABLE_NAME=$3
  go run export.go -k "$AWS_KEY" -s "$AWS_SECRET"-t "$TABLE_NAME" > "./tables/$TABLE_NAME".json
  echo "completed"

else 
  exit -1
fi