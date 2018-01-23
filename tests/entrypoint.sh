#!/bin/bash
cd $(dirname $0)

cd tests/
ls | sort | while read file
do
  echo "$file"
  if ! python3 "$file"
  then
    exit 1
  fi
done
