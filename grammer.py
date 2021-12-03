# print(type(10))
# print(type([1.2, 2, "sss"]))
# print(type("aaa"))
# print(type('a'))
# print(type(False))

# c 4bite アドレス　メモリ番地　連続で保存 1000, 1004, 1008,...
# python メモリ番地→16進数　1000, 20023,  424, 

# x = 10
# print(x)
# x=100
# print(x)
# y=3.14
# print(x*y)
# print(type(x*y))

# a = [1,2,3,4,5]
# print(a)
# len(a)
# print(a[0])
# print(a[4])
# a[4] = 99
# print(a)

# print(a[0:2])
# print(a[1:]) # = a[1:len(a)]
# print(a[1:99])
# print(a[:3]) # = a[0:3]
# print(a[:-1])
# print(a[:-2])

# me = {'height':180}
# print(me['height'])
# me['weight'] = 70

# print(me)
# print(type(me))

# hungry = True
# sleepy = False
# print(type(hungry))
# print(not hungry)
# print(hungry or sleepy)
# print(hungry and sleepy)

hungry = False
sleepy = True

if hungry:
    print("I'm hungry.")
elif sleepy:
    print("I'm sleepy.")
else:
    print("I'm satisfied!!")

for i in [1, 2, 3]:
  print(i)

for i in [True, False, True]:
  if i:
    print("success!!")
  else:
    print("failured...")


def hello():
    print("hello!")
    
hello()  

def Hello(x):
    print("Hello" + x + "!")
    
Hello("3")   

class Human:
    # constructor
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def hello(self):
        print("Hello " + self.name + "!")

man1 = Human("matsumoto", 22)
print(man1.age)
print(type(man1))
man1.hello()

# print(2.3.is_integer())

# class Float:
#     def is_integer():
#         return False

# class Int:
#     def is_integer():
#         return True 


import numpy as np

x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)


# print(x/2.0)


A = np.array([[1,2],[3,4]])
# print(A)
# print(A.shape)
# print(A.dtype)

B = np.array([[3,0],[0,6]])
# print(A + B)
# print(A * B)
# print(A * 10)

C = np.array([10,20]) # => [[10, 20], [10, 20]]
10 # => [[10,10], [10, 10]]
print(A*C)

X = np.array([[51,55],[14,19],[0,4]])
print(X)

print(X[0])

for row in X:
    print(row)
X = X.flatten()
print(X)
print(X[np.array([0,2,4])])    
print(X[np.array([1,2,3])])

print(X>15)
print(X[X>15])
print(X[np.array([True, True, False, True, False, True])])
