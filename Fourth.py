'''
Created on 08-Jun-2017

@author: hduser
'''
import random
from Crypto.Random.random import randint

ro=0
print "enter your number"
while(ro==0):
    print "try again"
    d=randint(0,50)
    guess=int(raw_input())
    if(guess==d):
        print "correct"
        ro=1
    else:
        if(guess>d):
             print "guess lower"
        else:
             print "guess higher"
        
 