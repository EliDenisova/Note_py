import datetime as dt


class FromCmd:
    def __init__(self, promt):
        self.promt = promt
        self.exec_cmd

    def exec_cmd(self, notes):
        if self.promt[1] in ('-help', '-h', '?', '-?'):
            print('Синтаксис консольных команд:')
            print('Добавить заметку ""-add Текст_заметки""')
            print('Изменить заметку ""-edit Номер_заметки Новый_Текст_заметки""')
            print('Удалить заметку ""-delete Номер_заметки""')
            print('Вывести список заметок ""-print""')
        elif self.promt[1] == '-add':
            ss = ''.join(self.promt[2:])
            if len(ss) > 0:
                notes.add_note(ss)
                return True
            else:
                print('после -add требуется текст заметки')
                return False
        elif self.promt[1] == '-delete':
            if self.promt[2].isdigit and 0 <= int(self.promt[2]) <= len(notes.notes):
                if notes.del_by_index(int(self.promt[2])) == True:
                    print('Заметка удалена')
                    return True
            else:
                print('Заметка по номеру не найдена')
                return False
        elif self.promt[1] == '-edit':
            if self.promt[2].isdigit and 0 <= int(self.promt[2]) <= len(notes.notes):
                ss = ''.join(self.promt[3:])
                if notes.edit_by_index(int(self.promt[2]), ss) == True:
                    return True
                else:
                    print('Заметка по номеру не найдена')
                    return False
            else:
                print('Заметка по номеру не найдена')
                return False
        elif self.promt[1] == '-print':
            notes.print_by_dates(dt.datetime.min, dt.datetime.max)
        else:
            return False