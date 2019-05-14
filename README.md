# gdata
A graph that shows my most searched in Google Search from 2015-2019

## First step : Download data from google account
After you wait, we use sqlite3 to create database based on my google search.
## Second step : Clean the data
I downloaded the file as html format so I had to do a bit of web scraping. I googled some stopwords data, so the most searched words won't be a word like 'in', etc. After that I put all the words into a database called mylife.db, which can be opened with DB Browser for SQLite.
## Create graph image with matplotlib and numpy
After the database was complete, I used the data from mylife.db to create a graph with matplotlib and numpy.
1471 images were created from 2015 to 2019 with images.py
## Generate the images
I used cv to generate the images and make it a video.

## Check out the word_images_1yrwin_1dslide folder, video.avi will show all the data time to time.
