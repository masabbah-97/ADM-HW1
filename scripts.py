
#Say "Hello, World!" With Python

print("Hello, World!")

#Python If-Else

n = int(input().strip())
if n % 2!=0:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print ('Not Weird')
elif n % 2 ==0 and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')


#Arithmetic Operators

a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

#Python: Division

a = int(input())
b = int(input())
print(a//b)
print(a/b)

#Loops

n=int(input())
for i in range(n):
    print (i*i)



#Write a function

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    
    return leap

year = int(input())
print(is_leap(year))


#Print Function
n = int(input())
output=''

for i in range(1,n+1):
    output=output+str(i)
print(output)



#Find the Runner-Up Score! 

n = int(input())
arr = map(int, input().split())
ls=list(arr)
m=max(ls)
revls=sorted(ls, reverse = True)
for i in revls:
    if i<m:
        runnerUp=i
        break
print(runnerUp)

#Nested List
x=[]
n=int(input())
scores=[]
names = []
for i in range(n):
    name=str(input())
    score=float(input())
    x.append([name,score])
    scores.append(score)

sortScores = sorted(scores)
sortScores = list(dict.fromkeys(sortScores))
secondLowest = sortScores[1]

for j in x:
    if j[1] == secondLowest:
        names.append(j[0])
sortedNames = sorted(names)
for k in sortedNames:
    print (k)

#Finding the percentage

n = int (input ())
studentMarks = {}
for i in range (n):
    studentList = input().split()
    studentMarks[studentList[0]] = list(map(float , studentList[1:]))
chosenStudent = input()
print ("{:.2f}".format(sum(studentMarks[chosenStudent])/3.0))

#Lists

ls = []
N = int(input())
for i in range (N):
    command = input().split()
    if command[0] == 'append':
        ls.append (int(command[1]))
    elif command[0] == 'print':
        print(ls)
    elif command[0] == 'insert':
        ls.insert(int(command[1]),int((command[2])))
    elif command[0] == 'remove':
        ls.remove(int(command[1]))
    elif command[0] == 'sort':
        ls=sorted(ls)
    elif command[0] == 'pop':
        ls.pop()
    elif command[0] == 'reverse':
        ls.reverse()

#List Comprehensions

x = int(input())
y = int(input())
z = int(input())
newLst=[]
sumOfVals=0
permList=[]
n = int(input())
for i in range(x+1):
    for j in range (y+1):
        for k in range (z+1):
            sumOfVals=i+j+k
            if sumOfVals !=n:
                newLst = [i,j,k]
                permList.append(newLst)
print(permList)

#Tuples

n = int(input())
integer_list = map(int, input().split())
tupleHash = hash(tuple(integer_list))
print (tupleHash)


#sWAP cASE

def swap_case(s):
    newLst=list(s)
    output=""
    for i in newLst:
        if i.isupper() == True:
            output += i.lower()
        elif i.islower() == True:
            output += i.upper()
        else:
            output += i
        
    return output



s = input()
result = swap_case(s)
print(result)

#String Split and Join

def split_and_join(line):
    lineSplited = line.split()
    lineJoined = "-".join(lineSplited)
    return lineJoined

line = input()
result = split_and_join(line)
print(result)

#What's Your Name?

def print_full_name(first, last):
    finalString = "Hello " + first + " " + last + "! You just delved into python."
    print(finalString)

first_name = input()
last_name = input()
print_full_name(first_name, last_name)

#Mutations

def mutate_string(string, position, character):
    strLst = list(string)
    strLst[position] = character
    string = ''.join(strLst)
    return string
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

#Find a String

def count_substring(string, sub_string):
    count = 0
    for i in range (len(string)):
        if sub_string == string [i:i+len(sub_string)]:
            count +=1
    return count
string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)

#String validators

from curses.ascii import isalnum, isalpha
alphaNumBool = False
alphaBool = False
digitBool = False
lowerBool = False
upperBool = False
s = input()
strLst=list(s)

for i in strLst:
    if i.isalnum() == True:
        alphaNumBool = True
        break

for i in strLst:
    if i.isalpha() == True:
        alphaBool = True
        break

for i in strLst:
    if i.isdigit() == True:
        digitBool = True
        break
for i in strLst:
    if i.islower() == True:
        lowerBool = True
        break

for i in strLst:
    if i.isupper() == True:
        upperBool = True
        break

