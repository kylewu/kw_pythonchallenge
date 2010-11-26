#!/usr/bin/env python

'''

    Author:
        Kyle Wu <imkylewu@gmail.com>
        http://www.kylewu.net
 
    File:             p5.py
    Create Date:      Fri Nov 26 10:11:24 2010

    http://www.pythonchallenge.com/pc/def/peak.html
'''

import urllib
import pickle

if __name__ == "__main__":

    p = handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    data = pickle.load(p)
    print type(data)
    for elm in data:
        print "".join([e[0] * e[1] for e in elm])
        #print elm

