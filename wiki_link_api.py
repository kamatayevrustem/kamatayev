import json
import wikipediaapi
import hashlib

class Wiki_link:

    def __init__(self, path, start):
        with open(path, 'r', encoding='utf-8') as myfile:
            self.file = json.load(myfile)
        self.start = start - 1
        self.wiki = wikipediaapi.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.file):
            raise StopIteration
        country = self.file[self.start]['name']['common']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl
        return country, country_link

    def gen(self, path):
        with open(path) as file:
            for line in file:
                line = hashlib.md5(line.encode("utf-8")).hexdigest()
                yield line.upper()


if __name__ == '__main__':
    output_file = open('countries_with_links777.txt', 'w', encoding="utf-8")
    for country, item in Wiki_link('countries.json', 0):
        output_file.write(str(country) + '\t —> \t' + str(item) + '\n')
        print('.', end='', flush=True)
    output_file.close()

    for items in Wiki_link.gen(0,'countries_with_links777.txt'):
        print(items)
