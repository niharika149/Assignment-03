def reverse_string(str):
    str1=''
    for i in str:
        str1=i+str1
    return str1
str2=input("Enter the string: ")
if __name__=='__main__':
    print("Reverse of a string is: ",reverse_string(str2))

