import random

print(random.randrange(1, 10))

num = 2.9
int(num)
print(num)

x = int(1)
y = int(2.8)
z = int("3")

print(type(x))
print(type(y))
print(type(z))

text = "The best things in life are free!"
if "free" in text:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present")

str = 'Kazakhstan'
print(str[-4:])