print (alphaNumBool)
print(alphaBool)
print(digitBool)
print(lowerBool)
print(upperBool)
                
#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap

def wrap(string, max_width):
    newString=""
    for i in range (0,len(string),max_width ):
        newString += string[i:i+max_width]+"\n"
    return newString

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

#Designer Door Mat  

firstPattern = '-'
secondPattern = '.|.'
welcomeMessage = 'WELCOME'
length, width = map(int, input().split())

for i in range (1 , length , 2):
    print((i*secondPattern).center(width,firstPattern))
print (welcomeMessage.center(width,firstPattern))

for i in range (length -2  , 0 , -2):
    print((i*secondPattern).center(width,firstPattern))


#String Formatting

def print_formatted(number):
    # your code goes here
    spacePadding = len(bin(number).replace('0b','')) 
    for i in range(1 , number+1):
        print (str(i).rjust(spacePadding) + ' ' +(oct(i).replace('0o',''))  .rjust(spacePadding) + ' '+(hex(i).replace('0x','').upper()).rjust(spacePadding) + ' ' + (bin(i).replace('0b','').rjust(spacePadding)))
    return number
n = int(input())
print_formatted(n)

#Alphabet Ragnoli

import string
def print_rangoli(n):
    alphabet = list(string.ascii_lowercase)
    finalString=''
    middleLine = '-'.join(alphabet[n-1::-1] + alphabet[1:n])
    width = len(middleLine)
    for i in range (n,1,-1):
        finalString+= '-'.join(alphabet[n-1:i-1:-1]+alphabet[i-1:n]).center(width,'-')+'\n'

    for i in range (1,n+1):
        finalString+='-'.join(alphabet[n-1:i-1:-1]+alphabet[i-1:n]).center(width,'-')+'\n'
    print(finalString) 
n = int(input())
print_rangoli(n)


#Capitalize
import os
def solve(s):
    fullNameLst = list(s)
    fullNameLst[0] = fullNameLst[0].capitalize()
    for i in range(len(fullNameLst)):
        if fullNameLst[i] == " ":
            fullNameLst[i+1] = fullNameLst[i+1].capitalize()
    fullName = ''.join(fullNameLst)
    return fullName

fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = solve(s)

fptr.write(result + '\n')

fptr.close()


#The Minion Game
def minion_game(string):
    vowels = 'AEIOU'
    kevinScore = 0
    stuartScore = 0
    for i in range (len (string)):
        if string [i] in vowels:
            kevinScore+=len(string[i:])
        else:
            stuartScore+=len(string[i:])
    if kevinScore > stuartScore:
        print ('Kevin',kevinScore)
    elif stuartScore > kevinScore:
        print('Stuart',stuartScore)
    else:
        print('Draw')
s = input()
minion_game(s)

#Merge the Tools!

def merge_the_tools(string , k):

    for i in range (0,len(string),k):
        finalString=''
        subString=string[i:i+k]
        finalString += string[i]
        for j in subString:
            if j not in finalString:
                finalString += j
        print(finalString)
    return
string, k = input(), int(input())
merge_the_tools(string, k)

#Introduction to Sets

import statistics
def average (array):
    st = set(array)
    avg = statistics.mean(st)
    return avg
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)


#No Idea!

m, n = map(int, input().split(' '))
elements = list(map(int, input().split(' ')))
A = set(map(int, input().split(' ')))
B = set(map(int, input().split(' ')))
happiness = 0

for i in elements:
    if i in A:
        happiness += 1
    
    if i in B:
        happiness -= 1
print(happiness)

#Symmetric Difference
m = int(input())
A = set(map(int, input().split(' ')))
n = int(input())
B = set(map(int, input().split(' ')))
finalLst = []
for i in A:
    if i not in B:
        finalLst.append(i)
for j in B:
    if j not in A:
        finalLst.append(j)
finalLst = sorted(finalLst)
for k in finalLst:
    print(k)

#Set.add()
n = int(input())
countries = set()
counter = 0
for i in range(n):
    countries.add(input())
for j in countries:
    counter +=1
print(counter)

#Set .discard(), .remove() & .pop()


n = int(input())
s = set(map(int, input().split()))
commandNumber = int(input())

for i in range(commandNumber):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    elif command[0] == 'remove':
        s.remove(int(command[1]))
print (sum(s))

#Set .union() Operation

n = int(input())
nSet = set(map(int, input().split()))
b = int(input())
bSet= set(map(int, input().split()))
union = nSet.union(bSet)
counter = 0
for i in union:
    counter +=1
