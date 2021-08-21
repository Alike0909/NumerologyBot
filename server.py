import matplotlib.pyplot as plt
# %matplotlib inline
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm
from docx2pdf import convert
from datetime import date, timedelta
from formulas import *
import pandas as pd
from infos import *

doc = DocxTemplate("шаблон.docx")

name = input("Enter name: ")
intern_name = input("Enter passport name: ")
surname = input("Enter surname: ")
second_surname = input("Enter second surname: ")
language = input("Enter language ru/en/kz: ")
born = input("Enter date: ")

data = dateDivider(born)

year = int(data[0])
month = int(data[1])
day = int(data[2])

today = date.today()
this_year = today.year
next_year = this_year + 1

age = calculateAge(date(year, month, day)) #year, month, day

OPV = abs(checkZero(abs_taro(day) - abs_taro(month))) #ОПВ 
CZ = abs_taro(abs_taro(day) + abs_taro(month) + rest22(year)) #СЗ
####################################################################################
perf_planet = []
planet_name = []
planet_info = []

add_planet = []
add_planet_info = []

for perf, planet in psycho_portrait[day].items() : #процент и основная планета
    perf_planet.append(perf)
    planet_name.append(planet)
    planet_info.append(planet_infos.get('{}'.format(planet)))

    if day > 22: #если больше 22 то ДОП Планета!
        add_planet.append(add_psycho.get("{}".format(day)))
        add_planet_info.append(planet_infos.get('{}'.format(add_planet[0])))
    else:
        add_planet.append('')
        add_planet_info.append('')
####################################################################################
# print(kur1_info.get(abs(CZ - OPV)))
old_CZ = abs_taro(abs_taro(day) + abs_taro(month) + abs_taro(sumNumbers(year)))
kur1 = kur1_info.get(abs(old_CZ - OPV)) #КУР 1

# print(kur2_info.get(abs_taro(OPV + abs_taro(day))))
kur2 = kur2_info.get(abs_taro(OPV + abs_taro(day))) #КУР 2
####################################################################################
nameTotalInfo = nameKarmas(intern_name) #ПОЛНАЯ ИНФОРМАЦИЯ ПО ИМЕНИ - [i] нужно записать отдельно для элементов
####################################################################################
URD1 = sumNumbers(year) + sumNumbers(month) + sumNumbers(day)
URD1_info = urdCheck(URD1)
PZ1 = sumNumbers(URD1)
PZ1_info = pz_info.get(PZ1)

URD2 = URD1 - 2 * int(data[2][0])
URD2_info = urdCheck(URD2)
PZ2 = sumNumbers(URD2)
PZ2_info = pz_info.get(PZ2)

URD3 = URD1 + 2 * int(data[0][3])
URD3_info = urdCheck(URD3)
PZ3 = sumNumbers(URD3)
PZ3_info = pz_info.get(PZ3)

CZ_info = cz_info.get(CZ)
####################################################################################
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

# print(TP1)
# print(TP2)
# print(TP3)
# print(TP4)
# print(TP5)
# print(TP6)

OPV7 = checkZero(abs(OPV6 - TP6))
OPV_total.append(OPV7)
TP7 = abs_taro(OPV6 + TP6)
TP_total.append(TP7)
# print(OPV_total)

for i in TP_total:
    if i in OPV_total:
        TP_total.remove(i)

TP_total = list(dict.fromkeys(TP_total))
####################################################################################
surnameKarmas(surname, language)
surname_info = rodology.get(surnameKarmas(surname, language))
if surnameKarmas(surname, language) in OPV_total:
    block = "у вас заблокирован талант рода"
else:
    block = "у вас не заблокирован талант рода"

if second_surname != '':
    surnameKarmas(second_surname, language)
    second_surname_info = rodology.get(surnameKarmas(surname, language))
    if surnameKarmas(second_surname, language) in OPV_total:
        second_block = "у вас заблокирован талант рода"
    else:
        second_block = "у вас не заблокирован талант рода"
else:
    second_surname = ''
    second_surname_info = ''
    second_block = ''
####################################################################################
x = [12,24,36,48,60,72,84]

arkh_num = (day * 100 + month) * year
arkh_energy = list(map(int,str(arkh_num)))
while len(arkh_energy) < 7:
    arkh_energy.append(0)
arkh_average = [round((sum(arkh_energy) / 7),2)] * 7
max_arkh = max(arkh_energy)

rod_num = day * month * year
rod_energy = list(map(int,str(rod_num)))
while len(rod_energy) < 7:
    rod_energy.append(0)
max_rod = max(rod_energy)
if sum(rod_energy) < 26:
    rod_energy_norma = "ниже пределов нормы, показатель того, что Род вам не доверяет."
else:
    rod_energy_norma = "в пределах нормы, показатель того, что Род вам доверяет."

# plt.xkcd()
# plt.style.use('')
temp_var = findInterceptions(rod_energy, arkh_average[0])
temp_var2 = findInterceptions(arkh_energy, arkh_average[0])
new_norma = [round((sum(arkh_energy) / 7),2)] * (len(temp_var))
try:
    plt.scatter(temp_var, new_norma, c ="yellow", linewidths = 2, marker ="^",  edgecolor ="red",  s = 100)
    plt.scatter(temp_var2, new_norma, c ="blue", linewidths = 2, marker =">",  edgecolor ="green",  s = 100)
except:
    pass

plt.plot(x, arkh_energy, marker='s', linewidth=3, label='Энергия Архангела')
plt.plot(x, rod_energy, marker='o', linewidth=3, label='Энергия Рода')
plt.plot(x, arkh_average, 'r--', label='Средняя Энергия')
plt.xlabel('Годы')
plt.ylabel('Уровень энергии')
# plt.title('График Энергии')
# plt.legend(['Уровень энергии', 'График Энергии'], frameon=False, loc='lower center', ncol=2) 
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
# plt.legend(loc='best')
plt.savefig('Graph1.png')
plt.clf()
plt.cla()
####################################################################################
# temp_var = findInterceptions(rod_energy,arkh_average[0])
# temp_var2 = findInterceptions(arkh_energy,arkh_average[0])
####################################################################################
try:
    if len(Interpretation(rod_energy, arkh_average[0], "up")) == 1:
        rod_graph_up = '{}'.format(Interpretation(rod_energy, arkh_average[0], "up")[0])
    elif len(Interpretation(rod_energy, arkh_average[0], "up")) == 2:
        rod_graph_up = '{} и {}'.format(Interpretation(rod_energy, arkh_average[0], "up")[0], Interpretation(rod_energy, arkh_average[0], "up")[1])
    elif len(Interpretation(rod_energy, arkh_average[0], "up")) == 3:
        rod_graph_up = '{}, {} и {}'.format(Interpretation(rod_energy, arkh_average[0], "up")[0], Interpretation(rod_energy, arkh_average[0], "up")[1], Interpretation(rod_energy, arkh_average[0], "up")[2])
except:
    rod_graph_up = 'до конца жизни'

try:
    if len(Peaks(rod_energy, arkh_average[0])) == 1:
        peaks_info = '{}'.format(Peaks(rod_energy, arkh_average[0])[0])
    elif len(Peaks(rod_energy, arkh_average[0])) == 2:
        peaks_info = '{} и {}'.format(Peaks(rod_energy, arkh_average[0])[0], Peaks(rod_energy, arkh_average[0])[1])
    elif len(Peaks(rod_energy, arkh_average[0])) == 3:
        peaks_info = '{}, {} и {}'.format(Peaks(rod_energy, arkh_average[0])[0], Peaks(rod_energy, arkh_average[0])[1], Peaks(rod_energy, arkh_average[0])[2])
    elif len(Peaks(rod_energy, arkh_average[0])) == 0:
        peaks_info = 'такого нет :('
except:
    peaks_info = 'такого нет :('

try:
    if len(Interpretation(rod_energy, arkh_average[0], "down")) == 1:
        rod_graph_down = '{}'.format(Interpretation(rod_energy, arkh_average[0], "down")[0])
    elif len(Interpretation(rod_energy, arkh_average[0], "down")) == 2:
        rod_graph_down = '{} и {}'.format(Interpretation(rod_energy, arkh_average[0], "down")[0], Interpretation(rod_energy, arkh_average[0], "down")[1])
    elif len(Interpretation(rod_energy, arkh_average[0], "down")) == 3:
        rod_graph_down = '{}, {} и {}'.format(Interpretation(rod_energy, arkh_average[0], "down")[0], Interpretation(rod_energy, arkh_average[0], "down")[1], Interpretation(rod_energy, arkh_average[0], "down")[2])
