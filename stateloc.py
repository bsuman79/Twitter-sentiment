import sys
import json
import pprint
#import numpy as np
import re
from decimal import *
#from pylab import *
#import matplotlib.pyplot as plt
#from matplotlib import rc
#import matplotlib.mlab as mlab

def lines(fp):
    print str(len(fp.readlines()))

def stateloc(fp):
      minlat, maxlat,minlon,maxlon, st=[],[],[],[],[]
      state={}
      data= json.loads(fp.read()) 
      skey=data['US']['states'].keys()
      for j in range (len(skey)):
          state=data['US']['states'][skey[j]]['cities']
          ckey=state.keys()  
          lat,lon=[],[]
          for i in range (len(ckey)):
               tmp1,tmp2=state[ckey[i]]['coordinates'].split(',') 
               #print skey[j],float(tmp1), float(tmp2)
               lat.append(float(tmp1)), lon.append(float(tmp2))
               #, state[ckey[i]]['name']
          if len(lat) >0: 
               minlat.append(min(lat)),maxlat.append(max(lat)),minlon.append(min(lon)),maxlon.append(max(lon)), st.append(skey[j])
      return st, minlat, maxlat, minlon, maxlon



def main():
    state_file = open(sys.argv[1],'r')
    state, minlat,maxlat,minlon,maxlon=stateloc(state_file)
    #for i in range(len(state)): print i,state[i],minlat[i],maxlat[i],minlon[i],maxlon[i]
    print state
    print [float(Decimal("%.0f" %e)) for e in minlat]
    print [float(Decimal("%.0f" %e)) for e in maxlat]
    print [float(Decimal("%.0f" %e)) for e in minlon]
    print [float(Decimal("%.0f" %e)) for e in maxlon]
if __name__ == '__main__':
    main()