print (counter)

#Set .intersection() Operation

n = int(input())
nSet = set(map(int, input().split()))
b = int(input())
bSet= set(map(int, input().split()))
intersection = nSet.intersection(bSet)
counter = 0
for i in intersection:
    counter += 1
print(counter)

#Set .differnce() Operation
n = int(input())
nSet = set(map(int, input().split()))
b = int(input())
bSet= set(map(int, input().split()))
difference = nSet.difference(bSet)
counter = 0
for i in difference:
    counter += 1
print(counter)

#Set .symmetric_difference() Operation

n = int(input())
nSet = set(map(int, input().split()))
b = int(input())
bSet= set(map(int, input().split()))
symDifference = nSet.symmetric_difference(bSet)
counter = 0
for i in symDifference:
    counter += 1
print(counter)

#Set Mutations

n = int(input())
s = set(map(int, input().split()))
commandNumber = int(input())

for i in range(commandNumber):
    command = input().split()
    if command[0] == 'intersection_update':
        a = set(map(int, input().split()))
        s.intersection_update(a)
    elif command[0] == 'symmetric_difference_update':
        a = set(map(int, input().split()))
        s.symmetric_difference_update(a)
    elif command[0] == 'update':
        a = set(map(int, input().split()))
        s.update(a)
    elif command[0] == 'difference_update':
        a = set(map(int, input().split()))
        s.difference_update(a)
print (sum(s))

#The Captain's Room
k = int(input())
roomLst = list(map(int, input().split()))
captainSet = set()
roomSet = set()
for i in roomLst:
    if i not in roomSet:
        captainSet.add(i)
        roomSet.add(i)
    else:
        captainSet.discard(i)
for j in captainSet:
    print(j)

#Check Subset

t = int(input())
for i in range (t):
    aNum = int(input())
    a = set(map(int, input().split()))
    bNum = int(input())
    b = set(map(int, input().split()))
    print (a.issubset(b))

#Check Strict Superset

setA = set(map(int, input().split()))
n = int(input())
counter = 0

for i in range(n):
    setB=set(map(int, input().split()))
    if (setB.issubset(setA) and setA.issuperset(setB) and setA != setB) == False:
        counter += 1
if counter == 0:
    print(True)
else:
    print(False)


#collections.Counter()

x = int(input())
shoeSizes = list(map(int, input().split()))
n = int(input())
moneyMade = []
counter = 0
for i in range(n):
    order = input().split()
    if int(order[0]) in shoeSizes:
        counter += int(order[1])
        shoeSizes.remove(int(order[0]))
print (counter)

#DefaultDict Tutorial

from collections import defaultdict
a = defaultdict(list)
b = []
n, m = map(int, input().split(' '))
for i in range (n):
    a[input()].append(i+1)

for j in range(m):
    b.append(input())

for k in b:
    if k in a.keys():
        print(" ".join(map(str,a[k])))
    else:
        print('-1')

#Collections.namedtuple()
from collections import namedtuple
n = int(input())
totalGrade = 0
tupleName = list(input().split(' '))
namesLst=[]
for i in tupleName:
    if i !='':
        namesLst.append(i)
for i in range(len(tupleName)):
    if namesLst[i]== 'MARKS':
        index = i
        break


students = namedtuple('Student', 'ID MARKS NAME CLASS')

for i in range(n):
    lst = list(input().split())
    student=students(lst[0],lst[index],lst[2],lst[3])
    totalGrade +=int(student.MARKS)
avg = totalGrade/float(n)
print("%.2f" %avg)


#Collections.OrderedDict()

from collections import OrderedDict
n = int(input())
ordered_dictionary = OrderedDict()
for i in range(n):
    item = input().split()
    itemName = " ".join(item[:-1])
    itemPrice = int(item[-1])
    if itemName in ordered_dictionary:
        ordered_dictionary[itemName] = (ordered_dictionary[itemName] + itemPrice)
    else:
        ordered_dictionary[itemName] = itemPrice

for i in ordered_dictionary:
    print (i + ' ' + str(ordered_dictionary[i]))


#Word Order
from collections import OrderedDict
n = int(input())
ordered_dictionary = OrderedDict()
words = 0
occLst=[]
for i in range (n):
    word = input()
    if word in ordered_dictionary:
        ordered_dictionary[word] += 1
    else:
        ordered_dictionary[word] = 1
