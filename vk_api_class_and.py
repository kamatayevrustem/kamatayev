import requests
import time

class VK:
    global TOKEN,URL_users_get,URL_friends_get,URL_groups_get,URL_groups_getById,URL_friends_getMutual
    TOKEN = ''
    URL_users_get = 'https://api.vk.com/method/users.get'
    URL_friends_get = 'https://api.vk.com/method/friends.get'
    URL_groups_get = 'https://api.vk.com/method/groups.get'
    URL_groups_getById = 'https://api.vk.com/method/groups.getById'
    URL_friends_getMutual = 'https://api.vk.com/method/friends.getMutual'

    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'Ссылка на профиль https://vk.com/id{}'.format(self.user_id)

    def clear_friends(self,list):
        actually = list
        print(len(actually), 'всех друзей:', actually)

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
        print(len(actually), 'всех чистки:', actually)
        return actually

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

    def __and__(self, other):
        list = []
        my_friends = []
        list.append(self.user_id)
        list.append(other.user_id)
        for i in list:
            params_user = {
                'user_id': i,
                'access_token': TOKEN,
                'v': '5.101'
            }
            print('.')
            time.sleep(0.5)
            friends = requests.get(URL_friends_get, params_user)
            friends_list = friends.json()
            for i in friends_list:
                for k in friends_list[i]:
                    if k == 'items':
                        for items in friends_list[i][k]:
                            my_friends.append(items)

        print(len(my_friends), 'друзей:', my_friends)

        # str2= user2.clear_friends(my_friends)
        strr = [2696, 18563, 35515, 37490, 43280, 55291, 63228, 65793, 73983, 83028, 84307, 92364, 96434, 101125, 101696, 104995, 108693, 110638, 118963, 144170, 160946, 161249, 173864, 176418, 184535, 189613, 194663, 215455, 221775, 226803, 246601, 267003, 277104, 305902, 333006, 335478, 392746, 420528, 423609, 707193, 907250, 997045, 1016701, 1213719, 1911904, 1999896, 2477558, 2524114, 2545986, 3378034, 4691510, 4802891, 4932876, 5751328, 6927396, 7181991, 7464821, 7507763, 9589019, 10412905, 10551398, 12104690, 12396680, 12888744, 16458409, 17036184, 23753244, 40535898, 77519068, 80572932, 146937460, 148197773, 162184085, 171690977, 353540295, 171276, 901053, 1460915, 2831856, 3938839, 4103027, 4367383, 4369754, 4591103, 4654621, 5094805, 5099643, 5165095, 5256024, 5476295, 5839561, 5888412, 6120402, 6233218, 6387109, 6675213, 6762254, 6793587, 6807103, 6807844, 7228114, 7281383, 7366510, 7654319, 7691667, 8021860, 8066679, 8179359, 8304146, 8506454, 8516933, 8621056, 8735409, 8887911, 8906792, 9248033, 9248673, 9423833, 9463791, 9523834, 9531247, 9667428, 9696101, 9703323, 9925058, 10027101, 10106083, 10257982, 10367980, 10642918, 10710702, 10788419, 10912050, 10945725, 11172375, 11183358, 11260865, 11438187, 11503911, 11551336, 11770261, 11814999, 12029217, 12078655, 12133135, 12153105, 12157798, 12260226, 12270032, 12742628, 12911298, 12919640, 12959981, 12984673, 13161790, 13164233, 13271059, 13436125, 13826174, 14192108, 14231017, 14359464, 14447427, 14479966, 14680176, 14774343, 14874187, 15073743, 15644206, 15872364, 16052805, 16096635, 16596323, 17159488, 17707890, 17805058, 18227485, 18416708, 18458602, 18465503, 18497312, 18705467, 18708565, 19393475, 19484366, 19612735, 19862840, 19947482, 19947904, 20192322, 20280352, 20358447, 20397158, 20401760, 20545928, 20577299, 20598937, 20630406, 20652580, 20827956, 20939126, 21029374, 21218224, 21292744, 21458942, 21473315, 21893233, 22045121, 22089472, 22417211, 22661481, 22789606, 23373694, 24018080, 24346037, 24507084, 24736851, 25793617, 26068696, 26111040, 26905320, 26920915, 27071731, 27385716, 27461238, 27471754, 28883110, 29134273, 29420856, 29636908, 29779660, 30416762, 30751481, 31134127, 31458207, 32365739, 34509985, 34774721, 37246313, 38308002, 39466037, 41617620, 42808931, 43429460, 47736741, 48430697, 48544699, 49595356, 49887167, 51330445, 51863700, 52924744, 53644407, 54795075, 55337784, 55515015, 56526639, 57189612, 60544554, 61741940, 62614275, 65000340, 66860509, 67306481, 67783061, 68708848, 69820297, 70328407, 72470601, 72710538, 75554532, 75883135, 82427997, 84926049, 85188014, 86291319, 86322534, 87471464, 90050365, 91390359, 91864105, 93336346, 93636121, 94213610, 94504590, 94986775, 97008058, 97593976, 99248123, 102181119, 104482029, 111294468, 112255915, 113929792, 113985916, 114319879, 114629712, 115843460, 116357078, 117407724, 118315935, 122524999, 124119928, 125776255, 129110803, 131669626, 132815942, 133280468, 133800950, 134555430, 135631443, 136590976, 137338648, 137866836, 138597556, 139304988, 139315663, 139834940, 140368169, 141835911, 141968284, 142467892, 143222701, 143662946, 144480916, 149318721, 149674298, 150757917, 151872268, 152110062, 155806308, 157027961, 161490950, 161632645, 163368372, 163690596, 166328792, 166596109, 167911904, 168273182, 177602857, 182204159, 183872551, 185313876, 186517930, 188861205, 190146675, 196952650, 200543624, 202797122, 210096067, 210688997, 211031044, 214489040, 215501253, 215767124, 219049430, 219104579, 222204952, 223690935, 223821391, 223888938, 230242787, 230249414, 232729684, 233227611, 234433611, 237145345, 237436257, 242600221, 242849425, 245563622, 246515944, 246521687, 247018756, 252962411, 257544431, 260380152, 262827486, 263556115, 264281605, 265053565, 266413216, 269818213, 270825265, 272151309, 280552667, 282798492, 286582824, 290846549, 292899285, 293791856, 294999277, 298513720, 318667265, 321393328, 325597690, 329977974, 331549150, 332797728, 336195237, 345794677, 346225397, 353156132, 354727459, 364989508, 366807312, 368255260, 368520663, 371854414, 376577103, 381190557, 381652314, 387154864, 388047972, 388470030, 401831913, 405475879, 407903371, 409875308, 411798369, 425793860, 435169782, 438609721, 439027043, 443235718, 449901409, 519053115, 521090176, 526392078, 546727044, 560236133, 566249935, 588603433]

        str2 = ''
        for ele in strr:
            ttt = '{},'.format(int(ele))
            str2 += ttt
        str2 = str2[0:-1]

        params_mutualfriends = {
            'access_token': TOKEN,
            'v': '5.101',
            'target_uids': str2
        }
        # Поиск общих друзей в списке текущих друзей
        print('Поиск общих друзей в списке текущих друзей')
        time.sleep(1)
        print('....')
        mutual_friends = requests.post(URL_friends_getMutual, params_mutualfriends)
        print(mutual_friends.text)
        mutual_friends_list = mutual_friends.json()
        print(f'1: {mutual_friends_list}')
        for m in mutual_friends_list:
            for j in mutual_friends_list[m]:
                print(j)
                name = user1.user_name(j['id'])
                abs = 547302144
                name = user1.user_name(abs)
                temp_list = []
                for ids in j['common_friends']:
                    temp_name = VK.user_name(ids)
                    temp_list.append(temp_name)
                    print(',')
                a = ('У {} с id{} найдено {} общих друзей {} с ID {}'.format(name, j['id'], j['common_count'],
                                                                             temp_list, j['common_friends']))
                print(a)
        user_info = requests.get(URL_users_get, params_user)
        b = user_info.json()
        return b

user1 = VK(234235)
user2 = VK(3435523)

#создали пользователей
mutal_user_list = user1 & user2
print(mutal_user_list)

print(user1)
