import matplotlib.pyplot as plot
from matplotlib import style
from datetime import date 
import transliterate as tr
from infos import *
  
def calculateAge(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
  
    # raised when birth date is February 29 
    # and the current year is not a leap year 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 

# print(calculateAge(date(1979, 9, 8)), "years") 

def zeroDeleter(num):
    if int(num[0]) == 0:
        return num[1]
    else:
        return num

def dateDivider(born):
    final_date = []

    born = born.replace('.', '')
    day = zeroDeleter(born[:2])
    month = zeroDeleter(born[2:-4])
    year = born[4:]

    final_date.append(year)
    final_date.append(month)
    final_date.append(day)

    return final_date

def nameCorrect(name):
    for i in name:
        if i == 'х':
            name = name.replace(i, 'kh')
        elif i == 'й':
            name = name.replace(i, 'y')
        elif i == 'е':
            name = name.replace(i, 'ye')
        elif i == 'я':
            name = name.replace(i, 'ya')
    
    return name

def nameKarmas(message):
    total_info = []

    name = message.lower()
    name = nameCorrect(name)
    code = []
    try:
        for i in name:
            key = list(name_code.keys())[list(name_code.values()).index(i)]
            if key > 22:
                code.append(key-22)
            else:
                code.append(key)
    except:
        name = tr.translit(name, reversed=True)
        name = name.replace("'", "")
        for i in name:
            key = list(name_code.keys())[list(name_code.values()).index(i)]
            if key > 22:
                code.append(key-22)
            else:
                code.append(key)

    total = sum(code)

    while total > 22:
        total = total - 22

    total_info.append(name)

    aim = list(name_aim.values())[list(name_aim.keys()).index(total)]
    total_info.append(str(aim))
    name_ = list(name_info.values())[list(name_info.keys()).index(total)]
    total_info.append(str(name_))

    talant_1 = list(name_talant.values())[list(name_talant.keys()).index(code[0])]
    total_info.append(str(talant_1))
    tal2 = code[0] + code[1]
    if tal2 > 22:
        tal2 = tal2 - 22
    talant_2 = list(name_talant.values())[list(name_talant.keys()).index(tal2)]
    total_info.append(str(talant_2))

    karma_1 = list(name_karma.values())[list(name_karma.keys()).index(code[len(code)-1])]
    total_info.append(str(karma_1))
    karm2 = code[len(code)-1] + code[len(code)-2]
    if karm2 > 22:
        karm2 = karm2 - 22
    karma_2 = list(name_karma.values())[list(name_karma.keys()).index(karm2)]
    total_info.append(str(karma_2))

    return total_info

def abs_taro(num):
    while int(num) > 22:
        num = num - 22
        if num <= 22:
            return num
    else:
        return num

def checkZero(num):
    if num == 0:
        num = 22
        return num
    else:
        return num

def sumNumbers(num):
    total = []

    for i in str(num):
        total.append(int(i))

    result = sum(total)

    return result

def rest22(num):
    rest = num / 22
    result = num - (int(rest) * 22)

    if result != 0:
        return result
    if result == 0:
        result = 22
        return result

def urdCheck(urd):
    if urd < 20:
        result = urd_info.get(1)
    elif urd > 19 and urd < 30:
        result = urd_info.get(2)
    elif urd > 29 and urd < 40:
        result = urd_info.get(3)
    elif urd > 39 and urd < 50:
        result = urd_info.get(4)
    elif urd > 49 and urd < 60:
        result = urd_info.get(5)
    else:
        result = urd_info.get(6)

    return result

def surnameKarmas(surname, language):
    result = []
    surname = surname.lower()

    if language == 'ru':
        for i in surname:
            for num, let in ru.items():
                if i in let:
                    result.append(num)
    elif language == 'en':
        for i in surname:
            for num, let in en.items():
                if i in let:
                    result.append(num)
    else:
        for i in surname:
            for num, let in kz.items():
                if i in let:
                    result.append(num)

    return abs_taro(sum(result))

def findInterceptions(energy, average):
    x = [12,24,36,48,60,72,84]
    y = energy
    n = average
    ind = []
    k = []
    l = []
    interception = []
    for i in range(len(y)-1):
        if ((y[i]>n and y[i+1]<n) or (y[i]<n and y[i+1]>n)):
            k.append((y[i+1]-y[i])/12)
            ind.append(i)

    for i in range(len(k)):
        l.append(y[ind[i]]-x[ind[i]]*k[i])

    for i in range(len(k)):
        interception.append(int(round((n-l[i])/k[i],0)))

    return interception

def findInterceptionsDown(energy, average):
    x = [12,24,36,48,60,72,84]
    y = energy
    n = average
    ind = []
    k = []
    l = []
    interception = []
    for i in range(len(y)-1):
        # if ((y[i]>n and y[i+1]<n) or (y[i]<n and y[i+1]>n)):
        if ((y[i]>n and y[i+1]<n)):
            k.append((y[i+1]-y[i])/12)
            ind.append(i)

    for i in range(len(k)):
        l.append(y[ind[i]]-x[ind[i]]*k[i])

    for i in range(len(k)):
        interception.append(int(round((n-l[i])/k[i],0)))

    return interception

def findInterceptionsUp(energy, average):
    x = [12,24,36,48,60,72,84]
    y = energy
    n = average
    ind = []
    k = []
    l = []
    interception = []
    for i in range(len(y)-1):
        # if ((y[i]>n and y[i+1]<n) or (y[i]<n and y[i+1]>n)):
        if ((y[i]<n and y[i+1]>n)):
            k.append((y[i+1]-y[i])/12)
            ind.append(i)

    for i in range(len(k)):
        l.append(y[ind[i]]-x[ind[i]]*k[i])

    for i in range(len(k)):
        interception.append(int(round((n-l[i])/k[i],0)))

    return interception

def forBest(upwards, peaks):
    best = []
    for i in range(len(upwards)):
        if upwards[i] < peaks[i]:
            best.append("{}-{}".format(upwards[i],peaks[i]))
    
    return best

def forWorst(upwards, downwards):
    worst = []
    for i in range(len(downwards)):
        if downwards[i] < upwards[i]:
            worst.append("{}-{}".format(downwards[i],upwards[i]))

    return worst

def Peaks(data, avg):
    x = [12,24,36,48,60,72,84]
    downwards = findInterceptionsDown(data,avg)
    upwards = findInterceptionsUp(data,avg)
    peaks = []
    for i in range(len(data)-2):
        if data[i+1] > data[i] and data[i+1] >= data[i+2]:
            if data[i+1] > avg:
                peaks.append(x[i+1])
        # elif data[i+2] > avg and data[i+2] > data[i+1]:
        elif data[i+1] > avg and data[i+1] == data[i]:
            peaks.remove(x[i])
            peaks.append(x[i+1])
        elif data[i+2] > avg and data[i+2] > data[i+1]:
            peaks.append(x[i+2])

    peaks = list(dict.fromkeys(peaks))
    return peaks

def Interpretation(data, avg, status):
    x = [12,24,36,48,60,72,84]
    downwards = findInterceptionsDown(data,avg)
    upwards = findInterceptionsUp(data,avg)
    # print(upwards)
    # print(downwards)
    peaks = []
    for i in range(len(data)-2):
        if data[i+1] > data[i] and data[i+1] >= data[i+2]:
            if data[i+1] > avg:
                peaks.append(x[i+1])
        # elif data[i+2] > avg and data[i+2] > data[i+1]:
        elif data[i+1] > avg and data[i+1] == data[i]:
            peaks.remove(x[i])
            peaks.append(x[i+1])
        elif data[i+2] > avg and data[i+2] > data[i+1]:
            peaks.append(x[i+2])

    peaks = list(dict.fromkeys(peaks))
    # print(peaks)
    if status == "up":
        try:
            if upwards[0] > peaks[0]:
                peaks.remove(peaks[0])
                # best = forBest(upwards, peaks)
                forBest(upwards, peaks).insert(0,peaks[0])
                return forBest(upwards, peaks)
            else:
                return forBest(upwards, peaks)
        except:
            return None
    elif status == "down":
        try:
            if downwards[0] > upwards[0]:
                upwards.remove(upwards[0])
                if len(downwards) == 1:
                    return forWorst(upwards, downwards)
                else:
                    temp = downwards[-1]
                    downwards.remove(downwards[-1])
                    forWorst(upwards, downwards).append(temp)
                    return forWorst(upwards, downwards)
            else:
                return forWorst(upwards, downwards)
        except:
            return None

def MonthTotalInfo(month):
    result = month_info.get(month)

    return result

def SexError(day, month, year, URD1, URD2, PZ1, PZ2):
    zeros_count = 0
    if len(str(day)) != 2:
        zeros_count += 1
    if len(str(month)) != 2:
        zeros_count += 1
    for i in str(year):
        if i == '0':
            zeros_count += 1
    for i in str(URD1):
        if i == '0':
            zeros_count += 1
    for i in str(URD2):
        if i == '0':
            zeros_count += 1
    for i in str(PZ1):
        if i == '0':
            zeros_count += 1
    for i in str(PZ2):
        if i == '0':
            zeros_count += 1

    return zeros_count

def SexTotal(day, month, year, URD1, URD2, PZ1, PZ2):
    sex_total = []
    for i in str(day):
        sex_total.append(i)
    for i in str(month):
        sex_total.append(i)
    for i in str(year):
        sex_total.append(i)
    for i in str(URD1):
        sex_total.append(i)
    for i in str(URD2):
        sex_total.append(i)
    for i in str(PZ1):
        sex_total.append(i)
    for i in str(PZ2):
        sex_total.append(i)

    sex_total = list(filter(lambda num: num != '0', sex_total))

    even_count, odd_count = 0, 0
    for num in sex_total:
        if int(num) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if even_count > odd_count:
        result = 'Женщиной'
    elif odd_count > even_count:
        result = 'Мужчиной'
    else:
        zeros = SexError(day, month, year, URD1, URD2, PZ1, PZ2)
        if zeros > 0:
            result = 'Мужчиной (с натяжкой)'
        else:
            result = 'Неизвестно какого пола'

    return result
    
def YearCycle(day, month, year, age):
    # style.use('seaborn')
    today = date.today()
    this_year = today.year

    years = []
    i = 0
    while len(years) < 9:
        new_year = this_year + i
        years.append(new_year)
        i += 1

    cycle_names = []
    for i in years:
        cycle_names.append(sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(i))))

    cycles = []
    for i in years:
        cycle = sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(i)))
        if cycle > 5:
            cycle = 10 - cycle
            cycles.append(cycle)
        else:
            cycles.append(sumNumbers(sumNumbers(sumNumbers(day) + sumNumbers(month) + sumNumbers(i))))

    plot.bar(years, cycles, color='ymcrgbkmy')
    plot.xticks(rotation=45)
    plot.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plot.title('Годичные циклы', fontweight='bold')
    plot.savefig('Graph2.png')
    plot.clf()
    plot.cla()

    return 1

