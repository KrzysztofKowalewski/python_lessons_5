def zad1():
    """
    Funkcja pobiera z klawiatury nazwę użytkownika i hasło do rejestracji
    Jeśli hasło spełnia wszystkie warunki(dłuższe niż 4 i krótsze niż 8, jedna mała i duża litera i jeden znak)
    To wtedy wyświetla komunikat o pomyślnej rejestracji, w innym wypadku, 
  
    Args:
        Brak, użytkownik wprowadza parametry z klawiatury
    
    Returns:
        Wynikiem jest hasło, które funkcja zapisuje do pliku tekstowego o nazwie wynik_zad1.txt
    
    """
    username = input("Wprowadź nazwę użytkownika: ")
    password = input("Wprowadź hasło: ")
    smol_letter = False
    big_letter = False
    digit = False
    if len(password) < 4:
        print("Twoje hasło jest za krótkie!")
        exit()
    if len(password) > 8:
        print("Twoje hasło jest za długie!")
        exit()
    for element in password:
        if smol_letter == False:
            if element.islower():
                smol_letter = True
                continue
        if big_letter == False:
            if element.isupper():
                big_letter = True
                continue
        if digit == False:
            if element.isdigit():
                digit = True
                continue
    if smol_letter == True and big_letter == True and digit == True:
        print("Witamy na stronie, hasło zostało przyjęte!")
        f1 = open("wynik_zad1.txt", 'w')
        f1.write("Nazwa uzytkownika: " + username)
        f1.write("\n")
        f1.write("Haslo: " + password)
        f1.close()
    elif smol_letter == False:
        print("Twoje hasło nie ma małej litery!")
    elif big_letter == False:
        print("Twoje hasło nie ma dużej litery!")
    elif digit == False:
        print("Twoje hasło nie ma cyfry!")
    


#zad1()



import pickle

def znajdz_podzielne(x, y):
    """
    Funkcja znajduje wszystkie liczby w zakresie od x do y (włącznie),
    które są podzielne przez 7, ale nie są wielokrotnościami 5.

    Args:
    x (int): Dolna granica zakresu włącznie.
    y (int): Górna granica zakresu włącznie.

    Returns:
    list: Lista liczb spełniających warunek.
    """
    wyniki = []
    try:
        for liczba in range(x, y + 1):
            if liczba % 7 == 0 and liczba % 5 != 0:
                wyniki.append(liczba)
    except TypeError:
        print("Błędne argumenty. Upewnij się, że x i y są liczbami całkowitymi.")
    return wyniki

def zapisz_do_pliku(lista, nazwa_pliku):
    """
    Funkcja zapisuje listę do pliku w formacie .pkl.

    Args:
    lista (list): Lista do zapisania.
    nazwa_pliku (str): Nazwa pliku (z rozszerzeniem .pkl).
    """
    try:
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(lista, plik)
        print(f"Wyniki zostały zapisane do pliku {nazwa_pliku}.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")

# Testowanie funkcji
# x = 1000
# y = 2101

# wyniki = znajdz_podzielne(x, y)
# print("Znalezione liczby:", wyniki)

# nazwa_pliku = "wyniki.pkl"
# zapisz_do_pliku(wyniki, nazwa_pliku)




def oblicz_potegi(*args):
    """
    Funkcja przyjmuje argumenty x1, x2, ..., xn i zwraca wyniki x1^x1, x2^x2, ..., xn^xn

    Args:
    *args: Argumenty - liczby, których potęgi należy obliczyć które potem są zamieniane na liste

    Returns:
    list: Lista zawierająca wyniki potęgowania które elementy są wyświetlane po przecinku.
    """
    wyniki = []
    if len(args) > 99:
        print("Błąd: Za dużo argumentów. Maksymalna liczba argumentów to 99.")
    else:
        for i in args:
            wyniki.append(pow(i,2))
    return wyniki

# Testowanie funkcji
# print("Podaj liczby oddzielone przecinkiem:")
# wejscie = input().split(',')
# argumenty = list(map(int, wejscie))

# wyniki = oblicz_potegi(*argumenty)
# print("Wyniki potęgowania: ")
# for x in wyniki:
#     if x == wyniki[-1]:
#         print(x, end=" ")
#     else:
#         print(x, end=",")


# ZADANIE 4 V-----------------------------------------------V

def oblicz_potegi_zad4(*args):
    """
    Funkcja przyjmuje argumenty x1, x2, ..., xn i zwraca wyniki potęgowania.

    Args:
    *args: Argumenty - liczby, których potęgi należy obliczyć.

    Returns:
    list: Lista zawierająca wyniki potęgowania.
    """
    wyniki = []
    if len(args) > 99:
        print("Błąd: Za dużo argumentów. Maksymalna liczba argumentów to 99.")
    else:
        global_vars = globals()
        for i in range(len(args)):
            x = args[i]
            global_vars[f'x{i+1}'] = x
            global_vars[f'y{i+1}'] = pow(x,2)
            wyniki.append(global_vars[f'y{i+1}'])
    return wyniki

# Testowanie funkcji
print("Podaj liczby oddzielone przecinkiem:")
wejscie = input().split(',')
argumenty = list(map(int, wejscie))

wyniki = oblicz_potegi_zad4(*argumenty)
print("Wyniki potęgowania:", wyniki)






