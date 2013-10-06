"""
Author Suman Bhattacharya
calculate the frequency of the words of the tweets
"""
import sys
import json
import re

def tweettext(fp):
      tw=[]
      d=fp.readlines()
      for line in d:
        data= json.loads(line) #line.split(',')
        if 'text' in data:
           tw.append(data[u'text'])  #.decode('utf-8', errors='ignore')
      return  tw 

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
          """tmp1 = re.sub('[|!#$)(;.,"]', '', tmp)
          if 'RT' in tmp1:
              left,split, right= tmp1.partition(':')
              #tmp1=re.sub(r'@\w+\s?','',right)
              tmp1= right
          tmp2= removewords(tmp1)"""
          tweetuni.append(tmp) #(re.sub('[:]','',tmp2))
    return tweetuni

def meafretwrwords(tweet):
    fre=[]
    twitword1=[]
    for i in range (len(tweet)):
       twitword=tweet[i].split()
       for j in range (len(twitword)):
           if twitword[j] not in twitword1:
                   twitword1.append(twitword[j])
                   ct=1.0
                   fre.append(ct)
           else:
                   ind=twitword1.index(twitword[j])
                   fre[ind] = float(fre[ind])+ 1.0
    return twitword1, fre

def main():
    tweet_file = open(sys.argv[1])
    tweet=tweettext(tweet_file)
    twclean= cleantweet(tweet)
    twitwords, twitwordfreq= meafretwrwords(twclean)
    #print len(twitwords), len(twitwordfreq)
    norm=1.0/sum(twitwordfreq) 
    for i in range (len(twitwords)): print twitwords[i], twitwordfreq[i]*norm
    #print twitwords[twitwordfreq.index(max(twitwordfreq))]
    #plothist(twitwordfreq)
    
if __name__ == '__main__':
    main()
