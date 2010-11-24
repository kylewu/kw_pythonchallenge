"""
Problem 1 : http://www.pythonchallenge.com/pc/def/map.html
"""

import string

if __name__ == "__main__":
    str = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    tran = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:]+string.ascii_lowercase[0:2])
    
    print str.translate(tran)
    print 'map'.translate(tran)
