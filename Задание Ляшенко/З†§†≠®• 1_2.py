
a = int(input('Введите время в секундах '))

b = ( a // 3600 )
c = (( a - (b * 3600 )) // 60 )
d = ( a - ( b * 3600) - ( c * 60 ) )

print(f'Данное время соответствует: {b} часов : {c} минут: {d} секунд ')
