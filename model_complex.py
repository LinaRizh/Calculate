x = 0
y = 0
z = ''
def chisla(a,b,c):
    global x
    global y
    global z
    x = complex(a)
    y = complex(b)
    z = c

def operation(x, y, s):
     if s == '+':
         return x+y 
     elif s == '*':
         return x*y
     elif s == '/':
         return x/y
     elif s == '-':
         return x-y
     elif s == '**':
         return x**y
     elif s == '//':
         return x//y