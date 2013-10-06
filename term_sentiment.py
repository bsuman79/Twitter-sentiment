"""
Author Suman Bhattacharya
place the tweets into which state they originated from using geo spatial data, then do the sentiment analysis of the tweets, sort the top ten happiest states in the US.
"""
import sys
import sys
import json
import re

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
    return senti

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
"""
def measenttwrwords(tweet, word, sent):
    senti=[]
    twitword1=[]
    unwantedwords=['have','had','did','The','I','you','My','at','an','so','him','her','has','This','A','in','the','my','to']
    for i in range (len(tweet)):
       twitword=tweet[i].split()
       for j in range (len(twitword)):
         if twitword[j] not in word and twitword[j] not in unwantedwords:
            if len(twitword1)==0:
                   twitword1.append(twitword[j])
                   senti.append(sent[i])
            ctr=0
            if twitword[j] in twitword1:
                   ind=twitword1.index(twitword[j])
                   #print ind
                   senti[ind] = float(senti[ind]) +float(sent[i])
                   ctr+=1  
                   if ctr==1: break                  
            if ctr==0:
                   twitword1.append(twitword[j])
                   senti.append(sent[i])
    return twitword1, senti
"""
def measenttwrwords(tweet, word, sent):
    senti=[]
    twitword1=[]
    for i in range (len(tweet)):
       twitword=tweet[i].split()
       for j in range (len(twitword)):
         if twitword[j] not in word:
           if twitword[j] not in twitword1:
                   twitword1.append(twitword[j])
                   senti.append(sent[i])
           else:
                   ind=twitword1.index(twitword[j])
                   #print ind
                   senti[ind] = float(senti[ind]) +float(sent[i])
    return twitword1, senti

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    tweet=tweettext(tweet_file)
    twclean= cleantweet(tweet)
    #for i in range(len(twclean)): print i, twclean[i]
    word, val= senttext(sent_file)  
    sent= measent(twclean,word,val)
    twitwords, twitwordsent= measenttwrwords(twclean,word,sent)
    #print len(twitwords), len(twitwordsent)
    for i in range (len(twitwords)): print twitwords[i], twitwordsent[i]
    
if __name__ == '__main__':
    main()