except:
    rod_graph_down = 'до конца жизни'
####################################################################################
try:
    if len(Interpretation(arkh_energy, arkh_average[0], "up")) == 1:
        arkh_graph_up = '{}'.format(Interpretation(arkh_energy, arkh_average[0], "up")[0])
    elif len(Interpretation(arkh_energy, arkh_average[0], "up")) == 2:
        arkh_graph_up = '{} и {}'.format(Interpretation(arkh_energy, arkh_average[0], "up")[0], Interpretation(arkh_energy, arkh_average[0], "up")[1])
    elif len(Interpretation(arkh_energy, arkh_average[0], "up")) == 3:
        arkh_graph_up = '{}, {} и {}'.format(Interpretation(arkh_energy, arkh_average[0], "up")[0], Interpretation(arkh_energy, arkh_average[0], "up")[1], Interpretation(arkh_energy, arkh_average[0], "up")[2])
except:
    arkh_graph_up = 'до конца жизни'

try:
    if len(Interpretation(arkh_energy, arkh_average[0], "down")) == 1:
        arkh_graph_down = '{}'.format(Interpretation(arkh_energy, arkh_average[0], "down")[0])
    elif len(Interpretation(arkh_energy, arkh_average[0], "down")) == 2:
        arkh_graph_down = '{} и {}'.format(Interpretation(arkh_energy, arkh_average[0], "down")[0], Interpretation(arkh_energy, arkh_average[0], "down")[1])
    elif len(Interpretation(arkh_energy, arkh_average[0], "down")) == 3:
        arkh_graph_down = '{}, {} и {}'.format(Interpretation(arkh_energy, arkh_average[0], "down")[0], Interpretation(arkh_energy, arkh_average[0], "down")[1], Interpretation(arkh_energy, arkh_average[0], "down")[2])
    elif len(Interpretation(arkh_energy, arkh_average[0], "down")) == 0:
        # arkh_graph_down = 'ERROR'
        downwards = findInterceptionsDown(arkh_energy, arkh_average[0])
        arkh_graph_down = '{} - до конца жизни'.format(downwards[-1])
except:
    downwards = findInterceptionsDown(arkh_energy, arkh_average[0])
    arkh_graph_down = '{} - до конца жизни'.format(downwards[-1])
####################################################################################
#Tут вообщем все что связано с месяцами наверное
MC_period = sumNumbers(day) + sumNumbers(month) + sumNumbers(year)
MC1_period = ('0 - {}'.format(MC_period))
MC2_period = ('{} - {}'.format(MC_period + 1, MC_period + 9))
MC3_period = ('{} - ∞'.format(MC_period + 10))

mc1 = rest22(day)
mc2 = rest22(month)
mc3 = rest22(sumNumbers(year))

mc1_info = mcycles.get(mc1)
mc2_info = mcycles.get(mc2)
mc3_info = mcycles.get(mc3)

MC = []
a = 0
while len(MC) < 8:
    MC.append(MC_period + a)
    a = a + 9


for i in MC:
    if i > age:
        nearest_age = i
        break
nearest_age_end = nearest_age + 1
nearest_period = MC.index(nearest_age)+1
####################################################################################
a = SexTotal(day, month, year, URD1, URD2, PZ1, PZ2)
####################################################################################
OPV_info = []
for i in OPV_total:
    OPV_info.append(opv.get(i))
# print(OPV_info[6])

opv_age = 36 - PZ1
opv1_age = "{} - {} лет".format(0, opv_age)
opv2_age = "{} - {} лет".format(opv_age + 1, opv_age + 9)
opv3_age = "{} - {} лет".format(opv_age + 10, opv_age + 18)
opv4_age = "{} - {} лет".format(opv_age + 19, opv_age + 27)
opv5_age = "{} - {} лет".format(opv_age + 28, opv_age + 36)
####################################################################################
TP_info = []
for i in TP_total:
    TP_info.append(tp.get(i))

while len(TP_info) < 7:
    TP_info.append('')
####################################################################################
if (this_year - year) == age:
    will = 'начался'
