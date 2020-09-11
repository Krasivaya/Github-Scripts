#!/bin/bash

function create() {
  cd 
  python create.py $1
  cd /home/coder/project
  cd /home/coder/project/$1
  git init
  touch readme.md
  echo '#' $1 >> readme.md
  git add .
  git commit -m 'My First Commit'
  git remote add origin https://github.com/Github_Username/$1.git
  git push origin master
  code .
}
