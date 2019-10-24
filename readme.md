This is our flask backend repository for our COMP90018 Project - Daily Picko

```
├── recommendBySelection.py         recommend by user's selected options
├── resolveLatlngToEntity.py        resolve longitude and latitude to address
├── sentimentRecommendation.py      guess what I like recommendation by sentiment analysis of check-in history and time
├── server.py                       backend flask server
├── readme.md
├── api                             Zomato API description
├── categories.py                   restaurant categories of Zomato
└── requirements.txt                python dependencies

```

Pre-Requisite:
 - python 3.7+


## Install dependencies
1. run **sudo pip3 install -r requirements.txt** (to install all dependencies)
2. replace line 14 in file resolveLatlngToEntity.py to the following to add google API key:
   'key': "AIzaSyDG_D-EdEwLb2ipCNinhxdD9EiqFdFA0B8",


## Steps to run
1. run python3 server.py


Notice: This repository offers the backend server to the project:
https://github.com/carolCheng123/COMP90018Project
