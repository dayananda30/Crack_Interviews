string1 = "this is a example string for learning python inbuilt string capability for"


print(35*'#')
print("Demonstrating Capatilize() Method --->  It capitalizes the first character of the String")
print(35*'#')
print("'{}'                         is the string before calling capatilize() Method".format(string1))
print("'{}'                         is the string before calling capatilize() Method".format(string1.capitalize()))
print(150*'*')



print(35*'#')
print("Demonstrating Count() Method ----> It Counts number of times substring occurs in a String between begin and end index.")
print(35*'#')
print("'{}'   is the count ".format(string1.count('for')))
print(150*'*')




print(35*'#')
print("Demonstrating endswith(suffix ,begin=0,end=n)  ---->	It returns a Boolean value if the string terminates with given suffix between begin and end.")
print(35*'#')
print("'{}'   is the count ".format(string1.endswith('for')))
print(150*'*')



print(35*'#')
print("Demonstrating find(substring ,beginIndex, endIndex)	It returns the index value of the string where substring is found between begin index and end index.")
print(35*'#')
print("'{}'   is the place where substring is present ".format(string1.find('python')))
print(150*'*')



print(35*'#')
print("Demonstrating index(subsring, beginIndex, endIndex)	It throws an exception if string is not found and works same as find() method.")
print(35*'#')
print("'{}'   is the index ".format(string1.index('python')))
print(150*'*')



print(35*'#')
print("Demonstrating isalnum()	It returns True if characters in the string are alphanumeric i.e., alphabets or numbers and there is at least 1 character. Otherwise it returns False.")
print(35*'#')
print("'{}'  ".format(string1.isalnum()))
print(150*'*')




print(35*'#')
print("Demonstrating isalpha()     It returns True when all the characters are alphabets and there is at least one character, otherwise False.")
print("'{}'  ".format(string1.isalpha()))
print(35*'#')
print("Demonstrating  isdigit()	   It returns True if all the characters are digit and there is at least one character, otherwise False..")
print("'{}'  ".format(string1.isdigit()))
print(35*'#')
print("Demonstrating islower()	   It returns True if the characters of a string are in lower case, otherwise False.")
print("'{}'  ".format(string1.islower()))
print(35*'#')
print("Demonstrating isupper()	   It returns False if characters of a string are in Upper case, otherwise False.")
print("'{}'  ".format(string1.isupper()))
print(35*'#')
print("Demonstrating isspace()	   It returns True if the characters of a string are whitespace, otherwise false.")
print("'{}'  ".format(string1.isupper()))
print(150*'*')






print(35*'#')
print("Demonstrating lower()	 It converts all the characters of a string to Lower case.")
print(35*'#')
print("'{}'                         is the string before calling lower() Method".format(string1))
print("'{}'                         is the string before calling lower() Method".format(string1.lower()))
print(150*'*')



print(35*'#')
print("Demonstrating upper()	It converts all the characters of a string to Upper Case..")
print(35*'#')
print("'{}'                         is the string before calling upper() Method".format(string1))
print("'{}'                         is the string before calling upper() Method".format(string1.upper()))
print(150*'*')




print(35*'#')
print("Demonstrating startswith(str ,begin=0,end=n)	It returns a Boolean value if the string starts with given str between begin and end.")
print(35*'#')
print("'{}'   is the count ".format(string1.startswith('for')))
print(150*'*')



print(35*'#')
print("Demonstrating swapcase()	     It inverts case of all characters in a string.")
print(35*'#')
print("'{}'                         is the string before calling swapcase() Method".format(string1))
print("'{}'                         is the string before calling swapcase() Method".format(string1.swapcase()))
print(150*'*')



print(35*'#')
print("Demonstrating lstrip()   It removes all leading whitespace of a string and can also be used to remove particular character from leading.")
print("Demonstrating rstrip()   It removes all trailing whitespace of a string and can also be used to remove particular character from trailing.")
print(35*'#')
print("'{}'   is the string before lstrip('this') ".format(string1))
print("'{}' is the string after lstrip('this') ".format(string1.lstrip('this')))
print("'{}'   is the string before rstrip('for') ".format(string1))
print("'{}' is the string after rstrip('for')".format(string1.rsplit('for')))
print(150*'*')









