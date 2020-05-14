import os
import requests
import datetime
import yadisk
import time


def translate_it(language_first, language_second, dir_file, dir_result):
    API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    URL_lang_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    from_lang = language_first
    y = yadisk.YaDisk(token='AgAAAAANkH7YAAZW0kz95Ip-SktyuoPYa_LsIl8')
    to_lang = language_second
    path_file = dir_file
    result_file = dir_result
    files = os.listdir(path_file)

    for i in files:
        if 'txt' in i:
            print(f'Текстовый файл сейчас переводится: {i}')
            x = datetime.datetime.now()
            timename = f'{x.hour}-{x.minute}-{x.second}-{x.microsecond}'
            full_path = '{}/{}'.format(path_file,i)
            print(f'Работаем с файлом: {full_path}')

            with open(full_path, 'r', encoding="utf8") as f:
                file = f.read()
                print(file)

            # параметры для определения языка с которого будет перевод:
            lang_detect = {
                'key': API_KEY,
                'text': file,
                'hint': 'en,ru,fr'
            }
            detect = requests.get(URL_lang_detect, params=lang_detect)
            detect_lang = detect.json()
            from_lang = detect_lang["lang"]
            print(f'Языка с которого будет перевод: {from_lang}')

            # параметры перевода
            params = {
                'key': API_KEY,
                'text': file,
                'lang': '{}-{}'.format(from_lang, to_lang),
            }
            response = requests.get(URL, params=params)
            json_ = response.json()
            translate = ''.join(json_['text'])
            print(translate)

            # сохранение в файл
            full_path_wfile = f'{result_file}-{from_lang}-{to_lang}-{timename}.txt'
            print('\n\n\n')

            with open(full_path_wfile, 'w', encoding="utf8") as f:
                f.write(translate)

            time.sleep(10)

            with open(full_path_wfile, "rb") as f:
                disk = f'/{from_lang}-{to_lang}-{timename}.txt'
                y.upload(f, disk)

    return response



if __name__ == '__main__':
    language_first = 'no'
    language_second = 'ru'
    dir_file = ("C:/Users/Рустем/Desktop/PYTHON/изучение/11 http/")
    dir_result = ("C:/Users/Рустем/Desktop/PYTHON/изучение/11 http/result")
    translate_it(language_first, language_second, dir_file, dir_result)

