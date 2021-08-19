# AUTHOR - HIMANK JESHWAR
# DATE - 19/08/21

'''Problem : -
    Find out the sum of First 10 natural numbers using recursion'''
def total(n):
    if n==0:
        return 0
    else:
        return n+total(n-1) 
num=10
print(f"Sum of First {num} natural numbers = {total(num)}") 

# This Problem works like this : - 
''' 10+[9+total(8)]
    10+9+[8+total(7)]
    10+9+8+[7+total(6)]
    10+9+8+7+[6+total(5)]
    10+9+8+7+6+[5+total(4)]
    10+9+8+7+6+5+[4+total(3)]
    10+9+8+7+6+5+4+[3+total(2)]
    10+9+8+7+6+5+4+3+[2+total(1)]
    10+9+8+7+6+5+4+3+2+[1]
'''
    # Answer = 55