
# Functions of string

#1. Capitalized

cap = "python is easy and simple to learn"
print(cap.capitalize())

#2. Title: capitalize the first character of each word in the string.

tit = "python is easy and simple to learn"
print(tit.title())

#3. Upper(): convert to uppercase
upp = "python is simple"
print(upp.upper())
#4. lower(): converts the string to lower
Low_ = "PYTHON IS SIMPLE"
print(Low_.lower())

#5.swapcase(): converts uppercase to lowercase
swap_ = "PYTHON is simple and Easy"
print(swap_.swapcase())

#6. lstrip(): leftstrip : it will strip or remove whitespace from left side of the string
lstrp_ = "          chaitanya "
print(lstrp_.lstrip())
#7. rstrip(): strips of whitespace from right
rstrp = '       chaitanya       '
print(rstrp.rstrip())
print(lstrp_.lstrip().rstrip().title()) #we can also combine multiple string function in a single line of code
#8. strip() : combination of lstrip and rstrip, strips whitespaces from both sides of the string
print(rstrp.strip())
#9. replace(): replaces the words or character set from the given string
        #syntax: string_name.replace('oldWord', 'newWord', count)

stamnt = "Python developer, data analyst, data engineer, data admin"
print(stamnt.replace('d','D',2))
print(stamnt.replace('d','D'))
print(stamnt.replace('data', 'DATA'))

#10. count(): counts number of occurances a character or word is repeated in the string
        #syntax: string_name.count('char/word', start_index, end_index)
count1 = 'Data engineer, Python developer, Data analyst, Data Admin'
print(count1.count('Data'))

#11.index()
indx = 'Data engineer, Python developer, Data analyst, Data Admin'
print(indx.index("Data",4))
print(indx.count('Data'))
"""
#12. split() : splits the words or characters to given delimiter(" "whitespace by default)
job_desc = "Python,Developer/Data Analyst"
splt = job_desc.split(",")
print(splt)
splt1 = splt[1].split('/')
print(splt1)

print(splt1.insert(0,'Python'))

"""