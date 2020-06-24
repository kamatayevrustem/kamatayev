import requests
import time
import json


class VK:

    def start(self):
        token = input('Введите TOKEN: ')
        ids = int(person.get_id(token))
        friend = person.friends(ids, token)
        user_group = person.user_list_group(ids, token)
        print(f'{len(user_group)} групп в ВК в которых состоит жертва: ', )
        print(*user_group)
        friends_group = person.friends_group(friend, token)
        len_friends = len(friends_group)
        print(f'{len_friends} групп в ВК в которых состоят друзья жертвы: ')
        print(*friends_group)
        finish = person.exclusive_group(user_group, friends_group)
        print(f'{len(finish)} групп в ВК жертвы, внутри нету друзей: ')
        print(*finish)
        person.group_info(finish, token)
        return True

    def clear_friends(self, list, token):
        actually = list
        TOKEN = token
        print(len(actually), 'друзей:', actually)
        for i in actually:
            params_user = {
                'user_id': i,
                'access_token': TOKEN,
                'v': '5.101',
            }
            URL_users_get = 'https://api.vk.com/method/users.get'
            print('.')
            print('clear_friends')
            time.sleep(1)
            repeat = True
            while repeat:
                info = requests.get(URL_users_get, params_user)
                data = info.json()
                # status = data.values()
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

    def get_id(self, token):
        TOKEN = token
        global ida
        victim = input('Введите ID или никнейм VK жертвы: ')
        try:
            victim = int(victim)
            print("Вы ввели ID жертвы, продолжаем")
            ida = int(victim)
        except ValueError:
            try:
                victim = victim
                params_user = {
                    'user_ids': victim,
                    'access_token': TOKEN,
                    'v': '5.101',
                }
                URL_users_get = 'https://api.vk.com/method/users.get'
                print('.')
                print('получил ID')
                info = requests.get(URL_users_get, params_user)
                print(info.json())
                datas = info.json()
                for key in datas.items():
                    for item in key:
                        if item != 'response':
                            for i in item:
                                ida = int(i['id'])
            except ValueError:
                False
        return ida

    def friends(self, getid, token):
        id_friends = getid
        TOKEN = token
        params_user = {
            'user_id': id_friends,
            'access_token': TOKEN,
            'v': '5.101'

        }
        URL_friends_get = 'https://api.vk.com/method/friends.get'
        print('.')
        print('получаю список друзей')
        repeat = True
        while repeat:
            friends = requests.get(URL_friends_get, params_user)
            friends_list = friends.json()
            for key in friends_list.items():
                for item in key:
                    for include in item:
                        if include == 'items':
                            list = item[include]
            list2 = person.clear_friends(list, TOKEN)
            print(f'У жертвы {len(list2)} живых друзей: {list2}')
            if 'error' in friends_list and 'error_code' in \
                    friends_list['error'] and \
                    friends_list['error']['error_code'] == 6:
                time.sleep(1)
            else:
                repeat = False
        return list2

    def user_list_group(self, getid, token):
        array_user = []
        id = getid
        TOKEN = token
        params_user = {
            'user_id': id,
            'access_token': TOKEN,
            'v': '5.101',
            'fields': 'city'
        }
        URL_groups_get = 'https://api.vk.com/method/groups.get'
        print('.')
        print('получаю группы жертвы')
        repeat = True
        while repeat:
            group = requests.get(URL_groups_get, params_user)
            group_list = group.json()
            for key in group_list.items():
                for item in key:
                    for include in item:
                        if include == 'items':
                            list = item[include]
                            for item_group in list:
                                print('1: ', type(item_group))
                                array_user.append(item_group)
            if 'error' in group_list and 'error_code' \
                    in group_list['error'] and \
                    group_list['error']['error_code'] == 6:
                time.sleep(1)
            else:
                repeat = False
        return array_user

    def get_list_group(self, getid, token):
        # global array_friends
        array_friends = []
        id = getid
        TOKEN = token
        params_user = {
            'user_id': id,
            'access_token': TOKEN,
            'v': '5.101',
            'fields': 'city'
        }
        URL_groups_get = 'https://api.vk.com/method/groups.get'
        print('.')
        print('получаю группы друзей')
        repeat = True
        while repeat:
            group = requests.get(URL_groups_get, params_user)
            group_list = group.json()
            for key in group_list.items():
                for item in key:
                    for include in item:
                        if include == 'items':
                            list = item[include]
                            for item_group in list:
                                print('2: ', type(item_group), item_group)
                                print(type(array_friends), array_friends)
                                array_friends.append(item_group)
            array_friends = set(array_friends)
            if 'error' in group_list and 'error_code' \
                    in group_list['error'] and \
                    group_list['error']['error_code'] == 6:
                time.sleep(1)
            else:
                repeat = False
        return array_friends

    def friends_group(self, all_friends, token):
        friends_total = all_friends
        TOKEN = token
        massiv = []
        for i in friends_total:
            group = person.get_list_group(i, TOKEN)
            for item in group:
                massiv.append(item)
        return set(massiv)

    def exclusive_group(self, userlist, friendlist):
        users_group = userlist
        friends_group = friendlist
        exclusive_array = []
        for item in friends_group:
            if item in users_group:
                print(f'Уникальная группа: {item}')
                exclusive_array.append(item)
        return exclusive_array

    def group_info(self, idgroup, token):
        items = idgroup
        TOKEN = token
        json = []
        for jam in items:
            params_user = {
                'group_ids': jam,
                'access_token': TOKEN,
                'v': '5.101',
                'fields': 'members_count'
            }
            URL_groups_getById = 'https://api.vk.com/method/groups.getById'
            print('.')
            print('получаю инфу по группе, красивый экспорт')
            repeat = True
            while repeat:
                group_info = requests.get(URL_groups_getById, params_user)
                info = group_info.json()
                for key in info.items():
                    for item in key:
                        if item != 'response':
                            for i in item:
                                name = i['name']
                                gid = int(i['id'])
                                members_count = int(i['members_count'])
                                # print(name,gid,members_count)
                                # raw = ''
                                raw = {"name": f'{name}', "gid": f'{gid}',
                                       "members_count": f'{members_count}'}
                json.append(raw)
                with open('groups.json', 'w', encoding="utf8") as f:
                    f.write(str(json))

                if 'error' in info and 'error_code' \
                        in info['error'] and info['error']['error_code'] == 6:
                    time.sleep(1)
                else:
                    repeat = False
        print('я записал в groups.json')


person = VK()
person.start()
