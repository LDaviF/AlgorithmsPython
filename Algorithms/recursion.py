def countdown(n):

    # -- base case --
    if n == 0:
        return
    
    # -- recursion case --
    else:
        print(n)
        countdown(n-1)
    
countdown(10)