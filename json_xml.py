# подключаем библиотеки Python
import json
import xml.etree.ElementTree as etree

# функция определения длины слова
def len_word(e):
  return len(e)

# функция сортировки и вывод ТОП слов по длине
def show_top(list):
    top = []
    data = list
    data_list=[]
    str1 = ""
    k = 1
    for item in data:
        str1+=item
    sort_list = str1.split(' ')
    sort_list = set(sort_list)
    sort_list = sorted(sort_list,key=len_word,reverse=True)

    six_word = sort_list[0:10]
    for count in six_word:
        if len(count)>6:
            print(f'{k}:', count)
            k+=1

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
    print(f'ТОП 10 длинных слов в XML файле:')
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
    print(f'ТОП 10 длинных слов в JSON файле:')
    show_top(data)

json_parse('file.json')
xml_parse('xml_file.xml')
