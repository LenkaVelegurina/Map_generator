from PyQt5 import QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QInputDialog
from random import choice
from time import sleep
from pprint import pprint
from PyQt5.Qt import *
import os
from PIL import ImageGrab
import sys

n, m = 4, 8
s_l = ''
flag_print = False
contest_name = 'ТРАЕКТОРИЯ-ПАЗЛ'
path = os.getcwd()
path_set = path
path_default = False
d = {"Г": 0, "С": 0, "Х": 0, "Т": 0, 'l': 0}
if path[-4:] != 'SAVE':
    path += '\\SAVE'


# Проход по графу из верхнего правого угла с целью посещения всех вершин из данной компоненты связанности
def dfs(x, i, j, used):
    used[i][j] = True
    if i < n - 1 and not used[i + 1][j] and x[i + 1][j] in ['tb', 'trbl', 'tr', 'tl',
                                                            'ctr', 'ctl', 'trb', 'tbl', 'trl']:
        dfs(x, i + 1, j, used)
    if j < m - 1 and not used[i][j + 1] and x[i][j + 1] in ['rl', 'trbl', 'tl', 'bl',
                                                            'ctl', 'cbl', 'rbl', 'tbl', 'trl']:
        dfs(x, i, j + 1, used)

    if i >= 1 and not used[i - 1][j] and x[i - 1][j] in ['tb', 'trbl', 'bl', 'rb',
                                                         'cbl', 'crb', 'trb', 'rbl', 'tbl']:
        dfs(x, i - 1, j, used)
    if j >= 1 and not used[i][j - 1] and x[i][j - 1] in ['rl', 'trbl', 'tr', 'rb',
                                                         'ctr', 'crb', 'trb', 'rbl', 'trl']:
        dfs(x, i, j - 1, used)


# Поиск в графе пустых клеток
def find_clear_area(x, used):
    for i in range(n):
        for j in range(m):
            if x[i][j] == '':
                used[i][j] = True


# Проверка графа на связанность
def check_connectivity(used):
    count = 0
    for i in range(n):
        for j in range(m):
            if used[i][j]:
                count += 1
    return count == n * m


def count_elements(x):
    global d
    d = {"Г": 0, "С": 0, "Х": 0, "Т": 0, 'l': 0}
    for i in range(n):
        for j in range(m):
            if x[i][j] == 'trbl':
                d['Х'] += 1
            elif x[i][j] in ['rl', 'tb']:
                d['l'] += 1
            elif x[i][j] == '':
                continue
            elif x[i][j] in ['trb', 'rbl', 'trl', 'tbl']:
                d['Т'] += 1
            else:
                if 'c' in x[i][j]:
                    d['С'] += 1
                else:
                    d['Г'] += 1


def check_elements(parent):
    try:
        if int(parent.new_window.lineEdit_8.text()) <= d['Г'] <= int(parent.new_window.lineEdit_3.text()) and \
                int(parent.new_window.lineEdit_6.text()) <= d['С'] <= int(parent.new_window.lineEdit_4.text()) and \
                int(parent.new_window.lineEdit_10.text()) <= d['Х'] <= int(parent.new_window.lineEdit_2.text()) and \
                int(parent.new_window.lineEdit_7.text()) <= d['Т'] <= int(parent.new_window.lineEdit.text()) and \
                int(parent.new_window.lineEdit_9.text()) <= d['l'] <= int(parent.new_window.lineEdit_5.text()):
            return True
        else:
            return False
    except BaseException:
        warning = QDialog()
        warning.setLayout(QVBoxLayout())
        warning.layout().addWidget(QLabel('<h1 style="color:red">'
                                          'Количество элементов поля должно'
                                          ' задаваться числом!</h1>'))
        warning.setWindowTitle('WARNING!')
        warning.exec_()
        return None


