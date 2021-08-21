# # from datetime import date 
# from formulas import *
# import inspect
# # born = '09.09.1979'

# # data = dateDivider(born)

# # year = int(data[0])
# # month = int(data[1])
# # day = int(data[2])

# # print(date(year, month, day))

# # from infos import *

# # for key, value in psycho_portrait[19].items() :
# #     print(key, value)
# # print(planets[1].keys())

# # print(planet_info.get('Солнце'))
# # print(kur1_info.get(1))

# # print(rest22(1980))
# # print(urdCheck(41))
# # name = 'мустафаев'
# # surname = []

# # for i in name:
# #     for num, let in ru.items():
# #         if i in let:
# #             surname.append(num)

# # print(sum(surname))
# # print(surnameKarmas(name))

# import os
# import platform

# userhome = os.path.expanduser('~')
# desktop = userhome + '/Desktop/'
# useros = platform.system() # returns e.g. 'Linux' 'Windows' 
# distribution = platform.linux_distribution()

# import matplotlib.pyplot as plt

# x = [12,24,36,48,60,72,84]
# y = [5, 8, 1, 2, 9, 0, 5]

# x2 = [12,24,36,48,60,72,84]
# y2 = [2, 9, 0, 1, 4, 5, 0]

# x3 = [12,24,36,48,60,72,84]
# y3 = [4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2]

# plt.plot(x, y, marker='s', linewidth=3, label='Энергия Архангела')
# plt.plot(x2, y2, marker='o', linewidth=3, label='Энергия Рода')
# plt.plot(x3, y3, 'r--', label='Средняя Энергия')
# plt.xlabel('Годы')
# plt.ylabel('Уровень энергии')
# plt.title('График Энергии')
# plt.legend()
# plt.show()
# def findInterceptionsDown(energy, average):
#     x = [12,24,36,48,60,72,84]
#     y = energy
#     n = average
#     ind = []
#     k = []
#     l = []
#     interception = []
#     for i in range(len(y)-1):
#         # if ((y[i]>n and y[i+1]<n) or (y[i]<n and y[i+1]>n)):
#         if ((y[i]>n and y[i+1]<n)):
#             k.append((y[i+1]-y[i])/12)
#             ind.append(i)

#     for i in range(len(k)):
#         l.append(y[ind[i]]-x[ind[i]]*k[i])

#     for i in range(len(k)):
#         interception.append(int(round((n-l[i])/k[i],0)))

#     return interception

# def findInterceptionsUp(energy, average):
#     x = [12,24,36,48,60,72,84]
#     y = energy
#     n = average
#     ind = []
#     k = []
#     l = []
#     interception = []
#     for i in range(len(y)-1):
#         # if ((y[i]>n and y[i+1]<n) or (y[i]<n and y[i+1]>n)):
#         if ((y[i]<n and y[i+1]>n)):
#             k.append((y[i+1]-y[i])/12)
#             ind.append(i)

#     for i in range(len(k)):
#         l.append(y[ind[i]]-x[ind[i]]*k[i])

#     for i in range(len(k)):
#         interception.append(int(round((n-l[i])/k[i],0)))

#     return interception

# x = [12,24,36,48,60,72,84]
# data = [5, 8, 1, 2, 9, 0, 5]
# data = [2, 9, 0, 1, 4, 5, 0]
# data = [1, 6, 0, 2, 9, 9, 0]
# # data = [4, 0, 1, 8, 0, 1, 4]
data = [3, 7, 8, 1, 8, 6, 9]
# # data = [4, 1, 3, 6, 1, 1, 0]
# # data = [2, 5, 8, 3, 9, 6, 6]
# data = [1, 7, 9, 8, 9, 1, 1]
avg = 6

# def forBest(upwards, peaks):
#     best = []
#     for i in range(len(upwards)):
#         if upwards[i] < peaks[i]:
#             best.append("{}-{}".format(upwards[i],peaks[i]))
    
#     return best

