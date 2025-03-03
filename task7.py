raw=input()
try:
    num=int(raw)
except ValueError:
    print('Можно вводить только числовые значения, а длина строки равна', len(raw))
else:
    print(num)
