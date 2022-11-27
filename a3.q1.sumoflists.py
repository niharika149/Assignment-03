def total():
    lst=[]
    length=int(input("Enter the length of the list: "))
    for i in range(length):
        elements=int(input("Enter element: "))
        lst.append(elements)
    print(lst)
    sum=0
    for i in lst:
        sum+=i
    print("Sum of the list is:",sum)
total()