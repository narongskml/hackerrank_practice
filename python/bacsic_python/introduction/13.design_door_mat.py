#    Size: 7 x 21 
#    ---------.|.---------
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------
    
#    Size: 11 x 33
#    ---------------.|.---------------
#    ------------.|..|..|.------------
#    ---------.|..|..|..|..|.---------
#    ------.|..|..|..|..|..|..|.------
#    ---.|..|..|..|..|..|..|..|..|.---
#    -------------WELCOME-------------
#    ---.|..|..|..|..|..|..|..|..|.---
#    ------.|..|..|..|..|..|..|.------
#    ---------.|..|..|..|..|.---------
#    ------------.|..|..|.------------
#    ---------------.|.---------------

# 9 x 27
#------------.|.------------
#---------.|..|..|.---------
#------.|..|..|..|..|.------
#---.|..|..|..|..|..|..|.---
#----------WELCOME----------
#---.|..|..|..|..|..|..|.---
#------.|..|..|..|..|.------
#---------.|..|..|.---------
#------------.|.------------

l = 9
w = 27
#top 
for i in range(l//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(w, '-'))    # print item loop with center and fill with -

print('WELCOME'.center(w,'-'))  # center

#buttom
for i in reversed(range(l//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(w, '-'))     # print item loop with center and fill with -   reverse