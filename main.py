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
          if res.group(0) in parametr:
            parametr = parametr.split(' ')
            number_of_words = len(parametr)
            i = 0
            while i < number_of_words:
              person.insert(num_parametr+i, parametr[0+i])
              del(person[num_parametr+i+1])
              i+=1





if __name__ == '__main__':
  contacts_list = filereader()
  my_contacts_list = Contacts_List(contacts_list)
  pprint(my_contacts_list.contacts_list)
  my_contacts_list.name_redactor()
  pprint(my_contacts_list.contacts_list)