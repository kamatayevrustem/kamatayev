#«Шпионские игры» VK API
import requests
import time
import json

class VK:
    name = "Tom"
    global TOKEN,URL_users_get,URL_friends_get,URL_groups_get,URL_groups_getById,URL_users_get,array_group, json

    TOKEN = ''
    URL_users_get = 'https://api.vk.com/method/users.get'
    URL_friends_get = 'https://api.vk.com/method/friends.get'
    URL_groups_get = 'https://api.vk.com/method/groups.get'
    URL_groups_getById = 'https://api.vk.com/method/groups.getById'
    array_group = []
    json = []


    def clear_friends(self,list):
        actually = list
        print(len(actually), 'друзей:', actually)

        for i in actually:
            params_user = {
                'user_id': i,
                'access_token': TOKEN,
                'v': '5.101',
                'count': 5
            }
            print('.')
            time.sleep(0.5)
            info = requests.get(URL_users_get, params_user)
            data = info.json()
            status = data.values()
            for getstring in status:
                for string in getstring:
                    for response in string:
                        if response == 'id':
                            id = string[response]
                        if response == 'deactivated':
                            actually.remove(int(id))
        return actually

    def start(self):
        # victim = input('Введите ID или никнейм VK жертвы: ')
        return True

    def get_id(self):
        global ida
        victim = input('Введите ID или никнейм VK жертвы: ')
        try:
            victim = int(victim)
            print("Вы ввели ID жертвы, продолжаем")
            ida = int(victim)
            print('111',ida)
        except ValueError:
            try:
                victim = victim
                params_user = {
                    'user_ids': victim,
                    'access_token': TOKEN,
                    'v': '5.101',
                }
                print('.')
                time.sleep(1)
                info = requests.get(URL_users_get, params_user)
                print(info.json())
                datas = info.json()
                # print(datas)
                for key in datas.items():
                    for item in key:
                        if item != 'response':
                            for i in item:
                                # print('проверка',i['id'])
                                ida = int(i['id'])
                                # ida = int(i['id'])
                print('222',ida)
            except ValueError:
                False
        return ida

    #Работает! получаем список друзей жертвы
    def friends(self,getid):
        id = getid
        params_user = {
            'user_id': id,
            'access_token': TOKEN,
            'v': '5.101',
            'count': 5
        }
        print('.')
        time.sleep(1)
        friends = requests.get(URL_friends_get, params_user)
        friends_list = friends.json()
        for key in friends_list.items():
            for item in key:
                for include in item:
                    if include == 'items':
                        list = item[include]
        # print(f'{len(list)} друзей пользователя id: {list}')
        list2 = person.clear_friends(list)
        print(f'У жертвы {len(list2)} живых друзей: {list2}')
        # clean_friends = clear_friends()

        return list2
        # print(f'Список друзей:{friends_list}')
        # return friends_list


    # работает! получаем список всех групп у пользователя
    def user_list_group(self,getid):
        array_user = []
        id = getid
        params_user = {
            'user_id': id,
            'access_token': TOKEN,
            'v': '5.101',
            'count': 1000,
            'fields': 'city'
        }
        print('.')
        time.sleep(1)
        group = requests.get(URL_groups_get, params_user)
        group_list = group.json()
        for key in group_list.items():
            for item in key:
                for include in item:
                    if include == 'items':
                        list = item[include]
                        for itemgroup in list:
                            array_user.append(itemgroup)
                        # print(f'1111 {list}')
        return array_user

    # работает! получаем список всех групп у пользователя
    def get_list_group(self,getid):
        global array_friends
        array_friends = []
        id = getid
        params_user = {
            'user_id': id,
            'access_token': TOKEN,
            'v': '5.101',
            'count': 10,
            'fields': 'city'
        }
        print('.')
        time.sleep(1)
        group = requests.get(URL_groups_get, params_user)
        group_list = group.json()
        for key in group_list.items():
            for item in key:
                for include in item:
                    if include == 'items':
                        list = item[include]
                        for itemgroup in list:
                            array_friends.append(itemgroup)
                        # print(f'1111 {list}')
        array_friends = set(array_friends)
        return array_friends


    def friends_group(self,all_friends):
        friends_total = all_friends
        massiv = []
        for i in friends_total:
            group = person.get_list_group(i)
            for item in group:
                massiv.append(item)
        return set(massiv)

    def exclusive_group(self,userlist,friendlist):
        users_group = userlist
        friends_group = friendlist
        exclusive_array = []
        for item in friends_group:
            if item not in users_group:
                exclusive_array.append(item)
        return exclusive_array

    def group_info(self,idgroup):
        items = idgroup
        for jam in items:
            params_user = {
                'group_ids': jam,
                'access_token': TOKEN,
                'v': '5.101',
                'fields': 'members_count'
            }
            print('.')
            time.sleep(3)
            group_info = requests.get(URL_groups_getById, params_user)
            info = group_info.json()
            for key in info.items():
                for item in key:
                    if item != 'response':
                        for i in item:
                            name = str(i['name'])
                            gid = int(i['id'])
                            members_count = int(i['members_count'])
                            # print(name,gid,members_count)
                            # raw = ''
                            raw = {"name": f'{name}', "gid": f'{gid}', "members_count": f'{members_count}'}
            json.append(raw)
            with open('groups.json', 'w', encoding="utf8") as f:
                f.write(str(json))
        print('я записал в groups.json')



person = VK()
person.start()

ids = int(person.get_id())
friend = person.friends(ids)

user_group = person.user_list_group(ids)
print(f'{len(user_group)} групп в ВК в которых состоит жертва: ', *user_group)

friends_group = person.friends_group(friend)
print(f'{len(friends_group)} групп в ВК в которых состоят друзья жертвы: ', *friends_group)

finish = person.exclusive_group(user_group, friends_group)
print(f'{len(finish)} групп в ВК в которых состоит жертва, но не состоит никто из его друзей: ', *finish)

person.group_info(finish)
# print(user_group)