def make_map(n=4, m=8, parent=None, s_l=''):
    def gen(n=4, m=8):
        global s_l
        a = [[''] * m for _ in range(n)]
        # Заполнение угловых клеток
        a[0][0] = choice(['rb', 'crb'])
        a[0][m - 1] = choice(['bl', 'cbl'])
        a[n - 1][0] = choice(['tr', 'ctr'])
        a[n - 1][m - 1] = choice(['tl', 'ctl'])
        # pprint(a)
        # print()

        for i in range(1, m - 2):
            # Заполнение верхней строки
            if a[0][i - 1] in ['rb', 'rbl', 'crb', 'rl']:
                a[0][i] = choice(['rbl', 'bl', 'rl', 'cbl'])
            else:
                a[0][i] = choice(['rb', 'crb'])
            # Заполнение нижней строки
            if a[n - 1][i - 1] in ['tr', 'ctr', 'trl', 'rl']:
                a[n - 1][i] = choice(['tl', 'ctl', 'trl', 'rl'])
            else:
                a[n - 1][i] = choice(['tr', 'ctr'])

        # Заполнение предпоследней клетки в верхней строке
        if a[0][m - 3] in ['rb', 'rbl', 'crb', 'rl']:
            a[0][m - 2] = choice(['rbl', 'rl'])
        else:
            a[0][m - 2] = choice(['rb', 'crb'])
        # Заполнение предпоследней клетки в нижней строке
        if a[n - 1][m - 3] in ['tr', 'ctr', 'trl', 'rl']:
            a[n - 1][m - 2] = choice(['trl', 'rl'])
        else:
            a[n - 1][m - 2] = choice(['tr', 'ctr'])
        # pprint(a)
        # print()

        for i in range(1, n - 1):
            # Заполнение левого столбца
            a[i][0] = choice(['trb', 'tb'])
            # Заполнение правого столбца
            a[i][m - 1] = choice(['tbl', 'tb'])
        # pprint(a)
        # print()

        # Заполнение центральной части карты
        for i in range(1, n - 2):
            for j in range(1, m - 2):
                if a[i][j - 1] in ['ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    if a[i - 1][j] in ['trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[i][j] = choice(['rb', 'crb'])
                    else:
                        a[i][j] = choice(['tr', 'ctr', 'trb', 'tb'])
                else:
                    if a[i - 1][j] in ['trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[i][j] = choice(['bl', 'cbl', 'rbl', 'rl'])
                    else:
                        a[i][j] = choice(['tl', 'ctl', 'tbl', 'trl', 'trbl'])
        # pprint(a)
        # print()

        # Заполнение предпоследней строки карты
        for i in range(1, m - 2):
            # Если нижняя закрыта
            if a[n - 1][i] == 'rl' or a[n - 1][i] == '':
                # Если левая закрыта
                if a[n - 2][i - 1] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[n - 3][i] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][i] = ''
                    # Если верхняя открыта
                    else:
                        a[n - 2][i] = choice(['tr', 'ctr'])
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[n - 3][i] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][i] = 'rl'
                    # Если верхняя открыта
                    else:
                        a[n - 2][i] = choice(['tl', 'ctl', 'trl'])
            # Если нижняя открыта
            else:
                # Если левая закрыта
                if a[n - 2][i - 1] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[n - 3][i] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][i] = choice(['rb', 'crb'])
                    # Если верхняя открыта
                    else:
                        a[n - 2][i] = choice(['tb', 'trb'])
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[n - 3][i] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][i] = choice(['bl', 'cbl', 'rbl'])
                    # Если верхняя открыта
                    else:
                        a[n - 2][i] = choice(['tbl', 'trbl'])
        # pprint(a)
        # print()

        # Заполнение предпоследнего столбца карты
        for i in range(1, n - 2):
            # print(i, m - 2)
            # Если правая закрыта
            if a[i][m - 1] == 'tb' or a[i][m - 1] == '':
                # Если левая закрыта
                if a[i][m - 3] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[i - 1][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[i][m - 2] = ''
                    # Если верхняя открыта
                    else:
                        a[i][m - 2] = 'tb'
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[i - 1][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[i][m - 2] = choice(['bl', 'cbl'])
                    # Если верхняя открыта
                    else:
                        a[i][m - 2] = choice(['tl', 'ctl', 'tbl'])
            # Если правая открыта
            else:
                # Если левая закрыта
                if a[i][m - 3] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[i - 1][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[i][m - 2] = choice(['rb', 'crb'])
                    # Если верхняя открыта
                    else:
                        a[i][m - 2] = choice(['tr', 'ctr', 'trb'])
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[i - 1][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[i][m - 2] = choice(['rl', 'rbl'])
                    # Если верхняя открыта
                    else:
                        a[i][m - 2] = choice(['trbl', 'trl'])
        # pprint(a)
        # print()

        # Если нижняя закрыта
        if a[n - 1][m - 2] in ['rl', '']:
            # Если правая закрыта
            if a[n - 2][m - 1] in ['tb', '']:
                # Если левая закрыта
                if a[n - 2][m - 3] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][m - 2] = ''
                    # Если верхняя открыта
                    else:
                        return False
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        return False
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = choice(['tl', 'ctl'])
            # Если правая открыта
            else:
                # Если левая закрыта
                if a[n - 2][m - 3] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        return False
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = choice(['tr', 'ctr'])
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][m - 2] = 'rl'
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = 'trl'
        # Если нижняя открыта
        else:
            # Если правая закрыта
            if a[n - 2][m - 1] in ['tb', '']:
                # Если левая закрыта
                if a[n - 2][m - 3] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        return False
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = 'tb'
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][m - 2] = choice(['bl', 'cbl'])
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = 'tbl'
            # Если правая открыта
            else:
                # Если левая закрыта
                if a[n - 2][m - 3] in ['', 'ctl', 'cbl', 'bl', 'tl', 'tb', 'tbl']:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][m - 2] = choice(['rb', 'crb'])
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = 'trb'
                # Если левая открыта
                else:
                    # Если верхняя закрыта
                    if a[n - 3][m - 2] in ['', 'trl', 'rl', 'tr', 'ctr', 'tl', 'ctl']:
                        a[n - 2][m - 2] = 'rbl'
                    # Если верхняя открыта
                    else:
                        a[n - 2][m - 2] = 'trbl'
        # pprint(a)
        # print()
        return a

    # Генерация поля происходит до тех пор, пока не будет соответствовать требуемым параметрам
    count_varieties = 0
    max_variety_number = parent.new_window.lineEdit_11.text()
    while True:
        count_varieties += 1
        try:
            int(max_variety_number)
        except BaseException:
            break
        if count_varieties == int(max_variety_number):
            return None
        x = gen(n, m)
        used = [[False] * m for _ in range(n)]
        if x:
            dfs(x, 0, 0, used)
            find_clear_area(x, used)
            count_elements(x)
            s_l.setText('Элементы поля: Г-образная линия: {}, Скруглённый поворот: {},'
                        ' X-образная линия: {}, Т-линия: {}, Прямая: {}.'. \
                        format(d['Г'], d['С'], d['Х'], d['Т'], d['l']))
            s_l.show()
            res_check = check_elements(parent)
            if check_connectivity(used) and res_check:
                break
            elif res_check is None:
                return None
    return x


def set_settings(parent):
    parent.new_window = uic.loadUi("settings.ui")
    parent.new_window.setWindowTitle("Настройки")
    # Обработка нажатия на кнопки
    parent.new_window.save_settings.clicked.connect(lambda: set_contest_name(parent))
    parent.new_window.path_button.clicked.connect(lambda: set_path(parent))


def open_settings(parent):
    parent.new_window.show()


# Настройка названия соревнования
def set_contest_name(parent):
    global contest_name
    contest_name = parent.new_window.contest_name.text()
    success = QDialog()
    success.setLayout(QVBoxLayout())
    success.layout().addWidget(QLabel('<h1 style="color:green">'
                                      'Настройки успешно сохранены!</h1>'))
    success.setWindowTitle('SUCCESS!')
    success.exec_()


# Настройка пути сохранения файлов
def set_path(parent):
    folder_name = QFileDialog.getExistingDirectory(parent, 'Open folder')
    global path
    global path_default
    if folder_name:
        path = folder_name
        path_default = True


class Generator(object):
    def __init__(self, form):
        global d
        self.form = form
        set_settings(form)
        form.setObjectName("Map_gen")
        form.setFixedSize(m * 100, n * 101 + 110)

        self.show_legend = QtWidgets.QLabel(form)
        self.show_legend.move(50, -65)
        self.show_legend.setText('')
        self.show_legend.setFixedSize(1000, 1000)

        self.save = QtWidgets.QPushButton(form)
        self.save.move(441, n * 101 + 60)
        self.save.setText('Сохранить')
        self.save.clicked.connect(self.save_img)

        self.print = QtWidgets.QPushButton(form)
        self.print.move(601, n * 101 + 60)
        self.print.setText('Печать')
        self.print.clicked.connect(self.print_img)

        self.gen = QtWidgets.QPushButton(form)
        self.gen.move(271, n * 101 + 60)
        self.gen.setText('Сгенерировать')
        self.gen.clicked.connect(self.regen)

        self.settings = QtWidgets.QPushButton(form)
        self.settings.move(100, n * 101 + 60)
        self.settings.setText('Настройки')
        self.settings.clicked.connect(lambda: open_settings(form))

    def save_img(self):
        # Делаем скриншот окна с картой
        p = window.geometry()
        bbox_section = (p.x(), p.y(), p.x() + 802, p.y() + 402)
        screen = ImageGrab.grab(bbox_section)
        x = 1
        os.chdir(path)
        # Ищем файл с наибольшим номером
        for current_dir, dirs, files in os.walk(path):
            for j in files:
                if os.access(j, os.F_OK):
                    try:
                        if j[:4] == 'line' and j[-4:] == '.jpg':
                            x = max(int(j[4:-4]) + 1, x)
                    except BaseException:
                        continue
        # Сохраняем поле и возвращаемся в исходную папку
        filename = 'line{}.jpg'.format(x)
        screen.save(filename)
        os.chdir(path_set)

    def print_img(self):
        # Сохраняем изображение
        global flag_print, d
        p = window.geometry()
        bbox_section = (p.x(), p.y(), p.x() + 802, p.y() + 402)
        screen = ImageGrab.grab(bbox_section)
        x = 1
        os.chdir(path)
        for current_dir, dirs, files in os.walk(path):
            for j in files:
                if os.access(j, os.F_OK):
                    try:
                        if j[:4] == 'line' and j[-4:] == '.jpg':
                            x = max(int(j[4:-4]) + 1, x)
                    except BaseException:
                        continue
        if not flag_print:
            flag_print = True
            filename = 'line{}.jpg'.format(x)
            screen.save(filename)
        else:
            x = x - 1
        # Печатаем изображение, написав название соревнования, номер варианта и установив альбомную ориентацию
        printer = QPrinter()
        te = QTextEdit()
        html = '<h1 align="center">{}<br>' \
               'ВАРИАНТ: {}</h1><br><img src="line{}.jpg"><br><br><br>Г-образная линия: {},' \
               ' Скруглённый поворот: {}, X-образная линия: {}, Т-линия: {}, Прямая: {}'. \
            format(contest_name, x, x, d['Г'], d['С'], d['Х'], d['Т'], d['l'])
        te.setHtml(html)
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec() == QDialog.Accepted:
            printer.setOrientation(QPrinter.Landscape)
            te.print(printer)
        os.chdir(path_set)

    def regen(self):
        global path_set
        os.chdir(path_set)
        n = 4
        m = 8
        form = self.form
        form.resize(m * 100, n * 100 + 100)

        a = make_map(n, m, form, self.show_legend)
        if a is None:
            warning = QDialog()
            warning.setLayout(QVBoxLayout())
            warning.layout().addWidget(QLabel('<h1 style="color:red">'
                                              'Не удалось сгенерировать'
                                              ' поле с данными настройками!</h1>'))
            warning.setWindowTitle('WARNING!')
            warning.exec_()
            return
        global flag_print
        flag_print = False
        # Вывод итоговой карты
        resources_path = os.getcwd()
        if resources_path[-3:] != 'RES':
            resources_path = os.getcwd() + '\\RES'
            os.chdir(resources_path)
        for i in range(n):
            for j in range(m):
                angle = 0
                pic = QtGui.QPixmap()
                if a[i][j] == '':
                    pic.load("''.jpg")
                elif a[i][j] == 'bl':
                    pic.load('bl.jpg')
                    angle = 90
                elif a[i][j] == 'cbl':
                    angle = -90
                    pic.load('cbl.jpg')
                elif a[i][j] == 'crb':
                    angle = 180
                    pic.load('crb.jpg')
                elif a[i][j] == 'ctl':
                    pic.load('ctl.jpg')
                elif a[i][j] == 'ctr':
                    pic.load('ctr.jpg')
                    angle = 90
                elif a[i][j] == 'rb':
                    pic.load('rb.jpg')
                elif a[i][j] == 'rbl':
                    pic.load('rbl.jpg')
                    angle = 90
                elif a[i][j] == 'rl':
                    pic.load('rl.jpg')
                    angle = 90
                elif a[i][j] == 'tb':
                    pic.load('tb.jpg')
                elif a[i][j] == 'tbl':
                    pic.load('tbl.jpg')
                    angle = 180
                elif a[i][j] == 'tl':
                    pic.load('tl.jpg')
                    angle = 180
                elif a[i][j] == 'tr':
                    pic.load('tr.jpg')
                    angle = -90
                elif a[i][j] == 'trb':
                    pic.load('trb.jpg')
                elif a[i][j] == 'rb':
                    pic.load('rb.jpg')
                elif a[i][j] == 'trbl':
                    pic.load('trbl.jpg')
                elif a[i][j] == 'trl':
                    pic.load('trl.jpg')
                    angle = -90
                pic = pic.scaledToHeight(100)
                t = QtGui.QTransform().rotate(angle)

                self.lbl2 = QtWidgets.QLabel(form)
                self.lbl2.move(100 * j, 100 * i)
                self.lbl2.setPixmap(pic.transformed(t))
                self.lbl2.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
                self.lbl2.show()
        os.chdir(resources_path[:-4])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Generator(window)
    window.setWindowTitle('MAP GENERATOR | v.1.4')
    window.show()
    sys.exit(app.exec_())
