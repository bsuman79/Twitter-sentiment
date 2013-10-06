"""
Author Suman Bhattacharya
measure sentiment of the tweets
"""
import sys
import json
import pprint
#import numpy as np
import re

#from pylab import *
#import matplotlib.pyplot as plt
#from matplotlib import rc
#import matplotlib.mlab as mlab

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def tweettext(fp):
      tw=[]
      d=fp.readlines()
      for line in d:
        data= json.loads(line) #line.split(',')
        if 'text' in data:
           tw.append(data[u'text'])  #.decode('utf-8', errors='ignore')
      return  tw 


def senttext(fp):
    word = []
    value=[]
    data=fp.readlines()
    for line in data:
       ct= len(line.split())
       value.append(line.split()[ct-1])
       s="" 
       for  j in range (ct-2): s+=str(line.split()[j]) +' '
       for j in range (ct-2,ct-1): s+= str(line.split()[j])
       word.append(s)
    return list(word), list(value)        

def findword(tweet, word):
  count=0
  tmp=tweet.split()
  for k in range (len(tmp)):
    if word == tmp[k]:
      count=count+1
  return count, word, tweet

def plothist(y):
    ax = subplot(    1,     1,    1)
    ax.hist(y, 50, normed=1, facecolor='green', alpha=0.75)
    show()

def measent(tweet, word, val):
    senti=[]
    for i in range (0,len(tweet)):
       value=0.0
       # count=count+findword(tweet[i], 'first')
       tmp=tweet[i].split()
       for j in range (len(word)):
         for k in range (len(tmp)):
           if word[j] ==tmp[k]:
            ind=word.index(word[j]) 
            value+=float(val[ind]) 
       #print value
       senti.append(float(value))
    return senti #np.array(senti)

def removewords(s):
    L = []
    for word in s.split():
        if not word.startswith('@') and not word.startswith('http'):
            L.append(word)
    return ' '.join(L)

def cleantweet(tweet):
    tweetuni=[]
    for i in range (len(tweet)):
          tmp=tweet[i].encode('utf-8')
          tmp1 = re.sub('[|!#$)(;.,"]', '', tmp)
          if 'RT' in tmp1:
              left,split, right= tmp1.partition(':')
              #tmp1=re.sub(r'@\w+\s?','',right)
              tmp1= right
          tmp2= removewords(tmp1)
          tweetuni.append(re.sub('[:]','',tmp2))
    return tweetuni

def main():
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    #lines(sent_file)
    #lines(tweet_file)
    tweet=tweettext(tweet_file)
    twclean= cleantweet(tweet)
    word, val= senttext(sent_file) 
    #print word
    senti= measent(twclean,word,val)
    for i in range (len(senti)):  print senti[i]
    #for i in range (len(word)):
    #   ct, word1, tw= findword(twclean[41],word[i])
    #   if ct==1: print ct, word1, tw, senti[41] 
    #print "# ",sum(senti), min(senti), max(senti), mean(senti), median(senti)
    #plothist(senti)
    #print "first occured", count, " times in", len(tweet)," tweets"

if __name__ == '__main__':
    main()
