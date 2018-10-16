def test(a):
    if a == 5:
       print("that's the value I'm looking for!")
    elif a == 7:
       print("that's an OK number")
    else:
       print("that number won't do!")

def fact(n):
    """compute the factorial of the input value, n"""
    if n == 0:
        return 1
    else:
        return n * fact(n-1)