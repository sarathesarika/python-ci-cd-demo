def frqfun(str1):
    dict1={}
    for i in str1:
        if i in dict1:
            dict1[i]+= 1
        else:
            dict1[i]=1
    print(dict1)
str1=input("enter string to know the freq of every elemnet")
frqfun(str1)

