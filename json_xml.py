import json
import xml.etree.ElementTree as etree
from collections import Counter

#фукнция поиска топ 10 самых часто встречающихся в новостях слов длиннее 6 символов
def show_top(data_set):
    data_word = data_set
    k = 0
    counter_data = Counter(data_word)
    all_data = counter_data.most_common()

    for item in all_data:
        if k<10:
            k+=1
            key,value = item
            print(f'№{k}: слово "{key}" - повторятся {value} раз(а)')

# функция парсинга XML файла
def xml_parse(file_name):
    list_word = []
    finish_list = []
    file_itself = file_name
    tree_name = etree.parse(file_itself)
    root_name = tree_name.getroot()
    for channel in root_name:
        for data in channel:
            for include in data:
                if include.tag == 'description':
                    list_word.append(include.text.split())

    for items in list_word:
        for words in items:
            if len(words)>=6:
                finish_list.append(words)

    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в XML:')
    show_top(finish_list)
    print('\n')

# функция парсинга JSON файла
def json_parse(file_name):
    file_itself = file_name
    list_of_data = []
    finish_list = []

    with open(file_itself, 'r', encoding='utf-8') as myfile:
        data_set=json.load(myfile)

    for item in data_set['rss']['channel']['items']:
        list_of_data.extend(item['description'].split())

    for items in list_of_data:
        if len(items)>=6:
            finish_list.append(items)

    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в JSON:')
    show_top(finish_list)
    print('\n')

def main():
    # важно, новостью считается текст в items -> description, я взял реальные тексты статей без лишних тэгов, все перепроверил и работает отлично
    json_parse('file.json')
    xml_parse('xml_file.xml')


if __name__ == '__main__':
    main()
