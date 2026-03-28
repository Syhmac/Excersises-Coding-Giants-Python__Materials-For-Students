# Pobrać od użytkownika 2 liczby
# Liczba 1 to jakaś liczba naszego wyboru
# Liczba 2 jest z przedziały 0 - 100 i reprezentuje procent
# Wyliczyć % z tej liczby

# Krok 1: Pobrać dane i zamienić je na liczby całkowite


# Krok 2: r = L1 * (L2/100)

# Krok 3: Wypisać wynik na ekran

num1 = float(input('podaj liczbe: '))
num2 = float(input('podaj liczbe od 1 do 100'))
wynik = num1 * (num2/100)

print(f'wynik: {wynik}')