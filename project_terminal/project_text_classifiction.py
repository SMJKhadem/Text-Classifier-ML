#!/usr/bin/env python
# coding: utf-8

#  # $\color{green}{\text{ Text Classification; Web Scraping  }}$
# 

# # Goal:  is to predict the artist from a piece of text. 

# ## Scrap the desired website

# Web scraping = getting data from websites

# In[418]:
import requests
import numpy as np
import random
import os
import pandas as pd
os.chdir("/Users/kasiafalecka/Desktop/spiced_projects/nigela-network-student-code/week_04/project/project_terminal/")
path=os.getcwd()
# Requests allows us to send HTTP requests to website/servers. It sends back a response code, and the full html (if successful).
# In[368]:
URL_1 = 'https://www.lyrics.com/artist/Nicki-Minaj/1049866'
URL_2 = 'https://www.lyrics.com/artist/Pink-Floyd/76669'
# Most web server try to detect and block web scraping attempts.
# To stay undetected you can try the following:
# - Set a real user agent and other header to appear legit (headers can be found [Here](https://github.com/tamimibrahim17/List-of-user-agents): 

# In[369]:
headers = {'User-agent': 'Mozilla/5.0 (X11; Linux i686; rv:2.0b10) Gecko/20100101 Firefox/4.0b10'}
# ​ Use a sleep or waiting time between requests, a computer can be much faster than a human:

# In[366]:
import time
import numpy as np
# In[370]:
#time.sleep(5)
response_1 = requests.get(url=URL_1, headers=headers)
# In[371]:
response_2 = requests.get(url=URL_2, headers=headers)
# In[32]:
response_1
# In[372]:


response_1.status_code


# 
# 
# * 200-range: successful
# * 300-range: redirect
# * 400-range: there was a problem with the client's request
# * 500-range: there was a problem on the end of the server

# Webpage itself is saved in the `.text` attribute.

# In[387]:


Nicky_html = response_1.text
Pink_html = response_2.text


# What do you notice:
# * It's written in HTML (you don't need to know HTML though to scrape data!)
# * HTML is structured using _tags_ (it also has _classes_ and _ids_)
# * It is nested, has hierarchical structure

# In[374]:


print(Nicky_html)


# In[ ]:





# - What is this output?
# 
# It's written in HTML (you don't need to know HTML though to scrape data!)
# 
# [HTML Introduction](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)

# - Each element consists of tags (opening tag and closing tag) and content.
# 
# - Some tags will have attributes which are like labels that are not displayed with the content but can help distinguish between different types of the same tag. 
# - Important for this week: a-tags. 
# <a href= </a>
# 
# 

# ### Writing/reading files in python
# 
# - This week we will be working a lot with text files and strings. We will be scraping a large amount of data, which it is important to only do once (and not keep re-running the scraping script, as this takes a long time and can get you banned).
# 
# Let's see how we can write in/read in a file in python.
# 
# - [Python documentation](https://docs.python.org/3/tutorial/inputoutput.html?highlight=open%20library#reading-and-writing-files)
# 
# modes:
# 
# * "w"- write / create content to a file
# * "r" - read content from a file
# * "a"- append content to a file
# 

# In[11]:


# w: write creates a file if it doesn't exist or overwrites it if it does:
os.getcwd()

# In[375]:


f = open('Nicky_html.txt', 'w')
f.write(Nicky_html)
f.close
f1 = open('Pink_html.txt', 'w')
f1.write(Pink_html)
f1.close


# In[376]:


# r: read only, you can read in a file and save it as a variable in your code or print it
f = open('Nicky_html.txt', 'r')
Nicky_html_read=f.read()
#print(Nicky_html_read)
f.close()
f1 = open("Pink_html.txt", 'r')
Pink_html = f1.read()
f1.close()


# In[ ]:


# a: append mode adds text to the end of a file without overwriting it.


# In[377]:


f=open('Nicky_html.txt','a')
f.write('blah blah blah')
f.close


# In[43]:


f = open('Nicky_html.txt', 'r')
Nicky_html_read=f.read()
print(Nicky_html_read)
f.close()


# In[378]:


f = open('Pink_html.txt', 'r')
Pink_html_read=f.read()
print(Pink_html_read)
f.close()


# ## Extract links
# 
# - re (regular expression)
# - BeautifulSoup

# ### Inspecting a webpage
# 
# (You will need this to find links to individual songs in your artist's page.)

# #### With re

# In[45]:


import re


# In[118]:


pattern=r'<a href="(/lyric/\d+/[A-z+/%0-9]+)">'


# In[119]:


pattern


# In[154]:


re.findall(pattern,Nicky_html_read)


# And then continue ... , Here the main focus is to do that with Beautifulsoup

# #### With Beautifulsoup

# In[379]:


from bs4 import BeautifulSoup


# In[380]:



# In[388]:
os.mkdir('Pink')
os.mkdir("Minaj")
# In[389]:

nicky_soup = BeautifulSoup(Nicky_html, 'html.parser')


# In[390]:


Pink_soup = BeautifulSoup(Pink_html,'html.parser')


# Find links and name for the songs and store them  in a list

# In[396]:


links_nicky=[]
song_tit_nicky = []
for a in nicky_soup.body.find_all('a', href=True):
     if 'lyric' in a['href']:
            links_nicky.append(a['href'])
            song_tit_nicky.append(a.text)
            #print(a['href'])


# In[397]:


links_Pink=[]
song_tit_Pink = []
for a in Pink_soup.body.find_all('a', href=True):
     if 'lyric' in a['href']:
            links_Pink.append(a['href'])
            song_tit_Pink.append(a.text)
            #print(a['href'])


# In[398]:


links_nicky.remove(links_nicky[0])
song_tit_nicky.remove(song_tit_nicky[0])


# In[399]:


links_Pink.remove(links_Pink[0])
song_tit_Pink.remove(song_tit_Pink[0])


# In[358]: some checks if any non alphanumerics is in the string


for i, names in enumerate(song_tit_nicky):
           song_tit_nicky[i]=song_tit_nicky[i].replace("/", "")



"Breathe (In the Air) [5.1 Surround Mix (2003) 96KHz/24 Bit" in song_tit_nicky
          



# In[296]:


song_tit_nicky


# Randomly choose 100 songs, find their lyrics and save them

# In[400]:


i=0
while(i<100):
    #time.sleep()
    j=random.choice(range(1, len(song_tit_nicky))) #avoid replacement by deleting the chosen ones think here for the limitations ...
    URL="https://www.lyrics.com/"+links_nicky[j]
    lyrics_nicky=requests.get(url=URL, headers=headers)
    lyrics_nicky_html=lyrics_nicky.text
    lyric_nicky_soup=BeautifulSoup(lyrics_nicky_html, 'html.parser')
    print(URL)
    if lyric_nicky_soup.find(id="lyric-body-text") is None:
        continue
    lyrics_pure=lyric_nicky_soup.body.find(id="lyric-body-text").text
    with open("./Minaj/"+song_tit_nicky[j], 'w') as f:
        f.write(lyrics_pure)
        #f.close()
    i+=1
    
    


# In[401]:


i=0
while(i<100):
    #time.sleep()
    j=random.choice(range(1, len(song_tit_Pink))) #avoid replacement by deleting the chosen ones think here for the limitations ...
    URL="https://www.lyrics.com/"+links_Pink[j]
    lyrics_Pink=requests.get(url=URL, headers=headers)
    lyrics_Pink_html=lyrics_Pink.text
    lyric_Pink_soup=BeautifulSoup(lyrics_Pink_html, 'html.parser')
    print(URL)
    if lyric_Pink_soup.find(id="lyric-body-text") is None:
        continue
    lyrics_pure=lyric_Pink_soup.body.find(id="lyric-body-text").text
    with open("./Pink/"+song_tit_Pink[j], 'w') as f:
        f.write(lyrics_pure)
        #f.close()
    i+=1


# ## Data preprocessing for modelling

# #### Build lyrics corpuse for your songs using the saved lyrics in Pink and Minaj directories

# In[430]:


corpus=[]
Name_of_artists=[]
for files in os.listdir("Minaj/"):
    with open ('Minaj/'+files, "r") as f:
        corpus.append(f.read())
        Name_of_artists.append("Minaj")


# In[408]:





# In[431]:


for files in os.listdir("Pink/"):
    with open ("Pink/"+files, 'r') as f1:
        corpus.append(f1.read())
        Name_of_artists.append("Pink")


# In[406]:

len(corpus)
len(Name_of_artists)



# #### TIFVectorizer

# In[432]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[433]:


vectorizer = TfidfVectorizer(stop_words="english")


# In[436]:

from sklearn.linear_model import LogisticRegression
m = LogisticRegression()

# In[437]:
from sklearn.pipeline import Pipeline

sing_predict=Pipeline([
     ('vectorizer', vectorizer ),
     ("model", m)
     
])


# In[439]:
from sklearn.model_selection import train_test_split

X=corpus
y=Name_of_artists
X_train, X_test, y_train, y_test= train_test_split(X, y, random_state=423)




# In[450]:


sing_predict.fit(X_train, y_train)


# In[453]:
sing_predict.score(X_train, y_train)
sing_predict.predict_proba(['we don"t need no education'])

# In[454]:
import pickle
with open('guess_singer.pkl', 'wb') as f:
	pickle.dump(sing_predict, f)





# In[459]:





# ### FIT TO LOGISTICREGRESSION

# In[460]:






# In[461]:





# In[463]:





# In[465]:





# In[ ]:




