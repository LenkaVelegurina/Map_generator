from PyQt5 import QtGui, QtWidgets
import sys

extra_s = 'C:\\Users\\1\\PycharmProjects\\untitled\\project_pyqt\\'


def make_map():
    from random import choice
    from pprint import pprint

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

    x = ''
    while True:
        x = gen()
        if x:
            break
    return x


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)

        a = make_map()
        n = 4
        m = 8
        print(a)
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
                self.lbl2 = QtWidgets.QLabel(Form)
                self.lbl2.move(100 * j, 100 * i)
                self.lbl2.setPixmap(pic.transformed(t))

        '''pic = QtGui.QPixmap()
        pic.load('tl.jpg')
        pic = pic.scaledToHeight(100)
        self.angle = -90

        t = QtGui.QTransform().rotate(self.angle)


        self.lbl2 = QtWidgets.QLabel(Form)
        self.lbl2.move(0, 0)
        self.lbl2.setPixmap(pic.transformed(t))
        pic2 = QtGui.QPixmap()
        pic2.load('tl.jpg')
        pic2 = pic2.scaledToHeight(100)

        self.lbl2 = QtWidgets.QLabel(Form)
        self.lbl2.move(0, 100)
        self.lbl2.setPixmap(pic2)'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
