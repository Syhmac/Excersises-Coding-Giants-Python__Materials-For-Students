number = 33 # int
text = 'Tekst w którym znajduje się coś w "cudzysłowie"' # string1
text2 = "Sample " + str(number)

print(text2)

num1 = 2
num2 = num1 + 7
text3 = str(num2) + " lives" # tekst + tekst działa, numer + text nie działa

print(type(num1)) # int

num1 = num1 + 0.5

print(type(num1)) # float

num1 = str(num1)

print(type(num1)) # string

text5 = '50'

num5 = int(text5)

print(num5) # num5 jest typu int