#!/bin/bash

function delete(){
    cd 
    python delete.py $1
    rm -rf $1
}