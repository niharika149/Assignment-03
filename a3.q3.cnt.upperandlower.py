def count():
    str1=input("Enter the string: ")
    upper_count=0
    lower_count=0
    for i in str1:
        if i>='a' and i<='z':
            lower_count+=1
        if i>='A' and i<='Z':
            upper_count+=1
    print("No.of upper case characters are:",upper_count)
    print("No.of lower case characters are:",lower_count)
count()
        
