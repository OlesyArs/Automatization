month = int(input('Введите номер месяца: '))

def month_to_season(month):

    if month in [12, 1, 2]: 
        return 'зима'
    elif month in [3, 4, 5]:
        return 'весна'
    elif month in [6, 7, 8]:
        return 'лето'
    elif month in [9, 10, 11]:
        return 'осень'
    else:
        return 'Такой месяц не существует'   
    
   

print(month_to_season(month))