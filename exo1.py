a = int(input("entre un nombre de a "))
b = int(input("entre un nombre de b "))
c = int(input("entre un nombre de  c "))

# définir et initialiser le maximum à zero
max = 0
if(a > b):
    max = a
else:
    max = b
if(max < c):
    max = c
else:
    max = max
print("Le maximum des trois nombre est : max(a,b,c) = ", max)

