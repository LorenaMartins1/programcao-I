temp = float(input())

if temp >= 39:
    print('Febre alta')
elif temp >= 37 and temp < 39:
    print('febril')
else:
    print('sem febre')