else:
    will = 'начнется'
YearCycle(day, month, year, age)
period = sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(this_year)))
####################################################################################
mercury_start = "{}/{}/{}".format(day, month, year)
mercury_finish = pd.to_datetime(mercury_start, format='%d/%m/%Y') + pd.DateOffset(days=52)
# "{}.{}".format(enddate.day, enddate.month)
venus_start = mercury_finish + pd.DateOffset(days=1)
venus_finish = venus_start + pd.DateOffset(days=51)
mars_start = venus_finish + pd.DateOffset(days=1)
mars_finish = mars_start + pd.DateOffset(days=51)
jupiter_start = mars_finish + pd.DateOffset(days=1)
jupiter_finish = jupiter_start + pd.DateOffset(days=51)
saturn_start = jupiter_finish + pd.DateOffset(days=1)
saturn_finish = saturn_start + pd.DateOffset(days=51)
uranus_start = saturn_finish + pd.DateOffset(days=1)
uranus_finish = uranus_start + pd.DateOffset(days=51)
neptune_start = uranus_finish + pd.DateOffset(days=1)
neptune_finish = neptune_start + pd.DateOffset(days=51)
####################################################################################


####################################################################################
OPV_total = list(dict.fromkeys(OPV_total))
countries = []

for i in OPV_total:
    countries.append(karma_countries.get(i))

while len(countries) < 7:
    countries.append('')
####################################################################################
ZK = abs_taro(abs_taro(day) + (2 * abs_taro(month)) + abs_taro(sumNumbers(year)))
####################################################################################
x = [10,20,30,40,50,60,70]

career_num = (day * 100 + month) * year
career_energy = list(map(int,str(career_num)))
while len(career_energy) < 7:
    career_energy.append(0)
career_average = [round((sum(career_energy) / 7),2)] * 7
max_career = max(career_energy)

life_num = day * month * year
life_energy = list(map(int,str(life_num)))
# print(len(life_energy))
while len(life_energy) < 7:
    life_energy.append(0)
max_life = max(life_energy)

plt.plot(x, career_energy, marker='s', linewidth=3, label='Карьера')
plt.plot(x, life_energy, marker='o', linewidth=3, label='Личная жизнь')
plt.plot(x, career_average, 'r--', label='Средняя Энергия')
plt.xlabel('Годы')
plt.ylabel('Уровень энергии')
# plt.title('График Энергии')
# plt.legend(['Уровень энергии', 'График Энергии'], frameon=False, loc='lower center', ncol=2) 
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
# plt.legend(loc='best')
plt.savefig('Graph3.png')
plt.clf()
plt.cla()
####################################################################################

