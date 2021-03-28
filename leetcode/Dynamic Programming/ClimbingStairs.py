#Climbing Stairs

#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# recursive algorithm
def climbStairs(n):
    if n == 0 : return 0
    if n == 1 or n ==2:
        return n
    return climbStairs(n-1)+climbStairs(n-2)   

climbStairs(4)


# Tail recursion:
def climbSt(n):
    return climbAux(n,1,1)
def climbAux(n,b,a):
    if n == 0: return b
    if n == 1: return a
    return climbAux(n-1,a,b+a)

climbSt(3)

