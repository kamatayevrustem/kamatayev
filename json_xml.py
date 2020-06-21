import json
import xml.etree.ElementTree as etree
from collections import Counter
import re

#фукнция поиска топ 10 самых часто встречающихся в новостях слов длиннее 6 символов
def show_top(list):
    data_word = list
    list_finish = []
    k = 0
    for i in data_word:
        list_finish.extend(i)
    list_finish2 = ''.join(list_finish)
    cnt = Counter(x for x in re.findall(r'[A-z\']{6,}', list_finish2))
    all_data = cnt.most_common()
    for item in all_data:
        if k<10:
            k+=1
            print(f'№{k}: {item[0]} повторяется {item[1]} раза')

# функция парсинга XML файла
def xml_parse(file):
    list_word = []
    file_name = file
    tree_name = etree.parse(file_name)
    root_name = tree_name.getroot()
    for channel in root_name:
        for data in channel:
            for include in data:
                if include.tag == 'description':
                    list_word.append(include.text)
    print('')
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в XML:')
    show_top(list_word)


# функция парсинга JSON файла
def json_parse(file):
    list_word = []
    file_name = file
    with open(file_name, 'r', encoding='utf-8') as myfile:
        data_set=json.load(myfile)
    for news in data_set:
       for new in data_set[news]:
           if new=='channel':
               for description in data_set[news][new]:
                   if description == 'items':
                       for descriptions in data_set[news][new]['items']:
                           list_word.append(descriptions['description'])
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в JSON:')
    show_top(list_word)

json_parse('file.json')
xml_parse('xml_file.xml')



# Результат программы:
# D:\Anaconda3\python.exe "C:/Users/Рустем/Desktop/PYTHON/изучение/10 Работа с JSON и XML/json_full3.py"
# Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в JSON:
# №1: Wilderness повторяется 23 раза
# №2: Travel повторяется 17 раза
# №3: Protea повторяется 15 раза
# №4: Safaris повторяется 13 раза
# №5: Marriott повторяется 12 раза
# №6: International повторяется 9 раза
# №7: Belmond повторяется 7 раза
# №8: Hotels повторяется 7 раза
# №9: Anantara повторяется 7 раза
# №10: Africa повторяется 6 раза
#
# Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в XML:
# №1: Wilderness повторяется 23 раза
# №2: Travel повторяется 17 раза
# №3: Protea повторяется 15 раза
# №4: Safaris повторяется 13 раза
# №5: Marriott повторяется 12 раза
# №6: International повторяется 9 раза
# №7: Belmond повторяется 7 раза
# №8: Hotels повторяется 7 раза
# №9: Anantara повторяется 7 раза
# №10: Africa повторяется 6 раза
#
# Process finished with exit code 0
