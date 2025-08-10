x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

x = 5
print(complex(x))

x = True
print(type(x))

print(str(35.82))

x = 'Welcome'
print(x[3:5])

txt = " Hello World "
x = txt.strip()


y = 3.14159
print(5 > 3)

print(bool("abc"))
print(bool(0))

x = 5
x += 3
print(x)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

[print(x) for x in ['apple', 'banana', 'cherry']]