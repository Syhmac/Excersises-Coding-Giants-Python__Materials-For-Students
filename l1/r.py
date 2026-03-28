import random

r1 = random.randint(1, 100) # 100 może być wylosowane
r2 = random.randrange(1, 100) # 100 nie może być wylosowane (1 - 99)
r3 = random.random() # 0 - 1 liczba z przecinkiem

print(r1)
print(r2)
print(r3)