import json
import xml.etree.ElementTree as etree
from collections import Counter
import re

#фукнция поиска топ 10 самых часто встречающихся в новостях слов длиннее 6 символов
def show_top(list):
    data_word = list
    str = ''
    k = 0

    for i in data_word:
        str = ''.join((str, i))

    cnt = Counter(x for x in re.findall(r'[A-z\']{6,}', str))
    all_data = cnt.most_common()

    for item in all_data:
        if k<10:
            k+=1
            print(f'№{k}: {item[0]} повторяется {item[1]} раза')


# функция парсинга XML файла
def xml_parse(file):
    list = []
    file = file
    tree = etree.parse(file)
    root = tree.getroot()
    for channel in root:
        for data in channel:
            for include in data:
                if include.tag == 'description':
                    list.append(include.text)
    print('')
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в XML:')
    show_top(list)

# функция парсинга JSON файла
def json_parse(file):
    list = []
    file = file
    with open(file, 'r', encoding='utf-8') as myfile:
        data=json.load(myfile)
    for news in data:
       for new in data[news]:
           if new=='channel':
               for description in data[news][new]:
                   if description == 'items':
                       for descriptions in data[news][new]['items']:
                           list.append(descriptions)
    data = []
    for item in list:
        data.append(item['description'])
    print('')
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в JSON:')
    show_top(data)

json_parse('file.json')
xml_parse('xml_file.xml')