# def Interpretation(data, avg):
#     x = [12,24,36,48,60,72,84]
#     downwards = findInterceptionsDown(data,avg)
#     upwards = findInterceptionsUp(data,avg)
#     peaks = []
#     for i in range(len(data)-2):
#         if data[i+1] > data[i] and data[i+1] >= data[i+2]:
#             if data[i+1] > avg:
#                 peaks.append(x[i+1])
#         # elif data[i+2] > avg and data[i+2] > data[i+1]:
#         elif data[i+1] > avg and data[i+1] == data[i]:
#             peaks.remove(x[i])
#             peaks.append(x[i+1])
#         elif data[i+2] > avg and data[i+2] > data[i+1]:
#             peaks.append(x[i+2])

#     peaks = list(dict.fromkeys(peaks))
#     # print(peaks)

#     best = None
#     try:
#         if upwards[0] > peaks[0]:
#             temp = peaks[0]
#             peaks.remove(peaks[0])
#             best = forBest(upwards, peaks)
#             best.insert(0,temp)
#         else:
#             best = forBest(upwards, peaks)
#     except:
#         best = None

#     # print(best)
#     return best
# # a = []
# # a.append('hey')
# # print(a)

# print(Interpretation(data, avg))

from formulas import *
from infos import *
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
from matplotlib import style
import pandas as pd
# style.use('seaborn')

# today = date.today()
# this_year = today.year
# years = []
# i = 0
# while len(years) < 9:
#     new_year = this_year + i
#     years.append(new_year)
#     i += 1

# day = 9
# month = 9
# cycle_names = []
# for i in years:
#     cycle_names.append(sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(i))))

# cycles = []
# for i in years:
#     cycle = sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(i)))
#     if cycle > 5:
#         cycle = 10 - cycle
#         cycles.append(cycle)
#     else:
#         cycles.append(sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(i))))

# bar = plt.bar(years, cycles, color='ymcrgbkmy')
# plt.xticks(rotation=45)
# plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# plt.title('Годичные циклы', fontsize=20, fontweight='bold')
# plt.show()




# result = forWorst(up, down)
# print(Interpretation(data, avg, "down"))
# print(result)
# print(forWorst([16, 62], [30, 74]))

# print(MonthTotalInfo(5))

# print(sumNumbers(19) + sumNumbers(11) + sumNumbers(1979))

# result = Interpretation(data, avg, "down")

# down = findInterceptionsDown(data, avg)
# up = findInterceptionsUp(data, avg)
# print(down)
# print(up)

# # peaks = Peaks(data, avg)
# print(result)

# print(len(down))

# print(opv.get(1))
# day = 3
# month = 4
# year = 1982
# x = [12,24,36,48,60,72,84]

# arkh_num = (day * 100 + month) * year
# arkh_energy = list(map(int,str(arkh_num)))
# if len(arkh_energy) < 7:
#     arkh_energy.append(str(0))
# print(arkh_energy)
# StartDate = "19/11"

# Date = datetime.strptime(StartDate, "%d/%m")
# EndDate = Date + timedelta(days=52)
# print(EndDate)
# import pandas as pd
# startdate = "19/11/"
# enddate = pd.to_datetime(startdate) + pd.DateOffset(days=52)
# print("{}.{}".format(enddate.day, enddate.month))
day = 6
month = 11
year  = 1987
# age = 38
# MC_period = sumNumbers(day) + sumNumbers(month) + sumNumbers(year)
# MC = []
# a = 0
# while len(MC) < 8:
#     MC.append(MC_period + a)
#     a = a + 9

# for i in MC:
#     if i > age:
#         nearest_age = i
#         break

# print(nearest_age)
# print(MC.index(nearest_age)+1)
# print(MC)

# mercury_start = "{}/{}/{}".format(day, month, year)
# mercury_finish = pd.to_datetime(mercury_start, format='%d/%m/%Y') + pd.DateOffset(days=52)

# print(mercury_start)
# print(mercury_finish)

CZ = abs_taro(abs_taro(day) + abs_taro(month) + rest22(year))
old_CZ = abs_taro(abs_taro(day) + abs_taro(month) + abs_taro(sumNumbers(year)))

print(old_CZ)
print(stones.get(old_CZ))