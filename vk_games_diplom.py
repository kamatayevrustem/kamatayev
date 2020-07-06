import requests
import time
import json


class VK:

    # начало программы
    def start(self):
        token = input('Введите TOKEN: ')
        ids = int(person.get_id(token))
        friend = person.friends(ids, token)
        user_group = person.get_list_group(ids, token)
        print(f'\n{len(user_group)} групп в ВК в которых состоит жертва: ', )
        # print(*user_group)
        friends_group = person.friends_group(friend, token)
        len_friends = len(friends_group)
        print(f'\n{len_friends} групп в ВК в которых состоят друзья жертвы: ')
        # print(*friends_group)
        finish = person.exclusive_group(user_group, friends_group)
        print(f'\n{len(finish)} групп в ВК в которых состоит жертва, '
              f'но не состоит никто из его друзей: ')
        # print(*finish)
        person.group_info(finish, token)
        return True

    # функция чистки списка с друзьями от удаленных и забаненных
    def clear_friends(self, actually, TOKEN):
        print(len(actually), 'друзей у жертвы:')
        for i in actually:
            params_user = {
                'user_id': i,
                'access_token': TOKEN,
                'v': '5.101',
            }
            URL_users_get = 'https://api.vk.com/method/users.get'
            print('.')
            # print('clear_friends')
            # time.sleep(1)
            repeat = True
            while repeat:
                info = requests.get(URL_users_get, params_user)
                data = info.json()
                try:
                    for item in data['response']:
                        if 'deactivated' in item:
                            response_id = item['id']
                            actually.remove(int(response_id))
                except KeyError:
                    print('..')
                except Exception:
                    print('..')

                if 'error' in data and 'error_code' in data['error'] \
                        and data['error']['error_code'] == 6:
                    time.sleep(1)
                else:
                    repeat = False
        return actually

    # получение ID жертвы, если введен никнейм, то переводив в ID
    def get_id(self, TOKEN):
        victim = input('Введите ID или никнейм VK жертвы: ')
        if victim.isdigit() == True:
            print("Вы ввели ID жертвы, продолжаем")
        else:
            params_user = {
                'user_ids': victim,
                'access_token': TOKEN,
                'v': '5.101',
            }
            URL_users_get = 'https://api.vk.com/method/users.get'
            print('. получил ID по никнейму')
            info = requests.get(URL_users_get, params_user)
            dataa = info.json()
            for item in dataa['response']:
                victim = int(item['id'])
                print(victim)
        return victim

    # фукнция получения списка друзей жертвы
    def friends(self, id_friends, TOKEN):
        params_user = {
            'user_id': id_friends,
            'access_token': TOKEN,
            'v': '5.101'
        }
        URL_friends_get = 'https://api.vk.com/method/friends.get'
        print('.')
        # print('получаю список друзей')
        time.sleep(1)
        friends = requests.get(URL_friends_get, params_user)
        friends_list = friends.json()
        for key in friends_list.items():
            for item in key:
                for include in item:
                    if include == 'items':
                        list = item[include]
        list_finish = person.clear_friends(list, TOKEN)
        # print(f'У жертвы {len(list2)} живых друзей: {list2}')
        return list_finish

    # получение списка групп
    def get_list_group(self, guid, TOKEN):
        array_friends = []
        params_user = {
            'user_id': guid,
            'access_token': TOKEN,
            'v': '5.101',
            'fields': 'city'
        }
        URL_groups_get = 'https://api.vk.com/method/groups.get'
        print('.')
        # print('получаю список групп')
        repeat = True
        while repeat:
            time.sleep(0.3)
            group = requests.get(URL_groups_get, params_user)
            group_list = group.json()
            try:
                for item in group_list['response']['items']:
                    array_friends.append(item)
            except:
                print('..')
            array_friends = set(array_friends)
            if 'error' in group_list and 'error_code' \
                    in group_list['error'] and \
                    group_list['error']['error_code'] == 6:
                time.sleep(1)
            else:
                repeat = False
        return array_friends

    # получаем список групп друзей
    def friends_group(self, friends_total, TOKEN):
        groups = []
        for i in friends_total:
            group = person.get_list_group(i, TOKEN)
            for item in group:
                groups.append(item)
        return set(groups)

    # функция отбора групп, в которых не состоят друзья
    def exclusive_group(self, users_group, friends_group):
        exclusive_array = []
        for item in friends_group:
            if item in users_group:
                users_group.remove(item)
        return users_group

    # информация о группе, точечная выгрузка
    def group_info(self, items, TOKEN):
        json_list = []
        for jam in items:
            params_user = {
                'group_ids': jam,
                'access_token': TOKEN,
                'v': '5.101',
                'fields': 'members_count'
            }
            URL_groups_getById = 'https://api.vk.com/method/groups.getById'
            print('.')
            time.sleep(0.3)
            group_info = requests.get(URL_groups_getById, params_user)
            info = group_info.json()
            # print(f'group_info: {info}')
            for item in info['response']:
                name = item['name']
                gid = item['id']
                members_count = item['members_count']
                raw = {"name": f'{name}', "gid": f'{gid}',
                       "members_count": f'{members_count}'}
                json_list.append(raw)
        with open('groups.json', 'w', encoding="utf8") as f:
            f.write(str(json_list))
        print('я записал в groups.json')


person = VK()
person.start()
