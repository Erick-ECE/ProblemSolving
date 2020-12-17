# Write a function that takes a number and returns a list of its digits
def digits(n):
    return [int(d) for d in str(n)]


digits(400)