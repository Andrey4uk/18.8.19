summ_tickets = 0
quantity_tickets = int(input('Здравствуйте! Введите количество билетов:\t'))

for age in range(quantity_tickets):
    age = int(input('Введите возраст посетителя:\t'))
    if age<18:
        summ_tickets += 0
    elif 18<=age<=25:
        summ_tickets += 990
    elif age>25:
        summ_tickets += 1390

if quantity_tickets > 3:
    summ_tickets -= summ_tickets / 100 * 10

print('Стоимость билетов составила:\t',summ_tickets)