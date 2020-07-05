import json
import xml.etree.ElementTree as etree
from collections import Counter


def count_words(all_words):
    counter_data = Counter(all_words)
    all_data = counter_data.most_common()
    k = 0
    for item in all_data:
        if k < 10:
            k += 1
            key, value = item
            print(f'№{k}: слово "{key}" - повторяется {value} раз(а)')
    print('\n')


# фукнция поиска топ 10 самых часто встречающихся в новостях слов длиннее 6 символов
def show_top(work_text, type_file):
    finish_list = []
    for items in work_text:
        if len(items) >= 6:
            finish_list.append(items.lower())
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в {type_file}:')
    count_words(finish_list)


def xml_unification(xml_list):
    unification_words = []
    print(f'XML: {xml_list}')
    for item in xml_list:
        for words in item:
            unification_words.append(words)
    return unification_words


# функция парсинга XML файла
def xml_parse(xml_name):
    list_word = []
    tree_name = etree.parse(xml_name)
    root_name = tree_name.getroot()
    for channel in root_name:
        for data in channel:
            for include in data:
                if include.tag == 'description':
                    list_word.append(include.text.split())
    list_words = xml_unification(list_word)
    return list_words


# функция парсинга JSON файла
def json_parse(json_name):
    list_of_data = []
    with open(json_name, 'r', encoding='utf-8') as myfile:
        data_set = json.load(myfile)
    for item in data_set['rss']['channel']['items']:
        list_of_data.extend(item['description'].split())
    print(f'JSON: {list_of_data}')
    return list_of_data


def main():
    # важно, новостью считается текст в items -> description, я взял реальные тексты статей без лишних тэгов, все перепроверил и работает отлично
    json_data = json_parse('file.json')
    xml_data = xml_parse('xml_file.xml')
    show_top(json_data, 'JSON')
    show_top(xml_data, 'XML')


if __name__ == '__main__':
    main()
