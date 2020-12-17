# Find multiples of five and three and sum it 'till N
def multiples(n):
    sum = 0
    for num in range(n):
        if num%3 == 0 or num%5 == 0:
            sum += num
    return sum

multiples(1000)
