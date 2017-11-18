import random

class Fishes:
    pass

class Bears:
    def __init__(self):
        self.sum = 0

river = []
empty = 0

def ecosystem(length, bear_proc, fish_proc):
    global empty
    global river
    kol_bears = int(bear_proc * 0.01 * length)
    kol_fishes = int(fish_proc * 0.01 * length)
    empty = length - kol_bears - kol_fishes
    for i in range(kol_fishes):
        river.append(Fishes())
    for i in range(kol_bears):
        river.append(Bears())
    for i in range(empty):
        river.append(None)
    random.shuffle(river)

def walking():
    global empty
    global river
    next_step = True
    for i in range(len(river)):
        if next_step:
            if type(river[i]) == Bears:
                next_step = bears_move(i)
            elif type(river[i]) == Fishes:
                next_step = fishes_move(i)
        else:
            next_step = True

def new_index():
    global empty
    global river
    if empty > 0:
        k = random.randint(1, empty)
        m = 0
        for i in range(len(river)):
            if river[i] is None:
                m += 1
                if m == k:
                    return i
    else:
        return -1

def new_animals(object):
    global empty
    global river
    x = new_index()
    if x != -1:
        if object == 'b':
            river[x] = Bears()
        else:
            river[x] = Fishes()
        empty -= 1

def bears_move(i):
    global bad_days
    global empty
    global river
    if i == 0:
        step = random.randint(0, 1)
    elif i == len(river) - 1:
        step = random.randint(-1, 0)
    else:
        step = random.randint(-1, 1)
    next_step = True
    if step == 1: next_step = False
    if step == 0:
        river[i].sum += 1
        if river[i].sum >= bad_days:
            river[i] = None
            empty += 1
    else:
        if type(river[i + step]) == Fishes:
            river[i + step] = Bears()
            river[i] = None
            empty += 1
        elif type(river[i + step]) == Bears:
            new_animals('b')
            river[i].sum += 1
            if river[i].sum >= bad_days:
                river[i] = None
                empty += 1
            next_step = True
        else:
            summa = river[i].sum
            river[i + step] = Bears()
            river[i] = None
            river[i + step].sum = summa + 1
            if river[i + step].sum >= bad_days:
                river[i + step] = None
                empty += 1
    return next_step

def fishes_move(i):
    global bad_days
    global empty
    global river
    if i == 0:
        step = random.randint(0, 1)
    elif i == len(river) - 1:
        step = random.randint(-1, 0)
    else:
        step = random.randint(-1, 1)
    next_step = True
    if step == 1: next_step = False
    if step != 0:
        if type(river[i + step]) == Fishes:
            new_animals('f')
        elif type(river[i + step]) == Bears:
            river[i] = None
            empty += 1
            river[i + step].sum = 0
            next_step = True
        else:
            river[i] = None
            river[i + step] = Fishes()
    return next_step

length = int(input('Введите длину реки: '))
bear_proc = int(input('Процент медведей: '))
fish_proc = int(input('Процент рыб: '))
bad_days = int(input('Количество "безрыбных" дней для медведя: '))
kol_steps = int(input('Количество дней: '))
ecosystem(length, bear_proc, fish_proc)

for i in range(kol_steps):
    s = ''
    for j in range(length):
        if type(river[j]) == Bears:
            s += 'B'
        elif type(river[j]) == Fishes:
            s += 'F'
        else:
            s += '-'
    print(s)
    walking()