for j in ordered_dictionary:
    words +=1
    occLst.append(str(ordered_dictionary[j]))
print (words)
print (" ".join(occLst))

#Collections.deque()

from collections import deque
n = int(input())
d = deque()
for i in range(n):
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
print (' '.join(d))


#Company Logo

from collections import Counter
s = sorted(input().strip())
counter = Counter(s).most_common()
top3 = counter[0:3]
for i in top3:
    print (i[0]+" "+str(i[1]))

#Piling up

t = int(input())
for i in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))
    if blocks[0] == max(blocks) or blocks[-1] == max(blocks):
        print('Yes')
    else:
        print('No')

#Calendar Module

import calendar
MM, DD, YYYY = map(int,input().split())
dayIndex = calendar.weekday(YYYY,MM,DD)
day = calendar.day_name[dayIndex].upper()
print (day)


#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    tz_1 = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    tz_2 = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    diff = abs(tz_2-tz_1)
    res = diff.total_seconds()
    return str(int(res))
    


fptr = open(os.environ['OUTPUT_PATH'], 'w')

t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    fptr.write(delta + '\n')

fptr.close()


#Exceptions
t = int(input())
for i in range(t):
    try:
        a, b = map(int, input().split(' '))
        print(a//b)
    except(ZeroDivisionError,ValueError) as e:
        print ("Error Code:",e)


#Zipped!
a, b = map(int, input().split(' '))
grades = []
for j in range (b):
    grades.append(list(map(float,input().split(' '))))
z = tuple(zip(*grades))
for i in z:
    print(sum(i)/b)

#Athlete Sort 
from operator import itemgetter
n, m = map(int, input().split(' '))
lst = []
for i in range(n):
    athlete = list(map(int, input().split()))
    lst.append(athlete)
k = itemgetter(int(input()))
finalList = sorted(lst , key =k )
for i in range(len(finalList)):
    finalList[i]=map(str,finalList[i])
for j in finalList:
    print(" ".join(j))

#ginorts

from curses.ascii import isdigit, islower, isupper
s = input()
upper = []
lower = []
even = []
odd = []
for i in s:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i) 
    elif i.isdigit():
        if int(i)%2 == 0:
            even.append(i)
        else:
            odd.append(i)
upper = "".join(sorted(upper))
lower = "".join(sorted(lower))
even = "".join(sorted(even))
odd = "".join(sorted(odd))
ginorts = lower+upper+odd+even
print(ginorts)


#Map and Lambda Function
cube = lambda x:x**3
def fibonacci(n):
    fibList =[]
    firstTerm = 0
    secondTerm = 1
    count = 0
    if n ==1:
        fibList.append(firstTerm)
    else:
        while count < n:
            nthTerm = firstTerm +secondTerm
            fibList.append(firstTerm)
            firstTerm = secondTerm
            secondTerm = nthTerm
            count += 1
    return(fibList)
n = int(input())
print(list(map(cube, fibonacci(n))))


#Detect Floating Point Number
import re 
n = int(input())
for i in range(n):
    t = input()

    value = False
    if t !='0':

        value = bool(re.search(r".",t))
        if value == True:
            try:
                float(t)
            except Exception as e:
                value=False
    else:
        value = False

    print(value)
     
#Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group() Groups() Groupdict()
import re 
s = input()
m = re.search(r"([a-zA-Z0-9])\1",s)
if m:
    match = m.group(1)
    print(match)
else:
    print(-1)
#Re.findall() & Re.finditer()
import re 
s = input()
regLst = re.findall(r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])',s,re.IGNORECASE)
if regLst:
    for i in regLst:
        print(i)
else:
    print(-1)

#Re.start() & Re.end()
import re
s = input()
k = re.compile(input())
m = k.search(s)
if m :
    while m:
        print((m.start(),m.end()-1))
        m=k.search(s,m.start()+1)
else:
    print((-1,-1))
#Regex Substitution
import re
def change(match):
    string = str(match.group(0))
    if string == " && ":
        change = " and "
    elif string == " || ":
        change = " or "
    return change

n =int(input())
for i in range (n):
    line = re.sub(r'\ \|\|\ ',change, input())
    output = re.sub(r'\ \&\&\ ',change, line) 
    output = re.sub(r'\ \|\|\ ',change, output) 
    output = re.sub(r'\ \&\&\ ',change, output)    
    print(output)

