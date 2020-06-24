import requests

class VK:
    name = "Tom"
    global TOKEN
    TOKEN = ''

    def get_user_list_mutual(self):
        URL_users_get = 'https://api.vk.com/method/users.get'
        URL_friends = 'https://api.vk.com/method/friends.get'
        URL_friends_getMutual = 'https://api.vk.com/method/friends.getMutual'
        params_user = {
            'access_token': TOKEN,
            'v': '5.101'
        }

        my_friends = []
        friends = requests.get(URL_friends, params_user)
        friends_list = friends.json()
        for i in friends_list:
            for k in friends_list[i]:
                if k == 'items':
                    for items in friends_list[i][k]:
                        my_friends.append(items)
        print('Список ID друзей Вконтакте:', my_friends)

        str1 = ""
        for ele in my_friends:
            ttt = '{},'.format(str(ele))
            str1 += ttt
        str1 = str1[0:-1]



        params_friends = {
            'access_token': TOKEN,
            'v': '5.101',
            'source_uid': '547302144',
            'target_uids': str1
        }

        # Поиск общих друзей в списке текущих друзей
        mutual_friends = requests.get(URL_friends_getMutual, params_friends)
        mutual_friends_list = mutual_friends.json()
        for m in mutual_friends_list:
            for j in mutual_friends_list[m]:
                # name = person.user_name(j['id'])
                abs = 547302144
                name = person.user_name(abs)
                temp_list = []
                for ids in j['common_friends']:
                    temp_name = person.user_name(ids)
                    temp_list.append(temp_name)
                a = ('У {} с id{} найдено {} общих друзей {} с ID {}'.format(name, j['id'], j['common_count'],
                                                                             temp_list, j['common_friends']))
                print(a)

        # user_info = requests.get(URL_users_get, params_user)
        # b = user_info.json()
        exit = ''
        return exit


    def user_name(self, id):
        first_name = ''
        user_id = id
        params = {
            'access_token': TOKEN,
            'v': '5.101',
            'user_ids': user_id,
            'fields': 'screen_name'
        }
        URL_users_get = 'https://api.vk.com/method/users.get'
        name = requests.get(URL_users_get, params)
        name_list = name.json()
        for i in name_list:
            for k in name_list[i]:
                for items_json in k:
                    if items_json == 'first_name':
                        first_name = k[items_json]
        return first_name

    def print(self, id):
        id_link = id
        link = 'Ссылка на профиль с id{} https://vk.com/id{}'.format(id_link, id_link)
        return link



person = VK()
print(person.get_user_list_mutual())
print(person.print(547302144))
