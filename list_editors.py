import re

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
                    number_of_words = len(parametr) - 1
                    i = 0
                    while i <= number_of_words:
                        person[i] = parametr[i]
                        i += 1

    def phone_redactor(self):
        pattern1 = r"(\+7|8)?(\s|\-)*\(?(\d{3})\)?(\s|\-)*(\d{3})(\s|\-)*(\d{2})(\s|\-)*(\d{2})"
        pattern2 = '(\()*([а-я]+)(\.)(\s)*(\d{4})(\))*'
        for person in self.contacts_list:
            for num_parametr, parametr in enumerate(person):
                person[num_parametr] = re.sub(pattern1, r'+7(\3)\5-\7-\9', parametr)
                person[num_parametr] = re.sub(pattern2, r'\2\3\5', person[num_parametr])

    def combiner(self):
        for person_num, person in enumerate(self.contacts_list):
            pattern = f'{person[0]} {person[1]}'
            for dupl_person_num, dupl_person in enumerate(self.contacts_list):
                if person_num < dupl_person_num:
                    person_text = ' '.join(dupl_person)
                    res = re.search(pattern, person_text)
                    if res != None:
                        number_of_params = len(person) - 1
                        i = 0
                        while i <= number_of_params:
                            if dupl_person[i] != '':
                                person[i] = dupl_person[i]
                            i += 1
                        self.contacts_list.remove(dupl_person)