from datetime import date

music_band ={
    'members':{
        'Tim':{
            'role':'singer',
            'date':(2000,4,27)
        },
        'Tom':{
            'role':'drumer',
            'date':(1999,12,1)
        },
        'Beks':{
            'role':'guitar',
            'date':(2000,4,28)
        }
    },
    'concerts':{
        'London':{
            'concert_date':date(2021,12,31),
            'expenses':[123,342,133],
            'income':10000
        },
        'Bishkek':{
            'concert_date':date(2022,11,2),
            'expenses':[555,342,113],
            'income':20000
        }
    }




}

def add_new_member(gastroli, **kwargs):
    gastroli['members'].update(kwargs)
    return gastroli


print(add_new_member(gastroli, **{'Nikolai Baskov': {'role': 'gj', 'date': date(1988, 9, 11)}}))


Удаление учаника

def remove(gastroli, name):
    return gastroli['members'].pop(name)


remove(gastroli, 'filip Kirkorov')
print(gastroli['members'])

def add_new_concert(gastroli, **kwargs):
    gastroli['concerts'].update(kwargs)
    return gastroli


print(add_new_concert(gastroli, **{'Talas': {
    'concert_date': date(2021, 8, 12),
    'expenses': [100, 122, 123, ],
    'income': 10000
}}))




def func_(gastroli,**kwargs):
    total = 0
    for i in gastroli:
        a = gastroli[i]['expenses']
        total += sum(a)
        return total
print(func_(gastroli['concerts']))


def func_(gastroli):
    total = 0
    for i in gastroli:
        total += i
    return total

print(func_(gastroli['concerts']['london']['expenses']))
print(func_(gastroli['concerts']['Bishkek']['expenses']))
print(func_(gastroli['concerts']['Osh']['expenses']))


# Напишите функцию, высчитывающую выгоду за концерт(разницу между затратами и суммой контракта)
def calcu_expenses(*args):
    return sum(args)


def func(gastroli, concert_name):
    income = gastroli['concerts'][concert_name]['income']
    return income - calcu_expenses(*gastroli['concerts'][concert_name]['expenses'])


print(func(gastroli, 'london'))
print(music_band)
