from formulas import *
from infos import *

name = input("Enter name: ")
surname = input("Enter surname: ")
born = input("Enter date: ")

data = dateDivider(born)

year = int(data[0])
month = int(data[1])
day = int(data[2])

age = calculateAge(date(year, month, day)) #year, month, day

OPV = checkZero(abs_taro(day) - abs_taro(month)) #ОПВ 
CZ = abs_taro(abs_taro(day) + abs_taro(month) + rest22(year)) #СЗ

for perf, planet in psycho_portrait[day].items() : #процент и основная планета
    # print(perf, planet)
    # print(planet_info.get('{}'.format(planet)))

    if day > 22: #если больше 22 то ДОП Планета!
        # print(add_psycho.get("{}".format(day)))
        add_planet = add_psycho.get("{}".format(day))
        # print(planet_info.get('{}'.format(add_planet)))

nameTotalInfo = nameKarmas(name) #ПОЛНАЯ ИНФОРМАЦИЯ ПО ИМЕНИ - [i] нужно записать отдельно для элементов
for i in range(1, len(nameTotalInfo)):
    # print("{}".format(nameTotalInfo[i]))
    print("")

kur1 = abs(CZ - OPV) #КУР 1
# print(kur1_info.get(kur1))

kur2 = abs_taro(OPV + abs_taro(day)) #КУР 2
# print(kur2_info.get(kur2))
# print(kur1)
# print(kur2)

URD1 = sumNumbers(year) + sumNumbers(month) + sumNumbers(day)
PZ1 = sumNumbers(URD1)
URD1_info = urdCheck(URD1)
print(URD1)
print(PZ1)

URD2 = URD1 - 2 * int(data[2][0])
PZ2 = sumNumbers(URD2)
URD2_info = urdCheck(URD2)
print(URD2)
print(PZ2)

URD3 = URD1 + 2 * int(data[0][3])
PZ3 = sumNumbers(URD3)
URD3_info = urdCheck(URD3)
print(URD3)
print(PZ3)

CZ_info = cz_info.get(CZ)

surnameKarmas(surname, 'ru')
print(surnameKarmas(surname, 'ru'))

OPV_total = []
TP_total = []

OPV1 = checkZero(abs(abs_taro(day) - month))
OPV_total.append(OPV1)
OPV2 = checkZero(abs(abs_taro(day) - abs_taro(sumNumbers(year))))
OPV_total.append(OPV2)
OPV3 = checkZero(abs(OPV1 - OPV2))
OPV_total.append(OPV3)
OPV4 = checkZero(abs(month - abs_taro(sumNumbers(year))))
OPV_total.append(OPV4)
OPV5 = checkZero(abs(month-OPV3))
OPV_total.append(OPV5)
OPV6 = abs_taro(OPV1 + OPV2 + OPV3 + OPV4 + OPV5)
OPV_total.append(OPV6)

TP1 = abs_taro(abs(abs_taro(day) + month))
TP_total.append(TP1)
TP2 = abs_taro(abs(abs_taro(day) + abs_taro(sumNumbers(year))))
TP_total.append(TP2)
TP3 = abs_taro(abs(TP1 + TP2))
TP_total.append(TP3)
TP4 = abs_taro(abs(month + abs_taro(sumNumbers(year))))
TP_total.append(TP4)
TP5 = abs_taro(abs(month + TP3))
TP_total.append(TP5)
TP6 = abs_taro(TP1 + TP2 + TP3 + TP4 + TP5)
TP_total.append(TP6)

OPV7 = checkZero(abs(OPV6 - TP6))
OPV_total.append(OPV7)
TP7 = abs_taro(OPV6 + TP6)
TP_total.append(TP7)

for i in TP_total:
    if i in OPV_total:
        TP_total.remove(i)
        # if i in OPV_total:
        #     TP_total.remove(i)

TP_total = list(dict.fromkeys(TP_total))

print(OPV_total)
print(TP_total)
# print(TP1 , TP2 , TP3 , TP4 , TP5, TP6, TP7)
# print(OPV1 , OPV2 , OPV3 , OPV4 , OPV5, OPV6, OPV7)
if surnameKarmas in OPV_total:
    block = "заблокировано"
else:
    block = "не заблокировано"
print(surnameKarmas)
print(block)