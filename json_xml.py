import json
import xmltojson
import xml.etree.ElementTree as etree
from pprint import pprint

def xml_topstring(name_of_file):
    list = []
    sort_list = []
    top = []
    file = name_of_file
    #читаем файл
    tree = etree.parse(file)
    root = tree.getroot()

    for channel in root:
        for data in channel:
            for include in data:
                # print(include.tag)
                if include.tag == 'description':
                    # print(include.text)
                    list.append(include.text)
    # print(list)
    for item in list:
        sort_list = item.split()
    sort_list2 = set(sort_list)
    sort = sorted(sort_list2, key=len, reverse = True)
    # больше 6ти символов
    for key in sort:
        if len(key)>6:
            top.append(key)
    print('XML:')
    print(top[0:6])



def json_topstring(name_of_file):
    list = []
    sort_list = []
    top = []
    file = name_of_file
    #читаем файл
    with open(file, 'r', encoding='utf-8') as myfile:
        data=json.load(myfile)

    for news in data:
       for new in data[news]:
           if new=='channel':
               for description in data[news][new]:
                   if description == 'items':
                       for descriptions in data[news][new]['items']:
                           list.append(descriptions)
    for item in list:
        all = item['description']
    sort_list = all.split(' ')
    #функция сортировки
    def myFunc(e):
      return len(e)
    sort_list.sort(key=myFunc,reverse=True)

    # больше 6ти символов
    print('JSON:')
    for key in sort_list:
        if len(key)>6:
            top.append(key)
    print(top[0:6])



json_topstring('file.json')
json_topstring('file2.json')
xml_topstring('xml_file.xml')
xml_topstring('xml_file2.xml')
