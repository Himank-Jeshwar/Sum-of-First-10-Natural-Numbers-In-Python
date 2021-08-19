# AUTHOR - HIMANK JESHWAR
# DATE - 19/08/21

''' PROBLEM :-
    Find the Sum of First 10 Natural Numbers using While Loop'''
naturalNo=10
sumNo=0
while naturalNo>0:
    sumNo+=naturalNo
    naturalNo-=1 
print(f"The Sum of First 10 natural numbers = {sumNo}") 

# This Program Works Like This :-
''' 
sumNo+=10=> sumNo = (0+10=10) and the value of naturalNo = 10
sumNo+=9 => sumNo = (10+9=19) and now naturalNo = 9 (decreased by 1 due to naturalNo-=1)
sumNo+=8 => sumNo = (19+8=27) and now naturalNo = 8 (decreased by 1 due to naturalNo-=1)
sumNo+=7 => sumNo = (27+7=34) and now naturalNo = 7 (decreased by 1 due to naturalNo-=1)
sumNo+=6 => sumNo = (34+6=40) and now naturalNo = 6 (decreased by 1 due to naturalNo-=1)
sumNo+=5 => sumNo = (40+5=45) and now naturalNo = 5 (decreased by 1 due to naturalNo-=1)
sumNo+=4 => sumNo = (45+4=49) and now naturalNo = 4 (decreased by 1 due to naturalNo-=1)
sumNo+=3 => sumNo = (49+3=52) and now naturalNo = 3 (decreased by 1 due to naturalNo-=1)
sumNo+=2 => sumNo = (52+2=54) and now naturalNo = 2 (decreased by 1 due to naturalNo-=1)
sumNo+=1 => sumNo = (54+1=55) and now naturalNo = 1 ''' 
                # The Final Answer i.e, 55