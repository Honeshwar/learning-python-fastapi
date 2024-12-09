# CRUD operation in string
# create and update and read and delete string
str1 = 'This is string'
str1 = str('This is string')
str1 = '''this is
sada
asdsa
asd'''#use to create multiline string
str1 = None#delete
print(str1)#read


# Note: All string methods returns new values. They do not change the original string.
str1 = "this is my String. hi there!"

# capitalize()	Converts the first character to upper case
str2 = str1.capitalize()
# print(str1,str2)
# print(str2)


# casefold()	Converts string into lower case
# Return a version of the string suitable for caseless comparisons.
'''
This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.'''

str2 = str1.casefold()

# to convert string to upper and lower case
str3 = str1.lower()
str4 = str1.upper()

# print(str2,'\n',str3,'\n',str4)



# finding occurance of substring
str5 = str1.count('is',5)

str5 = str1.encode()

str5 = str1.endswith('hi')

str5 = str1.find("is")

str5 = str1.index("is")#first match string index/position return, similar to find() but on not matching substring find() return -1 but index() raise exceptionS



# split()	Splits the string at the specified separator, and returns a list
str5 = str1.split('.')
str1 = '''dklf
sdfklm
skdmf lskdnmf
sdklfms'''
str5 = str1.splitlines()


str5 = str1.isdigit()# isdecimal,isnumeric, islower
print(str5)