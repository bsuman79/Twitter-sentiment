"""
Author Suman Bhattacharya
place the tweets into which state they originated from using geo spatial data, then do the sentiment analysis of the tweets, sort the top ten happiest states in the US.
"""
import sys
import json
import pprint
import re
state=[u'WA',u'VA',u'DE',u'DC',u'WI',u'WV',u'HI',u'FL',u'WY',u'NH',u'NJ',u'NM',u'TX',u'LA',u'NC',u'ND',u'NE',u'TN',u'NY',u'PA',u'CA',u'NV',u'PR',u'CO',u'AK',u'AL',u'AR',u'VT',u'IL',u'GA',u'IN',u'IA',u'OK',u'AZ',u'ID',u'CT',u'ME',u'MD',u'MA',u'OH',u'UT',u'MO',u'MN',u'MI',u'RI',u'KS',u'MT',u'MS',u'SC',u'KY',u'OR',u'SD']
minlat=[46,37, 39, 39, 43, 37, 20, 25, 41, 43, 39, 32, 26, 30, 34, 46, 40, 35, 40, 40, 33, 36, 18, 39, 55, 31, 33, 43, 38, 31, 38, 40, 34, 31, 42, 41, 43, 38, 41, 39, 37, 36, 44, 42, 41, 37, 45, 30, 32, 37, 42, 43]
maxlat=[49, 39, 40, 39, 47, 40, 22, 31, 45, 44, 41, 37, 36, 33, 36, 48, 42, 37, 45, 42, 41, 41, 30, 40, 71, 35, 36, 45, 42, 35, 42, 43, 37, 35, 48, 42, 47, 40, 43, 42, 42, 40, 47, 47, 42, 40, 49, 35, 35, 39, 46, 45]
minlon=[-124, -82, -76, -77, -93, -82, -159, -87, -111, -72, -75, -109, -106, -94, -83, -104, -104, -90, -79, -80, -124, -120, -98, -106, -165, -88, -95, -73, -91, -85, -88, -96, -101, -115, -117, -74, -71, -79, -73, -85, -114, -95, -97, -87, -72, -101, -114, -91, -83, -89, -124, -104]
maxlon=[-117, -76, -75, -77, -87, -78, -155, -80, -104, -71, -74, -103, -94, -90, -76, -97, -96, -82, -73, -75, -115, -114, -65, -105, -132, -85, -90, -72, -88, -81, -85, -90, -95, -110, -112, -72, -68, -76, -70, -81, -111, -90, -92, -82, -71, -95, -104, -88, -79, -83, -117, -97]
def tweettext(fp):
      tw, tw1=[],[]
      d=fp.readlines()
      for line in d:
        data= json.loads(line)
        if 'text' in data:
           tw.append(data[u'text']) 
           tw1.append(data['coordinates'])
      return  tw, tw1 
def sentistate(sent, co):
    snt, lon, lat=[],[],[]
    for i in range (len(sent)): 
        if co[i] is not None: 
           snt.append(sent[i])   
           lon.append(co[i]['coordinates'][0])
           lat.append(co[i]['coordinates'][1])
    statesent=[0]*(len(state))
    for j in range (len(state)):
        for i in range (len(snt)):
            if lat[i] !=0.0 and lon[i] !=0.0:
                if float(minlat[j])/float(lat[i])<1.0 and float(maxlat[j])/float(lat[i])>1.0 and float(maxlon[j])/float(lon[i])<1.0 and float(minlon[j])/float(lon[i])>1.0:
                   statesent[j] += snt[i]
    return dict(zip (state, statesent))
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
       tmp=tweet[i].split()
       for j in range (len(word)):
         for k in range (len(tmp)):
           if word[j] ==tmp[k]:
            ind=word.index(word[j]) 
            value+=float(val[ind]) 
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
              tmp1= right
          tmp2= removewords(tmp1)
          tweetuni.append(re.sub('[:]','',tmp2))
    return tweetuni
def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
def main():
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    tweet, co=tweettext(tweet_file)
    twclean= cleantweet(tweet)
    word, val= senttext(sent_file) 
    senti= measent(twclean,word,val)
    tally=sentistate(senti, co)
    print keywithmaxval(tally)
if __name__ == '__main__':
    main()
