
def fibonacciFunction(m):
    m = int(m)
    if(m>1):
        return fibonacciFunction(m-1) + fibonacciFunction(m-2)
    else:
        if (m==1):
            return 1
        else:
            if (m==0):
                return 0

