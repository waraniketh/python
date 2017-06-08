'''
Created on 08-Jun-2017

@author: hduser
'''

ani=raw_input("enter the string")
vowel="aeiou"
counting=0

for ad in vowel:
            print ad+" "+str(ani.count(ad))       
#print ani
for ch in vowel:
    counting=0
    for ch1 in ani:
        if(ch==ch1):
            counting=counting+1
    if(counting>0):        
        print ch+" "+str(counting)        