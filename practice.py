def list(a):

    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b


a=[2,4,2,5,7,8,8,5,7,3,9]
print(list(a))
