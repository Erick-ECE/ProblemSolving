#asteroidCollision most frecuent asked in Lyft and Amazon

def asteroidCollision(asteroids):
    stack = []
    top= 0
    i=0
    while i < len(asteroids):
        if asteroids[i] > 0:
            stack.append(asteroids[i])
            top=stack[-1] if stack!=[] else 0
        else:
            while (stack!=[]) and (top>0) and (top<abs(asteroids[i])):
                stack.pop()
                top=stack[-1] if stack!=[] else 0
            if stack == [] or top<0:
                stack.append(asteroids[i])
                top=stack[-1]
            elif top == abs(asteroids[i]):
                stack.pop()
                top=stack[-1] if stack!=[] else 0
        i+=1
    return stack

        
                

        
#INPUTS             #OUTPUTS
l1=[5,10,-5]        # [5,10]
l2=[8,-8]           #[]
l3=[10,2,-5]        #[10]
l4=[-2,-1,1,2]      #[-2,-1,1,2]
l5=[-2,-2,1,-2]     #[-2,-2,-2]
l7=[-2,-1,1,-2]     #[-2,-1,-2]
l8=[-2,1,-1,-1]     #[-2,-1]
l9=[-2,1]           #[-2,1]



asteroidCollision(l1)
asteroidCollision(l2)
asteroidCollision(l3)
asteroidCollision(l4)
asteroidCollision(l5)
asteroidCollision(l7)
asteroidCollision(l8)
asteroidCollision(l9)



