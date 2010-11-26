'''

    Author:
        Kyle Wu <imkylewu@gmail.com>
        http://www.kylewu.net
 
    File:             p4.py
    Create Date:      Wed Nov 24 22:08:13 2010

    http://www.pythonchallenge.com/pc/def/linkedlist.php
'''

import urllib
import re

if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    #num = "12345"
    # 92118 Yes. Divide by two and keep going.
    num = "46059"
    # 65667 peak.html

    while 1:
        data = urllib.urlopen(url + num).read()
        num =  "".join(re.findall("and the next nothing is ([0-9]+)", data))
        print num
