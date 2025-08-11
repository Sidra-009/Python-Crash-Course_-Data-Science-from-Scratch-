# %
for i in [1,2,3]:
    print(i) # print 1 
    for j in [1,2,3]:
       print(j) # print 1
       print(i+j) # print 2
    print(i) # print 1
print("Looping is Done")        

# %%
long_winded_computation = (1+4+6+9+7)
print(long_winded_computation)

# %%
#Lists 
list = [[1,3,4],[1,8,9],[83,5,0]]
list #prints list

# %%
# Easy to read list 
list = [[45,78,90],
        [34,56,78],
        [33,11,22]]
list

# %%
# Modules
import re
regex =re.compile("[-0.9]+",re.I)
regex

# %%
''' re is the module containing functions and constants for working with regular expressions. After this type of import u must prefix those
functions with re.in order to access them.'''
import re as regex 
regex = regex.compile("[0-9]+",regex.I)
regex


# %%
'''A function is a rule for taking zero or more inputs and returning a corresponding output. In Python, we typically define functions using def:'''
def Sidra(S):
    "Hey I am Sidra, a Data Science Student i created this function to return my Semesters i have done"
    return S*2   
Sidra(2)    

# %%
def full_name(first_name="Sidra",last_name="Bibi"):
    return first_name+" "+last_name
full_name("Sidra","Saqlain")
full_name("Sidra")
full_name(last_name="Saqlain")

# %%
#Strings
Name = 'sidra'
name="Sidra"
name,Name


# %%
str="/t"
st="\t"
len(st),len(str)

# %%
try: 
   print(0 / 0) 
except ZeroDivisionError: 
     print("cannot divide by zero")

# %%
#Lists
"""he most fundamental data structure in Python is the list, which is simply an ordered collection (it is similar to what in other languages 
might be called an array, but with some added functionality):"""
integer_list = [1,2,3]
homogenous_list= ["Apple", 1 , 0.9]
len(integer_list)
sum(integer_list)


# %%
x=[0,1,2,3,4,5,6,7,8,9]
print(x[0])
print(x[3])
four=x[4]
print(four)
nine=x[-1]
print(nine)
eight=x[-2]
print(eight)

# %%
#List Slicing 
x=[0,1,2,3,4,5,6,7,8,9]
print(x[2:])
print(x[:9])
print(x[1:-1])
print(x[6:9])
print(x[-3:])
print(x[:])
print(x[1:5:-1])
print(x[::3])
0 in x
77 in x

# %%
x=[1,2,3]
x.extend([4,5,6,7,9])
print(x)
"""if dont want to modify x then """
y =x + [5,7,9]
y

# %%
x,y=[1,2]
x,y
x


# %%
#Tuple
#Tuples are lists’ immutable cousins. Pretty much anything you can do to a list that doesn’t involve modifying it, you can do to a tuple. You  specify a tuple by using parentheses (or nothing) instead of square brackets:
list=[1,2,3]
tuple=(1,3)
other_tuple=3,4
list[1]=9
print(list)
try:
    tuple[1]=9
except TypeError:
    print("tuple is not mutable")

# %%
def sum_of_tuple(x,y):
    return (x+y),(x*y)
sp=sum_of_tuple(3,2)
s,p=sum_of_tuple(4,8)
print(sp)
print(s,p)


# %%
#DICTIONARY
'''a dictionary, which associates values with keys and allows you to quickly retrieve the value corresponding to a given key:'''
empty_dict={}
empty_dict2=dict()
print(empty_dict)
empty_dict2
grades={"Sidra":80, "Amna":81, "Hiba":82}
print(grades["Sidra"])
print(grades["Amna"])
try:
    grades["Kate"]
except KeyError:
    print("NO grade for Kate")
print("Sidra" in grades)
print("Kate" in grades)
Hiba=grades.get("Hiba")
Hiba


# %%
#DICTIONARY
'''a dictionary, which associates values with keys and allows you to quickly retrieve the value corresponding to a given key:'''
empty_dict={}
empty_dict2=dict()
print(empty_dict)
empty_dict2
grades={"Sidra":80, "Amna":81, "Hiba":82}
print(grades["Sidra"])
print(grades["Amna"])
try:
    grades["Kate"]
except KeyError:
    print("NO grade for Kate")
print("Sidra" in grades)
print("Kate" in grades)
Hiba=grades.get("Hiba")
Hiba
grades["Sidra"]=90
print("Updated Grades:",grades)
len(grades)

# %%
tweet={
    "user":"Sidra",
    "text":"Data Science Student",
    "tweet_counts":100,
    "hashtags":["#Practice","#Data Science","#Student","#Couroius"]
}
#print(tweet.keys())
#print(tweet.values())
#print(tweet.items())
tweet_keys   = tweet.keys()     
tweet_values = tweet.values()    
tweet_items  = tweet.items()
"user" in tweet_keys
"Sidra" in tweet_values

# %%
#DEFAULTDICT
'''If a key doesn’t exist, it automatically creates it with a default value'''
from collections import defaultdict
count=defaultdict(int)
for fruit in['apple','mango']:
    count[fruit]+=1
print(count)

# %%
from collections import defaultdict
count=defaultdict(int)
text="Sidra Saqlain"
for texts in text:
    count[text]+=1
print(count)

# %%
#COUNTERS
''' a special dictionary designed specifically to count hashable objects like strings, numbers, tuples, etc.'''



