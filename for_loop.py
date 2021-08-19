# AUTHOR - HIMANK JESHWAR
# DATE - 19/08/21

'''PROBLEM : -
    Find the Sum of First 10 natural numbers using For Loop'''
sumNo=0
for naturalNo in range(1,11):
    sumNo+=naturalNo
    naturalNo-=1
print(f"The Sum of First 10 natural numbers = {sumNo}")   

# This Program Works Like This : -
'''
As naturalNo=10 and initially we have taken sumNo=0 

sumNo+=naturalNo => here sumNo = (0+10=10) and value of naturalNo is 10

sumNo+=naturalNo => here sumNo=(10+9=19) as naturalNo = 9 here,decreased 
                 by 1 due to naturalNo-=1     

sumNo+=naturalNo => here sumNo = (19+8=27) as naturalNo = 8 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo => here sumNo = (27+7=34) as naturalNo = 7 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo => here sumNo = (34+6=40) as naturalNo = 6 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo => here sumNo = (40+5=45) as naturalNo = 5 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo => here sumNo = (45+4=49) as naturalNo = 4 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo => here sumNo = (49+3=52) as naturalNo = 3 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo =>here sumNo = (52+2=54) as naturalNo = 2 here,decreased 
                 by 1 due to naturalNo-=1

sumNo+=naturalNo =>here sumNo = (54+5=55) as naturalNo = 1 here,decreased 
                 by 1 due to naturalNo-=1 '''

                #  The Final Answer = 55