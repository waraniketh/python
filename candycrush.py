'''
Created on 08-Jun-2017

@author: hduser
'''
guess=raw_input("enter your crush")
listing="aditya"
match=0
for ch in listing:
    for ch1 in guess:
        if(ch==ch1):
            match=match+1
if(match>7):
    print "waaaawwwww"

toverify="all the best"
for i in range(3,5):
    print toverify 
print toverify[3:7]    