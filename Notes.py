import csv
import datetime as dt


class Notes:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        try:
            with open(file_name, mode='r', newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=';', escapechar='\\')
                for _ in data:
                    self.notes.append([int(_[0]),
                                       dt.datetime.strptime(_[1], '%d-%m-%Y %H:%M:%S'),
                                       _[2]])
        except:
            pass

    def __rewrite_csv__(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';', escapechar='\\')
            csv_writer.writerows(self.notes)

    def add_note(self, text):
        if len(self.notes) > 0:
            index = self.notes[-1][0] + 1
        else:
            index = 0
        self.notes.append([index, dt.datetime.today().replace(microsecond=0), text])
        with open(self.file_name, 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';', escapechar='\\')
            csv_writer.writerow(self.notes[-1])

    def print_by_dates(self, first, last):
        out = False
        i = 0
        for _ in self.notes:
            if first <= _[1] <= last:
                print(*_)
                out = True
            i += 1
        return out

    def print_by_id(self, index):
        for _ in self.notes:
            if _[0] == index:
                print(*_)
                return True
        return False

    def del_by_index(self, index):
        i = 0
        for _ in self.notes:
            if _[0] == index:
                self.notes.pop(index)
                self.__rewrite_csv__()
            i += 1
        return False

    def edit_by_index(self, index, new_text):
        i = 0
        for _ in self.notes:
            if _[0] == index:
                self.notes[index][1] = dt.datetime.today().replace(microsecond=0)
                self.notes[index][2] = new_text
                self.__rewrite_csv__()
            i += 1
        return False