context = { 
    'name' : name,
    'intern_name' : intern_name,
    'surname' : surname,
    'second_surname' : second_surname,
    'date' : born,
    'age' : age,

    'date_day' : day,
    'date_month' : month,
    'this_year' : this_year,
    'next_year' : next_year,

    'planet_perf' : perf_planet[0],
    'planet' : planet_name[0],
    'planet_info' : planet_info[0],
    'planet_add' : add_planet[0],
    'planet_add_info' : add_planet_info[0],

    'Kur1' : kur1,
    'Kur2' : kur2,

    'name_info' : nameTotalInfo[1],
    'name_info2' : nameTotalInfo[2],
    'name_talant1' : nameTotalInfo[3],
    'name_talant2' : nameTotalInfo[4],
    'name_karma1' : nameTotalInfo[5],
    'name_karma2' : nameTotalInfo[6],

    'key1' : URD1,
    'key2' : PZ1,
    'key3' : URD2,
    'key4' : PZ2,
    'key5' : URD3,
    'key6' : PZ3,
    'chzhp' : PZ1,
    'key1_info' : URD1_info,
    'key3_info' : URD2_info,
    'key5_info' : URD3_info,
    'key2_info' : PZ1_info,
    'key4_info' : PZ2_info,
    'key6_info' : PZ3_info,

    'social' : CZ_info,
    
    'surname_info' : surname_info,
    'block' : block,
    'second_surname_info' : second_surname_info,
    'second_block' : second_block,

    'rod_energy_norma' : rod_energy_norma,
    'graph' : InlineImage(doc, 'Graph1.png', width=Cm(20), height=Cm(12)),
    'temp_var' : temp_var,
    'temp_var2' : temp_var2,
    'rod_graph_down' : rod_graph_down,
    'rod_graph_up' : rod_graph_up,
    'peaks' : peaks_info,
    'arkh_graph_down' : arkh_graph_down,
    'arkh_graph_up' : arkh_graph_up,

    'month_info' : MonthTotalInfo(month),
    'month_info_period' : MC2_period,

    'MC1_period' : MC1_period,
    'MC2_period' : MC2_period,
    'MC3_period' : MC3_period,
    'mc1_info' : mc1_info,
    'mc2_info' : mc2_info,
    'mc3_info' : mc3_info,
    'num1' : MC_period,
    'num2' : MC_period+9,
    'num3' : MC_period+18,
    'num4' : MC_period+27,
    'num5' : MC_period+36,
    'num6' : MC_period+45,
    'num7' : MC_period+54,
    'num8' : MC_period+63,
    'nearest_age' : nearest_age,
    'nearest_age_end' : nearest_age_end,
    'nearest_period' : nearest_period,

    'sex_info' : SexTotal(day, month, year, URD1, URD2, PZ1, PZ2),

    'opv1_info' : OPV_info[0],
    'opv2_info' : OPV_info[1],
    'opv3_info' : OPV_info[2],
    'opv4_info' : OPV_info[3],
    'opv5_info' : OPV_info[4],
    'opv6_info' : OPV_info[5],
    'opv7_info' : OPV_info[6],

    'opv1_age' : opv1_age,
    'opv2_age' : opv2_age,
    'opv3_age' : opv3_age,
    'opv4_age' : opv4_age,
    'opv5_age' : opv5_age,
    
    'tp1_info' : TP_info[0],
    'tp2_info' : TP_info[1],
    'tp3_info' : TP_info[2],
    'tp4_info' : TP_info[3],
    'tp5_info' : TP_info[4],
    'tp6_info' : TP_info[5],
    'tp7_info' : TP_info[6],

    'will' : will,
    'period' : period,
    'graph2' : InlineImage(doc, 'Graph2.png', width=Cm(20), height=Cm(12)),

    'mercury_start' : "{}.{}".format(day, month),
    'mercury_finish' : "{}.{}".format(mercury_finish.day, mercury_finish.month),
    'venus_start' : "{}.{}".format(venus_start.day, venus_start.month),
    'venus_finish' : "{}.{}".format(venus_finish.day, venus_finish.month),
    'mars_start' : "{}.{}".format(mars_start.day, mars_start.month),
    'mars_finish' : "{}.{}".format(mars_finish.day, mars_finish.month),
    'jupiter_start' : "{}.{}".format(jupiter_start.day, jupiter_start.month),
    'jupiter_finish' : "{}.{}".format(jupiter_finish.day, jupiter_finish.month),
    'saturn_start' : "{}.{}".format(saturn_start.day, saturn_start.month),
    'saturn_finish' : "{}.{}".format(saturn_finish.day, saturn_finish.month),
    'uranus_start' : "{}.{}".format(uranus_start.day, uranus_start.month),
    'uranus_finish' : "{}.{}".format(uranus_finish.day, uranus_finish.month),
    'neptune_start' : "{}.{}".format(neptune_start.day, neptune_start.month),
    'neptune_finish' : "{}.{}".format(neptune_finish.day, neptune_finish.month),

    'graph3' : InlineImage(doc, 'Graph3.png', width=Cm(25), height=Cm(14.5)),
    
    'country1' : countries[0],
    'country2' : countries[1],
    'country3' : countries[2],
    'country4' : countries[3],
    'country5' : countries[4],
    'country6' : countries[5],
    'country7' : countries[6],

    'zk_info' : zk_info.get(ZK),
    'prof_zk' : professions.get(ZK),
    'prof_date' : professions.get(abs_taro(day)),
    'prof_cz' : professions.get(CZ),
    'stone' : stones.get(CZ)
}

doc.render(context)
doc.save("/Users/godsmacbook/Desktop/{} {} {}.docx".format(name, surname, born))

# convert(r"/Users/godsmacbook/Desktop/{} {} {}.docx".format(name, surname, born), r"novoe.pdf")
