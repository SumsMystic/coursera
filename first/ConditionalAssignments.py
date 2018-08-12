'''
Created on Apr 2, 2018

@author: Sumeet Agrawal
'''

hrs = input("Enter Hours:")
h = float(hrs)
rateperhour = input("Enter Rate Per Hour:")
r = float(rateperhour)
if(h < 40):
    totalpay = h * r
else:
    totalpay = (40 * r) + (1.5 * (h-40) * r)
print(totalpay)