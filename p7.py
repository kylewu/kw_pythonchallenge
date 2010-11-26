'''

    Author:
        Kyle Wu <imkylewu@gmail.com>
        http://www.kylewu.net
 
    File:             p7.py
    Create Date:      Fri Nov 26 11:10:24 2010

	http://www.pythonchallenge.com/pc/def/oxygen.html
    
'''

#TODO don't know why
import urllib
import os
import Image
import re

if __name__ == "__main__":
    source = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    save_as = 'temp.png'
    urllib.urlretrieve(source, save_as)

    i = Image.open(save_as)
    row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
    ords = [r for r, g, b, a in row if r == g == b]
    print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))
    

    #box = ()
    #region = image.crop(box)
    os.remove(save_as)
