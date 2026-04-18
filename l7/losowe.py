import random

amount = int(input('Ile liczb wylosować? '))
result = []

for i in range(amount):
	number = random.randint(0,10)
	if number != 5:
		result.append(number)

print(result)
print(len(result))
print(result.count(7))

if 7 in result:
	print("Na liście jest 7")
else:
	print("Na liście nie ma 7")