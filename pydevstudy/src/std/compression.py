'''
Created on 2011-3-13

@author: me
'''
import zlib
s = 'witch which has which witches wrist watchwitch which has which witches wrist watch'
print('source len',len(s))

t = zlib.compress(s)
print('compress len', len(t))

print(zlib.decompress(t))
print(zlib.crc32(s))
