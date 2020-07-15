class Contact(object):

    def __init__(self, first_name, last_name, phone_number, favorite_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact

        self.additional_info_args_list = []
        for a in args:
            self.additional_info_args_list.append(a)

        self.additional_info_kwargs_dict = {}
        for item_name, item_value in kwargs.items():
            self.additional_info_kwargs_dict[item_name] = item_value

    def __str__(self):
        if self.favorite_contact:
            favorite_contact_ru = 'да'
        else:
            favorite_contact_ru = 'нет'

        return str(
            "Имя: " + self.first_name + "\n" +
            "Фамилия: " + self.last_name + "\n" +
            "Телефон: " + self.phone_number + "\n" +
            "В избранных: " + favorite_contact_ru + "\n" +
            "Дополнительная информация: " + "\n" +
            "\t" + '\n\t'.join(self.additional_info_args_list) + "\n" +
            "\t" + "\n\t".join('{}: {}'.format(item_name, item_value) for item_name, item_value
                               in sorted(self.additional_info_kwargs_dict.items()))
            )


class PhoneBook:

    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name

# Вывод контактов из телефонной книги
    def get_contacts(phonebook):
        contacts = []
        for contact in phonebook:
            contacts.append(contact)
        return contacts

# Добавление нового контакта
    def create_contact(contact, phonebook):
        phonebook = phonebook.append(contact)
        return phonebook

# Удаление контакта по номеру телефона
    def delete_contact_by_number(phone_number, phonebook):
        if contact.__dict__['phone_number'] == phone_number:
            phonebook.remove(contact)
        return phonebook

# Поиск всех избранных номеров
    def get_favorite_contacts(phonebook):
        favorite_contacts = []
        for contact in phonebook:
            if contact.__dict__['favorite_contact']:
                favorite_contacts.append(contact)
        return favorite_contacts

# Поиск контакта по имени и фамилии
    def get_contact_by_name(phonebook, first_name, last_name):
        found_contacts = []
        for contact in phonebook:
            if contact.__dict__['first_name'] == first_name and (contact.__dict__)['last_name'] == last_name:
                found_contacts.append(contact)
        return found_contacts


jhon = Contact('Jhon', 'Smith', '+71234567809', True, 'Moscow, Tverskaya, 1',
               '+79000000000', 'engineer', telegram='@jhony', email='jhony@smith.com')

cathreen = Contact('Cathreen', 'Black', '+70001112222', False, 'Tula, Lenina, 1',
                   '+79555555555', 'doctor', telegram='@cath', email='cath@black.com')

duke = Contact('Duke', 'Green', '+79998887766', False, 'Orel, Tvardovskogo, 100',
               '+77777777777', 'manager', telegram='@duke', email='duke@mail.com')


work_phonebook = []
PhoneBook.create_contact(jhon, work_phonebook)
PhoneBook.create_contact(cathreen, work_phonebook)
PhoneBook.create_contact(duke, work_phonebook)

print('=' * 50)
print('Список всех контактов:')

contacts = PhoneBook.get_contacts(work_phonebook)
for contact in contacts:
    print(contact)

print('=' * 50)
print('Список контактов после удаления по номеру телефона:')

for contact in contacts:
    PhoneBook.delete_contact_by_number('+70001112222', work_phonebook)

contacts = PhoneBook.get_contacts(work_phonebook)
for contact in contacts:
    print(contact)

print('=' * 50)
print('Избранные контакты:')

favorite_contacts = PhoneBook.get_favorite_contacts(work_phonebook)
for contact in favorite_contacts:
    print(contact)

print('=' * 50)
print('Найденный по имени и фамилии контакт:')

found_contacts = PhoneBook.get_contact_by_name(work_phonebook, 'Duke', 'Green')
for contact in found_contacts:
    print(contact)