# Validating Roman Numerals

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers

import re
n = int(input())
for i in range(n):
    number = input()
    found = bool(re.match(r"^[789]\d{9}$",number))
    if found == True:
        print('YES')
    else:
        print('NO')

#Validating and Parsin Email Addresses
import re
n = int(input())

for i in range (n):
    email = input()
    emailLst = email.split(' ')
    firstName = emailLst[0]
    address = emailLst[1]
    isEmail = bool(re.match(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>",address))
    if isEmail:
         print(firstName,address)

#Hex Color Code
import re
n = int(input())
s = ""
css = False
for i in range(n):
    line = input()
    if '{' in line:
        css = True
    elif '}' in line:
        css = False
    if css == True:
        if '{' not in  line :
            s+=line
    
m = re.findall(r'#[a-fA-F0-9]{3,6}',s)
for i in m:
    print (i)

#HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :",tag)
        if attrs:
            for i in attrs:
                attribute = '-> ' + i[0] + ' > '+str(i[1])
                print(attribute)
    def handle_endtag(self, tag):
        print ("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :",tag)
        if attrs:
            for i in attrs:
                attribute = '-> ' + i[0] + ' > '+str(i[1])
                print(attribute)
        
n = int(input())
parser = MyHTMLParser()

for i in range(n):
    line = input()
    parser.feed(line)

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        dataLen = len(data.split('\n'))
        if data !='\n':
            if dataLen > 1:
                print ('>>> Multi-line Comment \n'+data)
            else :
                print('>>> Single-line Comment \n' +data)
    def handle_data(self, data: str):
        if data.strip():
            print('>>> Data \n'+data)
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        dataLen = len(data.split('\n'))
        if data !='\n':
            if dataLen > 1:
                print ('>>>Multi-line Comment \n'+data)
            else :
                print('>>> Single-line Comment \n' +data)
    def handle_data(self, data: str):
        print('>>>Data \n'+data)

#Validating UID
from collections import defaultdict
import re
t = int(input())
for i in range(t):
    repitition = False
    a = defaultdict(int)
    s = input().strip()
    for j in s:
        a[j] +=1
    for k in a.values():
        if k >1:
            repitition = True
            break
        else :
            repitition = False
    if repitition == True:
        print('Invalid')
    else:
        if  bool(re.search(r'(.*[A-Z]){2,}', s)) == True and bool(re.search(r'[a-zA-Z0-9]',s)) ==True and bool(re.search(r'(.*[0-9]){3,}',s))== True and len(s)==10 and s.isalnum()==True:
            if re.search(r'.*(.).*\1+.*',s):
                print('Invalid')
            else:
                print('Valid')
        else:
           print ('Invalid')

#Validating Credit Card Numbers

import re

n = int(input())

for i in range (n):
    s = input().strip()
    if s.len == 16 and bool(re.match(r"^[4-6]\d{16}$",n)):
        print('Valid')
    else :
        print('Invalid')

#Validating Postal Codes
import re
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"	# Do not delete 'r'.
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix


#XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = 0
    count += len(node.attrib)
    for i in node:
        count+= get_attr_number(i)
    return count
    # your code goes here

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))



#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            s = l[i]
            l[i] = '+91 ' + s[-10:-5] +' ' + s[-5:]
        f(l)
        
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#Decorators 2 - Name Directory

import operator
def person_lister(f):
    def inner(people):
        for i in range(len(people)):
            people[i][2] = int(people[i][2])
        srtPeople = sorted (people,key = operator.itemgetter(2))
        ppl = map(f,srtPeople)
        return ppl
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


#Arrays

import numpy

def arrays(arr):
    arr = list(map(float,arr))
    arr.reverse()
    arr = numpy.array(arr,float)
    return arr
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape

import numpy

lst = list(map(int, input().split()))
print (numpy.reshape(lst,(3,3)))

#Transpose and Flatten

import numpy
n , m = map( int, input().split())
lst = []
for i in range (n):
    lst.append(list(map(int,input().split())))
arr = numpy.array(lst)
print(arr.transpose())
print(arr.flatten())

#Concatenate

import numpy
n , m, p = map( int, input().split())
nLst = []
mLst = []
for i in range(n):
    nLst.append(list(map(int,input().split())))
for j in range(m):
    mLst.append(list(map(int,input().split())))
nArr = numpy.array(nLst)
mArr = numpy.array(mLst)
print(numpy.concatenate((nArr,mArr),axis = 0))


