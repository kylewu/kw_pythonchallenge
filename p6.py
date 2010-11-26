'''

    Author:
        Kyle Wu <imkylewu@gmail.com>
        http://www.kylewu.net
 
    File:             p6.py
    Create Date:      Fri Nov 26 10:39:57 2010

    http://www.pythonchallenge.com/pc/def/channel.html
'''

import zipfile
import re
import urllib
import os

if __name__ == "__main__":
    source = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    save_as = 'temp.zip'
    urllib.urlretrieve(source, save_as)

    zf = zipfile.ZipFile(save_as, 'r')
    f = '90052'
    res = []

    print zf.read('46145.txt')

    while 1:
        try:
            data = zf.read('%s.txt' % f)
            f = "".join(  re.findall("is ([0-9]+)", data) )
            res.append(zf.getinfo('%s.txt' % f).comment)
            print f
        except:
            print "".join(res)
            break

    os.remove(save_as)
