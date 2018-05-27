#!/bin/bash

DATE=$(date +"%Y-%m-%d-%H-%M-%S")

raspistill -vf -hf -o ~/Project/capture_pic/$DATE.jpg
