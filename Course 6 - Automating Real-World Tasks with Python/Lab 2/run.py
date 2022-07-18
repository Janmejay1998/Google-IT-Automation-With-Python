#!/usr/bin/env python3
import os
import requests

# Set source dir for feedback file:
source_dir = "feedback/"

# Capture list of files:
files = os.listdir(source_dir)

# Function to read file lines into list:
def readlines(file):
    with open(source_dir + file) as f:
        lines = f.read().splitlines()
    return lines


# Load feedback entries into dictionary:
feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
    lines = readlines(file)
    feedback.append(dict(zip(keys, lines)))

# Set host url:
url = "http://localhost/feedback/"

# Post feedback entries:
for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")
