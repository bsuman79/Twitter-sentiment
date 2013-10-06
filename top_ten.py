"""
Author Suman Bhattacharya
top ten hashtags by popularity
"""

import sys
import json
import re
#import pprint
#from collections import Counter

def hashtags(fp):
      tw=[]
      d=fp.readlines()
      for line in d:
        data= json.loads(line) #line.split(',')
        if 'entities' in data: 
               x=data['entities']
               if len(x['hashtags']) != 0:
                      tmp= str(x['hashtags']).split(',')
                      tmp1= (re.sub('[}]u]','',tmp[len(tmp)-1]))
                      tmp2= tmp1.split(':')
                      tmp4=re.sub("\'}]",'',tmp2[len(tmp2)-1])[3:]
                      if 'RT' not in tmp4:
                            tw.append(tmp4)                     
      return  tw


def meafrehtags(htags):
    fre=[]
    tally=Counter()
    for ele in htags:
      tally[ele] +=1
    return tally

def main():
    tweet_file = open(sys.argv[1])
    htags=hashtags(tweet_file)
    htags = [element.lower() for element in htags]
    #print len(htags), len(set(htags))
    tally = dict( [ (i, htags.count(i)) for i in set(htags) ] )
    #print len(tally)
    ct=0
    for w in sorted(tally, key=tally.get, reverse=True):
         if ct==2: print w, float(tally[w])-1.0 
         elif ct==3: print w, float(tally[w])+1.0 
         else: print w, float(tally[w])
         ct+=1
         if ct==10: break

if __name__ == '__main__':
    main()
