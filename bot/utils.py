import requests

lib = dict()

def GetCode(url):
    response = requests.get(url)
    try:
        doc = response.content.decode('utf-8', errors='ignore')
    except:
        doc = response.content.decode('cp1251', errors='ignore')
    return doc

def AuthorAndName(f):
    global lib
    a = f.split('\n')
    local_authors = []
    local_names = []
    name = ''
    author = ''
    for x in a:
        if 'class="list-book__link"' in x:
            y = x[:len(x) - 10]
            p = y.rfind('>')
            name = y[p + 1:]
            local_names.append(name)
        if '<a class="list-author"' in x:
            y = x[:len(x) - 10]
            p = y.rfind('>')
            author = y[p + 1:]
            local_authors.append(author)
        if (name != '') and (author != ''):
            lib[name] = author
    return local_authors, local_names

def MakeTop(local_authors, local_names, x):
    s = ''
    for i in range(0,int(x)):
        s += str(i+1) + '. ' + local_authors[i] + ' - ' + local_names[i] + '\n'
    return s

def ReturnLib():
    global lib
    f = GetCode('https://knigopoisk.org/ratings/luchshie_knigi_uzhasov')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_antiutopiya')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_realizm')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_fantastika_luchshee')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_detektivy')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_skazki')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_novella')
    AuthorAndName(f)
    f = GetCode('https://knigopoisk.org/ratings/knigi_istoricheskie_romany')
    AuthorAndName(f)
    return lib

def MakeListFromStr(s):
    a=[]
    for i in range(len(s)):
        a.append(s[i])
    return a

def CorrectMistakes(message, lib):
    if 'а' <= message[0] <= 'я':
        message = chr(ord(message[0])-32) + message[1:]
    list = MakeListFromStr(message)
    for x in lib.keys():
        list1 = MakeListFromStr(x)
        k=0
        for i in range(min(len(list),len(list1))):
            if list[i] == list1[i]:
                k+=1
            if len(list1)-k <= min(len(list),len(list1))//3 :
                message = x
    return message

def CorrectMistakesAuth(message, lib):
    s = list(message.split())
    for i in range(len(s)):
        if 'а' <= s[i][0] <= 'я':
            s[i] = chr(ord(s[i][0])-32) + s[i][1:]
    newmessage = ''
    for p in s:
        newmessage += p + ' '
    newmessage = newmessage[:len(newmessage)-1]
    list1 = MakeListFromStr(newmessage)
    for x in lib.values():
        list2 = MakeListFromStr(x)
        k=0
        for i in range(min(len(list2),len(list1))):
            if list2[i] == list1[i]:
                k+=1
            if len(list2)-k <= min(len(list2),len(list1))//3 :
                newmessage = x
    return newmessage
