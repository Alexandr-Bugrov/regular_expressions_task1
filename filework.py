import csv

def filereader():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def filewriter(contacts_list):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list)