#Zeros and Ones

import numpy
tpl = tuple(map(int,input().split()))
print(numpy.zeros(tpl, dtype = int))
print(numpy.ones(tpl, dtype = int))

#Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')
n , m = map( int, input().split())
print(numpy.eye(n,m))

#Array Mathematics

import numpy
n , m = map( int, input().split())
aLst = [] 
bLst = [] 

for i in range (n):
    aLst.append(list(map(int,input().split())))
for j in range (n):
    bLst.append(list(map(int,input().split())))
    
a = numpy.array(aLst , dtype=int)
b = numpy.array(bLst , dtype=int)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print (a % b)
print (a ** b)

#Floor, Ceil, Rint

import numpy
numpy.set_printoptions(legacy='1.13')
lst = list(map( float , input().split()))
arr = numpy.array(lst)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

#Sum and Prod

import numpy
n , m = map( int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
arr = numpy.array(lst)
arrSum = numpy.sum(arr, axis=0)
print(numpy.prod(arrSum))

#Min and Max

import numpy
n , m = map( int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
arr = numpy.array(lst)
minimum = numpy.min(arr, axis = 1)
print(numpy.max(minimum))

#Mean, Var, and Std

import numpy
n , m = map( int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
arr = numpy.array(lst)
print (numpy.mean(arr,axis = 1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr),11))

#Dot and Cross

import numpy
n = int(input())
aLst=[]
bLst=[]
for i in range (n):
    aLst.append(list(map(int,input().split())))
for j in range (n):
    bLst.append(list(map(int,input().split())))
a = numpy.array(aLst , dtype=int)
b = numpy.array(bLst , dtype=int)
print(numpy.dot(a,b))

#Inner and Outer 

import numpy
aLst=list(map(int,input().split()))
bLst=list(map(int,input().split()))
a = numpy.array(aLst , dtype=int)
b = numpy.array(bLst , dtype=int)
print(numpy.inner(a,b))
print(numpy.outer(a,b))

#Polynomials

import numpy
lst=list(map(float,input().split()))
print(numpy.polyval(lst,float(input())))

#Linear Algebra

import numpy
n = int(input())
lst = []
for i in range (n):
    lst.append(list(map(float,input().split())))
arr= numpy.array(lst , dtype=float)
print (round(numpy.linalg.det(arr),2))


#Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    maxH = max(candles)
    count = 0
    for i in candles:
        if i == maxH:
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    diff = x2 - x1
    rateDiff = v1 - v2
    if v1 > v2 and  diff % rateDiff == 0:
        return 'YES'
    else:
        return 'NO'
        
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    prevDay = math.floor(5/2)
    cummulative = prevDay
    for _ in range(1,n):
        day = math.floor((prevDay*3)/2)
        cummulative += day
        prevDay = day
    return cummulative
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def super_digit(n):
    
    sum = 0
    for i in n:
        sum += int(i)
    return rec(str(sum))

def rec(num):
    if len(num) > 1:
        num = super_digit(num)
    return num
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]

    k = int(first_multiple_input[1])
    num = n*k
    result = rec(num)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1


def insertionSort1(n, arr):
    found = False
    last = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] > last:
            arr[i+1] = arr[i]
        elif arr[i] < last:
            arr[i+1] = last
            found = True
        strArr = list(map(str,arr))
        print(" ".join(strArr))
        if i == 0 and found == False:
            arr[0] = last
            strArr = list(map(str,arr))
            print(" ".join(strArr))
        
        if found == True:
            break


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

insertionSort1(n, arr)

#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    found = False
    last = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] > last:
            arr[i+1] = arr[i]
        elif arr[i] < last:
            arr[i+1] = last
            found = True
        #strArr = list(map(str,arr))
        #print(" ".join(strArr))
        if i == 0 and found == False:
            arr[0] = last
            #strArr = list(map(str,arr))
            #print(" ".join(strArr))
        
        if found == True:
            break
    return arr




def insertionSort2(n, arr):
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            strArr = list(map(str,arr))
            jn =" ".join(strArr) 
            if jn != None:
                print(jn)
        elif arr[i] < arr[i-1]:
            tmpArr=insertionSort1(i+1,arr[:i+1])
            arr[:i+1]=tmpArr
            strArr = list(map(str,arr))
            jn =" ".join(strArr) 
            if jn != None:
                print(jn)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
