Arrrr = [1,2,3,4,5,7,8,9]
def simpleArraySum(ar):
    total = 0
    m = len(ar)
    if ar == "" or ar == []:
        f"the input must be a list:{ar}"
    else:
        for aray in range(m):
            total = total + ar[aray]
        return total

total = simpleArraySum(Arrrr)