# def PlanetPeriods(start, end):

def InterpretationTen(data, avg, status):
    x = [10,20,30,40,50,60,70]
    downwards = findInterceptionsDown(data,avg)
    upwards = findInterceptionsUp(data,avg)
    # print(upwards)
    # print(downwards)
    peaks = []
    for i in range(len(data)-2):
        if data[i+1] > data[i] and data[i+1] >= data[i+2]:
            if data[i+1] > avg:
                peaks.append(x[i+1])
        # elif data[i+2] > avg and data[i+2] > data[i+1]:
        elif data[i+1] > avg and data[i+1] == data[i]:
            peaks.remove(x[i])
            peaks.append(x[i+1])
        elif data[i+2] > avg and data[i+2] > data[i+1]:
            peaks.append(x[i+2])

    peaks = list(dict.fromkeys(peaks))
    # print(peaks)
    if status == "up":
        try:
            if upwards[0] > peaks[0]:
                peaks.remove(peaks[0])
                # best = forBest(upwards, peaks)
                forBest(upwards, peaks).insert(0,peaks[0])
                return forBest(upwards, peaks)
            else:
                return forBest(upwards, peaks)
        except:
            return None
    elif status == "down":
        try:
            if downwards[0] > upwards[0]:
                upwards.remove(upwards[0])
                if len(downwards) == 1:
                    return forWorst(upwards, downwards)
                else:
                    temp = downwards[-1]
                    downwards.remove(downwards[-1])
                    forWorst(upwards, downwards).append(temp)
                    return forWorst(upwards, downwards)
            else:
                return forWorst(upwards, downwards)
        except:
            return None