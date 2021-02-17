# LeetCode Move Zeroes
#Given an array nums, write a function to move all 0's 
# to the end of it while maintaining the relative order of the non-zero elements

lista = [0,1,0,3,12]
count=-1
while True:
    try:
        count+=1
        lista.remove(0)
    except:
        break
for i in range(count):
    lista.append(0)
