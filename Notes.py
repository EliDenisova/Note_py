import csv
import datetime as dt
import sys


class Notes():
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        try:
            with open(file_name, mode='r', newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=';', escapechar='\\')
                for _ in data:
                    self.notes.append([dt.datetime.strptime
                                       (_[0], '%Y-%m-%d %H:%M:%S'), _[1]])
        except:
            pass

    def __rewrite_csv__(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';', escapechar='\\')
            csv_writer.writerows(self.notes)

    def add_note(self, text):
        self.notes.append([dt.datetime.today().replace(microsecond=0), text])
        with open(self.file_name, 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';', escapechar='\\')
            csv_writer.writerow(self.notes[-1])

    def filter_by_dates(self, first, last):
        i = 0
        out = []
        for _ in self.notes:
            if first <= _[0] <= last:
                out.append([(i), _[0], _[1]])
            i += 1
        return out

    def print_by_dates(self, first, last):
        i = 0
        out = False
        for _ in self.notes:
            if first <= _[0] <= last:
                print(i, str(_[0]), _[1])
                out = True
            i += 1
        return out

    def print_by_id(self, index):
        if 0 <= index <= len(self.notes):
            print(index, str(self.notes[index][0]), self.notes[index][1])
            return True
        else:
            return False

    def del_by_index(self, index):
        if 0 <= index <= len(self.notes):
            self.notes.pop(index)
            self.__rewrite_csv__()
            return True
        else:
            return False

    def edit_by_index(self, index, new_text):
        if 0 <= index <= len(self.notes) and len(new_text) > 0:
            self.notes[index][0] = dt.datetime.today().replace(microsecond=0)
            self.notes[index][1] = new_text
            self.__rewrite_csv__()
            return True
        else:
            return False




