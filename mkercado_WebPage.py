from vpython import *
#GlowScript 3.1 VPython
from random import seed
#Code borrowed from 
#https://glowingpython.blogspot.com/2013/01/box-muller-transformation.html
#Adapted to Glowscript by D. O'Neil
##################################

#set up start progam, if then statement
n=100
press=0
def B(b):
    def T(n):
        print (s.text, s.number)
    winput (bind=T)
    n=input ('type number') 
    seed()
#Generates a random number according to a Gaussian [normal] distribution 
    def gaussian():
        u1 = random()
        u2 = random()
        t = sqrt(-2*log(u1))*cos(2*pi*u2)
        x = sqrt(-2*log(u1))*sin(2*pi*u2)
        return x  #could also return t by writing return x,t

#we are going to store the output in a list (xlist)
        #n = 100 #choose how many points you want ***********IMPORTANT********
    i = 0
    mean = random()*200
    sd= random()*(5)
    xlist=[0 for x in range(n)] #initialize the list
    while(i<n):
        xlist[i] =  gaussian()*sd+mean #call the generator function
        i+=1
    print ("data")
    for j in range (n):    
        print(xlist[j])
    print ("")

#set up straph
button ( bind=B, text='Create new measurement')
scene.append_to_caption('\n\n')

