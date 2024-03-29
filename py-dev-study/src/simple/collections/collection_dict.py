# -*- coding: utf-8 -*-
'''
Created on 2010-7-3

@author: me
'''
def dictTest():
        # 'ab' is short for 'a'ddress'b'ook
        
        ab = {       
              'Swaroop'   : 'swaroopch@byteofpython.info',
               'Larry'     : 'larry@wall.org',
               'Matsumoto' : 'matz@ruby-lang.org',
               'Spammer'   : 'spammer@hotmail.com'
        }
        
        print("Swaroop's address is %s"   % ab['Swaroop'])
        
        # Adding a key/value pair
        ab['Guido'] = 'guido@python.org'
        
        # Deleting a key/value pair
        del ab['Spammer']
        
        print('key set:' , list(ab.keys()))
        print('value list: ' , list(ab.values()))
        
        print('\nThere are %d contacts in the address-book\n' % len(ab))
        for name, address in list(ab.items()):
            print('Contact %s at %s' % (name, address))
        
        if 'Guido' in ab: # OR ab.has_key('Guido')
            print("\nGuido's address is %s" % ab['Guido'])
        
        print('---------help----------')
        print(help(dict))
      
def dictTest1():
        d = dict(
                 [('sape', 4139), 
                  ('guido', 4127), 
                  ('jack', 4098)]
         )
        
        dd = dict(sape=4139, guido=4127, jack=4098)
        
        print(d)
        print(dd)

        

  
if __name__ == '__main__' :
    dictTest()
    dictTest1()