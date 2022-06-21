from pprint import pprint
from filework import filereader
from filework import filewriter
from list_editors import Contacts_List


if __name__ == '__main__':
    my_contacts_list = Contacts_List(filereader())
    my_contacts_list.name_redactor()
    my_contacts_list.phone_redactor()
    my_contacts_list.combiner()
    pprint(my_contacts_list.contacts_list)
    filewriter(my_contacts_list.contacts_list)
