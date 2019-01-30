from PyQt5 import QtGui, QtWidgets
from random import choice
from pprint import pprint
from PyQt5.Qt import *
from PIL import ImageGrab
import sys


def make_map():
    def gen():
        n, m = 4, 8
        a = [[''] * m for _ in range(n)]
        all_kinds = ['tb', 'lr', 'trbl', 'tr', 'tl', 'bl',
                     'rb', 'ctr', 'ctl', 'cbl', 'crb', 'trb',
                     'rbl', 'tbl', 'tlr']
        # Заполнение угловых клеток
        a[0][0] = choice(['rb', 'crb'])
        a[0][m - 1] = choice(['bl', 'cbl'])
        a[n - 1][0] = choice(['tr', 'ctr'])
        a[n - 1][m - 1] = choice(['tl', 'ctl'])
        pprint(a)
        print()

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
        pprint(a)
        print()

        for i in range(1, n - 1):
            # Заполнение левого столбца
            a[i][0] = choice(['trb', 'tb'])
            # Заполнение правого столбца
            a[i][m - 1] = choice(['tbl', 'tb'])
        pprint(a)
        print()

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
        pprint(a)
        print()

        # Заполнение предспоследней строки карты
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
        pprint(a)
        print()

        # Заполнение предспоследнего столбца карты
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
        pprint(a)
        print()

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
        pprint(a)
        print()
        return a

    while True:
        x = gen()
        if x:
            break
    return x


class Generator(object):
    def __init__(self, form):
        self.form = form
        form.setObjectName("Map_gen")
        form.resize(800, 500)

        self.save = QtWidgets.QPushButton(form)
        self.save.move(200, 450)
        self.save.setText('Сохранить')
        self.save.clicked.connect(self.save_img)

        self.print = QtWidgets.QPushButton(form)
        self.print.move(400, 450)
        self.print.setText('Печать')
        self.print.clicked.connect(self.print_img)

        self.gen = QtWidgets.QPushButton(form)
        self.gen.move(50, 450)
        self.gen.setText('Сгенерировать')
        self.gen.clicked.connect(self.regen)

        a = make_map()
        n = 4
        m = 8
        print(a)

        # Вывод итоговой карты
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


    def save_img(self):
        filename = 'Screenshot.jpg'
        p = window.geometry()
        bbox_section = (p.x(), p.y(), p.x() + 800, p.y() + 400)
        screen = ImageGrab.grab(bbox_section)
        screen.save(filename)

    def print_img(self):
        filename = 'Screenshot.jpg'
        p = window.geometry()
        bbox_section = (p.x(), p.y(), p.x() + 800, p.y() + 400)
        screen = ImageGrab.grab(bbox_section)
        screen.save(filename)
        printer = QPrinter()
        te = QTextEdit()
        html = '<h1 align="center">ТРАЕКТОРИЯ - ПАЗЛ<br>' \
               'ВАРИАНТ: 1</h1><br><img src="Screenshot.jpg">'
        te.setHtml(html)
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec() == QDialog.Accepted:
            printer.setOrientation(QPrinter.Landscape)
            te.print(printer)

    def regen(self):
        form = self.form
        a = make_map()
        n = 4
        m = 8
        print(a)

        # Вывод итоговой карты
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
                self.lbl2.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Generator(window)
    window.show()
    sys.exit(app.exec_())
