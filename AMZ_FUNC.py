
# coding: utf-8

# In[1]:

import bottlenose
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import pandas as pd
import os

def get_reviews(isbn):
    AWS_ACCESS_KEY_ID='XXX' # insert key ID
    AWS_SECRET_ACCESS_KEY='ZZZzz' #insert access key
    AWS_ASSOCIATE_TAG='zzz' #insert tag
    amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)
    
    response = amazon.ItemLookup(ItemId=isbn, ResponseGroup="SalesRank, ItemAttributes, Reviews, Small", SearchIndex="Books", IdType="ISBN", IncludeReviewsSummary=True)
    soup = BeautifulSoup(response, "lxml")
    try:
        stem_url = soup.find_all("url")[5]
    except IndexError:
        return [isbn, 'NA', 'NA']
    else:
        pass
    text_parts = stem_url.findAll(text=True)
    text = ''.join(text_parts)
    
    html = urlopen(text).read()
    new_soup = BeautifulSoup(html, "lxml")
    
    new_soup.select(".asinReviewsSummary ")
    stars = new_soup.select(".asinReviewsSummary")
    findstars = BeautifulSoup(str(stars))
    try:
        avg_review = findstars.find_all(text=True)[2]
    except IndexError:
        return [isbn, 'NA', 'NA']
    else:
        pass
    score = avg_review.split()[0]
    
    total_stars = new_soup.select("a")[25]
    find_total_stars = BeautifulSoup(str(total_stars))
    total_stars = find_total_stars.find_all(text=True)[0]
    total_reviews = total_stars.split()[0]
    
    results = [isbn, score, total_reviews]
    
    return results

#get_reviews('0307887189')
amazon_reviews = []

books = pd.read_csv("/Users/gabelev/projects/AMZ/S2010F2013.csv")[0:20]
#print books

for row_index, row in books.iterrows():
    call_rev = get_reviews((row)['ISBN'])
    amazon_reviews.append(call_rev)


# In[2]:

print amazon_reviews


# In[ ]:

books = pd.read_csv("/Users/gabelev/projects/AMZ/cb_100_alt2.csv")[21:40]
#print books

for row_index, row in books.iterrows():
    call_rev = get_reviews((row)['ISBN'])
    amazon_reviews.append(call_rev)

print amazon_reviews


# In[5]:

books = pd.read_csv("/Users/gabelev/projects/AMZ/cb_100_alt2.csv")[41:60]
#print books

for row_index, row in books.iterrows():
    call_rev = get_reviews((row)['ISBN'])
    amazon_reviews.append(call_rev)

print amazon_reviews


# In[7]:

books = pd.read_csv("/Users/gabelev/projects/AMZ/cb_100_alt2.csv")[61:80]
#print books

for row_index, row in books.iterrows():
    call_rev = get_reviews((row)['ISBN'])
    amazon_reviews.append(call_rev)

print amazon_reviews


# In[8]:

books = pd.read_csv("/Users/gabelev/projects/AMZ/cb_100_alt2.csv")[81:100]
#print books

for row_index, row in books.iterrows():
    call_rev = get_reviews((row)['ISBN'])
    amazon_reviews.append(call_rev)

print amazon_reviews


# In[9]:

books = pd.read_csv("/Users/gabelev/projects/AMZ/cb_100_alt2.csv")[100:120]
#print books

for row_index, row in books.iterrows():
    call_rev = get_reviews((row)['ISBN'])
    amazon_reviews.append(call_rev)

print amazon_reviews


# In[12]:

print amazon_reviews

import csv

resultFile = open("output3.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(amazon_reviews)


# In[13]:

final_books = pd.read_csv("/Users/gabelev/projects/AMZ/cb_100_alt3.csv")
#print final_books.head()
final_books.set_index('ISBN')


# In[15]:

final_results = pd.read_csv("/Users/gabelev/projects/AMZ/output2.csv")
#print final_books.head()
final_results.set_index('ISBN')


# In[17]:

final_totals = pd.merge(final_books, final_results)


# In[25]:

print final_totals


# In[24]:

final_totals


# In[27]:

final_totals.to_csv("final_output44.csv")


# In[ ]:



