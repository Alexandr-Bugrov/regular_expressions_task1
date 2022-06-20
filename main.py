from pprint import pprint
import csv
import re


def filereader():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


class Contacts_List:
    def __init__(self, contacts_list):
        self.contacts_list = contacts_list

    def name_redactor(self):
        pattern = r"([А-Я][а-я]+)(\ )([А-Я][а-я]+)(\ )*([А-Я][а-я]+)*"
        for person in self.contacts_list:
            for num_parametr, parametr in enumerate(person):
                res = re.search(pattern, parametr)
                if res != None:
                    parametr = parametr.split(' ')
                    number_of_words = len(parametr)
                    i = 0
                    while i < number_of_words:
                        person.insert(num_parametr+i, parametr[0+i])
                        del(person[num_parametr+i+1])
                        i+=1

    def phone_redactor(self):
        pattern1 = r"(\+7|8)?(\s|\-)*\(?(\d{3})\)?(\s|\-)*(\d{3})(\s|\-)*(\d{2})(\s|\-)*(\d{2})"
        pattern2 = '(\()*([а-я]+)(\.)(\s)*(\d{4})(\))*'
        for person in self.contacts_list:
            for num_parametr, parametr in enumerate(person):
                person[num_parametr] = re.sub(pattern1, r'+7(\3)\5-\7-\9', parametr)
                person[num_parametr] = re.sub(pattern2, r'\2\3\5', person[num_parametr])








if __name__ == '__main__':
    my_contacts_list = Contacts_List(filereader())
    pprint(my_contacts_list.contacts_list)
    my_contacts_list.name_redactor()
    my_contacts_list.phone_redactor()
    pprint(my_contacts_list.contacts_list)

