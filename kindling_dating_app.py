# -*- coding: utf-8 -*-
"""kindling dating app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pk_0Iq5uAd3nKq7mTynPS6VdxxQ9wHpD
"""

#@title Run this to import random bios { display-mode: "form" }

import requests
import pandas as pd
import time
import random
import re
import numpy as np
import _pickle as pickle
from tqdm import tqdm_notebook as tqdm
from bs4 import BeautifulSoup as bs


## Using BeautifulSoup

# Randomizing the refresh rate
seq = [i/10 for i in range(8,18)]

# Creating a list of bios
biolist = []

# Gathering bios by looping and refreshing the web page
for _ in tqdm(range(100)):
    
    # Refreshing the page
    page = requests.get("https://www.fakepersongenerator.com/user-biography-generator?new=refresh")
    soup = bs(page.content)
    
    try:
        # Getting the bios
        bios = soup.find('div', class_='row no-margin for-sign').find_all('p')

        # Adding to a list of the bios
        biolist.extend([re.findall('"([^"]*)"', i.text) for i in bios])
    except:
        pass
    
    # Sleeping 
    time.sleep(random.choice(seq))
    
# Creating a DF from the bio list
bio_df = pd.DataFrame(biolist, columns=['Bios'])

#@title More stuff on adding topics to our profiles (1-10 for how much you are interested in each topic) { display-mode: "form" }
length=len(bio_df)
ageList=[]
genderList=[]
topics=['Movies', 'Video Games', 'Politics']
topicsList=[]
for i in range(length):
  ageList.append(random.randint(13, 25))
  genderList.append(random.randint(0, 1))
  topicsList.append([random.randint(1, 10), 
                     random.randint(1, 10), random.randint(1, 10)])

age_df = pd.DataFrame(ageList, columns=['Age'])
gender_df = pd.DataFrame(genderList, columns=['Gender'])
topics_df = pd.DataFrame(topicsList, columns=topics)

df=bio_df.join(age_df).join(gender_df).join(topics_df)

print(df.head().to_markdown())

#@title teach the computer english
import re
import gdown
import seaborn as sns
import pandas as pd
import numpy as np
from torchtext.vocab import GloVe
from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib
import matplotlib.pyplot as plt
import requests, io, zipfile

VEC_SIZE = 300
glove = GloVe(name='6B', dim=VEC_SIZE)

# Returns word vector for word if it exists, else return None.
def get_word_vector(word):
    try:
      return glove.vectors[glove.stoi[word.lower()]].numpy()
    except KeyError:
      return None

#@title testing the cool word simularity machine { run: "auto", display-mode: "both" }

def cosine_similarity(vec1, vec2):    
  return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

word1 = "ethnicity" #@param {type:"string"}
word2 = "potatoes" #@param {type:"string"}

print('Word 1:', word1)
print('Word 2:', word2)

def cosine_similarity_of_words(word1, word2):
  vec1 = get_word_vector(word1)
  vec2 = get_word_vector(word2)
  
  if vec1 is None:
    print(word1, 'is not a valid word. Try another.')
  if vec2 is None:
    print(word2, 'is not a valid word. Try another.')
  if vec1 is None or vec2 is None:
    return None
  
  return cosine_similarity(vec1, vec2)
  

print('\nCosine similarity:', cosine_similarity_of_words(word1, word2))

def getBioVector(bio):
  bio=bio.strip()
  found_words=0.0
  X=np.zeros(VEC_SIZE)
  for word in bio.split():  
    vec = get_word_vector(word)
    if vec is not None:
        found_words += 1
        X += vec
  if found_words > 0:
        X /= found_words
  return X
def getBioScore(bio1, bio2):
  return cosine_similarity(getBioVector(bio1), getBioVector(bio2))

bio1 = "I play minecarft and click quickly on kids" #@param {type:"string"}
bio2 = "I am such an environmentalist" #@param {type:"string"}

print('Bio 1:', bio1)
print('Bio 2:', bio2)
print('\nCosine similarity:', getBioScore(bio1, bio2))

def bestMatches(person, lim):
  matches=[]
  for i in range(len(df)):
    if(i!=person):
      if(abs(df['Age'][i]-df['Age'][person]) <= 2 and df['Gender'][i]!=df['Gender'][person]):
        matches.append([getBioScore(df['Bios'][i], df['Bios'][person]), i] )
  matches.sort(reverse=True)
  for i in range(min(lim, len(matches))):
    print(matches[i][1], df['Bios'][matches[i][1]])

print("THIS GUY MATCHES WITH:", df['Bios'][0])

bestMatches(0, 5)