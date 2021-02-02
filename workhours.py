import math as m

# How many time you have for eating at the middle of a workday ?

LUNCH = 0.75

def getDay(hs, lunch = LUNCH):
    
    return hs[1] - hs[0] - lunch

wd = 17.5 - 8.5 - 0.75 # work day usual hours
friday = 16.25 - 8.5 - 0.75 # friday hours

'''
2020
august = {3:[8.5, 16.], 4:[8.5, 17.5], 6:[9.2, 15.], 7:[8.75, 16.25], 10:[8.5, 17.5], 11:[8.75, 16.5], 12:[8.5, 15.], 13:[13.5, 17.5], 14:[8.5, 16.25], 20:[8.5, 17.5], 21:[9.25, 16.25], 22:[8.75, 14.0],
         23:[8.5, 12.0]}
MyAugust = (wd*(4*4+1)+friday*(4))/2

september = {1:[8.5, 17.5], 2:[8.5, 17.5],3:[8.75, 13.25],7:[8.5, 17.5], 8:[9., 17.5], 9:[9., 13.25], 10:[8.5, 17.5], 21:[9., 15.75], 24:[8.5, 13.], 25:[9.,13.], 29:[8.6, 13.]}
MySep = (wd*(3*4+6 - 4)+friday*(4))/2

october = {2:[10., 15.2], 12:[8.5*5, 13.25*5], 19:[8.5*2, 13.25*2], 21:[8.75, 14.], 26:[8.5,17.5], 27:[8.75, 15.], 28:[8.75, 18.], 29:[9., 17.5], 30:[9.25, 16.25]}
MyOct = (wd*17 + friday*5)/2

novem = {3:[9., 16.5], 5:[8.75, 17.5], 6:[8.5, 16.0], 9:[9., 17.], 10:[9., 17.5], 11:[10., 17.], 12:[9., 13.5], 16:[9.,17.5],17:[9.25, 17.],23:[9.25,17.5],24:[9.25, 17.5]}
MyNov = (wd*16 + friday*4)/2
'''

# Set a dictionary with all everyday check-in's 

feb = {2:[10.5,17.5]}

# All days you should work off ?

MyFeb = (wd*15 + friday*4)/2


# Set current month 

month = feb 
MyMonth = MyFeb 

remain = MyMonth
for day in month:
    remain -= getDay(month[day])

pers = round((MyMonth - remain)/MyMonth*100, 2)

print(f'\n\tВсего в этом месяце: {MyMonth} часов\n Отходил: {MyMonth - remain:.2f} часов ({pers:.1f}%)')
print('\tОсталось: ', m.floor(remain), 'часов, ', "%.0f" % ((remain % 1) * 60), ' минут\n' )
print('Это примерно ', remain/8., ' ПОЛНЫХ рабочих дней\n')