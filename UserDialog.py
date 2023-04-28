import datetime as dt


class UserDialog:
    @staticmethod
    def print_menu():
        print('\n =====',
              'Ваш как-бы-Джарвис приветствует вас.',
              'Введите один из номеров команды ниже (цифру и enter)', sep=chr(10))
        print('1 - добавить заметку',
              '2 - показать заметки (с фильтром по дате от .. до ..)',
              '3 - редактировать заметку по ID',
              '4 - удалить заметку по ID',
              '0 - выход',
              sep='\n')

    @staticmethod
    def user_choice():
        ur_cmd = input('ожидаю цифру...:')
        if not ur_cmd.isdigit():
            print('Мискузи?... Введите цифру от 0 до 4')
        elif int(ur_cmd) not in range(5):
            print('Чрезмерно сложные цифры для простой задачи. Введите цифру от 0 до 4')
        else:
            return int(ur_cmd)

    def menu_cycle(self, notes):
        exit_flag = False
        while not exit_flag:
            self.print_menu()
            ur_cmd = self.user_choice()
            if ur_cmd == 1:
                # добавить заметку
                inp = input('Введите текст заметки (или пустой ввод для отмены):')
                if len(inp) > 0:
                    notes.add_note(inp)
            elif ur_cmd == 2:
                # показать заметки по фильтру даты
                try:
                    d, m, y = input(
                        'Введите начальную дату фильтра (yyyy/mm/dd) (пустой ввод без начальной даты):').split('/')
                    min_date = dt.datetime(int(y), int(m), int(d))
                except:
                    print('(вывод без нижней границы даты)')
                    min_date = dt.datetime.min
                try:
                    d, m, y = input(
                        'Введите конечную дату фильтра (yyyy/mm/dd) (пустой ввод без конечной даты):').split('/')
                    max_date = dt.datetime(int(y), int(m), int(d))
                except:
                    print('(вывод без верхней границы даты)')
                    max_date = dt.datetime.max
                print('В запрашиваемом диапазоне найдены заметки:')
                if not notes.print_by_dates(first=min_date, last=max_date):
                    print('точнее НЕ найдены')
                input('ENTER для продолжения')

            elif ur_cmd == 3:
                # редактировать заметку по ID
                try:
                    inp_id = int(input('Введите ID заметки:'))
                    print('Заметка: ', end='')
                    if notes.print_by_id(inp_id):
                        inp = input('Введите новый текст заметки (или пустой ввод для отмены):')
                        if len(inp) == 0 or notes.edit_by_index(inp_id, inp) == False:
                            print('...осталась без изменений')
                    else:
                        print('не найдена.')
                except:
                    print('Ошибка ввода. Необходимо целое число')

            elif ur_cmd == 4:
                # удалить заметку по ID
                try:
                    inp_id = int(input('Введите ID заметки:'))
                    print('Заметка: ', end='')
                    if notes.print_by_id(inp_id):
                        inp = input('Удалить? (Y/N)')
                        if inp == 'Y' or inp == 'y':
                            notes.del_by_index(inp_id)
                    else:
                        print('не найдена.')
                except:
                    print('Ошибка ввода. Необходимо целое число')

            elif ur_cmd == 0:
                print('Наш экипаж прощается с вами и желает дальнейших успехов...')
                exit_flag = True
