from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QLineEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle("Определения площади фундамента")

g1_label = QLabel("G1 - коэффициент условия работы основания ")
g1_edit = QLineEdit("")

g2_label = QLabel("G2 - коэффициент условия работы сооружения")
g2_edit = QLineEdit("")

k_label = QLabel("K - коэффициент надежности")
k_edit = QLineEdit("")

k1_label = QLabel("K1 - коэффициент развития области предельного равновесия")
k1_edit = QLineEdit("")

k2_label = QLabel("K2 - коэффициент расчетной ширины фундамента")
k2_edit = QLineEdit("")

f1_label = QLabel("F1 - угол внутреннего трения грунта φI")
f1_edit = QLineEdit("")

c_label = QLabel("C - сцепление грунта")
c_edit = QLineEdit("")

a1_label = QLabel("A1 - коэффициент формы подошвы фундамента α1")
a1_edit = QLineEdit("")

b_label = QLabel("B - коэффициент заполнения объема фундамента β")
b_edit = QLineEdit("")

q1_label = QLabel("Q1 - удельный вес воды ")
q1_edit = QLineEdit("")

q2_label = QLabel("Q2 - удельный вес грунта обратной засыпки ")
q2_edit = QLineEdit("")

q3_label = QLabel("Q3 - удельный вес грунта основания")
q3_edit = QLineEdit("")

q4_label = QLabel("Q4 - удельный вес условного фундамента")
q4_edit = QLineEdit("")

z_label = QLabel("Z - уровень воды относительно поверхности грунта")
z_edit = QLineEdit("")

h_label = QLabel("H - глубина подвала")
h_edit = QLineEdit("")

p_label = QLabel("P - вертикальная нагрузка на уровне планировки N")
p_edit = QLineEdit("")

d1_label = QLabel("D1  -глубина заложения подошвы фундамента")
d1_edit = QLineEdit("")

a2_label = QLabel("A2 - коэффициент изменения глубины заложения подошвы")
a2_edit = QLineEdit("")

m1_label = QLabel("M1 - параметр, зависимый от φII, Mγ")
m1_edit = QLineEdit("")

m2_label = QLabel("M2 - параметр, зависимый от φII, Мq")
m2_edit = QLineEdit("")

m3_label = QLabel("M3 - параметр, зависимый от φII, Мс")
m3_edit = QLineEdit("")

main_line = QVBoxLayout()
#1
col_1 = QVBoxLayout()

col_1.addWidget(g1_label)
col_1.addWidget(g1_edit)

col_1.addWidget(g2_label)
col_1.addWidget(g2_edit)

col_1.addWidget(k_label)
col_1.addWidget(k_edit)

col_1.addWidget(k1_label)
col_1.addWidget(k1_edit)

col_1.addWidget(k2_label)
col_1.addWidget(k2_edit)

col_1.addWidget(f1_label)
col_1.addWidget(f1_edit)

col_1.addWidget(c_label)
col_1.addWidget(c_edit)
#2 
col_2 = QVBoxLayout()

col_2.addWidget(a1_label)
col_2.addWidget(a1_edit)

col_2.addWidget(b_label)
col_2.addWidget(b_edit)

col_2.addWidget(q1_label)
col_2.addWidget(q1_edit)

col_2.addWidget(q2_label)
col_2.addWidget(q2_edit)

col_2.addWidget(q3_label)
col_2.addWidget(q3_edit)

col_2.addWidget(q4_label)
col_2.addWidget(q4_edit)

col_2.addWidget(z_label)
col_2.addWidget(z_edit)
#3
col_3 = QVBoxLayout()

col_3.addWidget(h_label)
col_3.addWidget(h_edit)

col_3.addWidget(p_label)
col_3.addWidget(p_edit)

col_3.addWidget(d1_label)
col_3.addWidget(d1_edit)

col_3.addWidget(a2_label)
col_3.addWidget(a2_edit)

col_3.addWidget(m1_label)
col_3.addWidget(m1_edit)

col_3.addWidget(m2_label)
col_3.addWidget(m2_edit)

col_3.addWidget(m3_label)
col_3.addWidget(m3_edit)

button = QPushButton("Расчитать")
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_2.addWidget(button)

row_1.addLayout(col_1)
row_1.addLayout(col_2)
row_1.addLayout(col_3)


main_line.addLayout(row_1)
main_line.addLayout(row_2)
window.setLayout(main_line)

def calculation():
    try:
        yv = float(q1_edit.text())
        d1 = float(d1_edit.text())
        z = float(z_edit.text())
        yf = float(q4_edit.text())
        n = float(p_edit.text())
        g1 = float(g1_edit.text())
        g2 = float(g2_edit.text())
        h = float(h_edit.text())
        k = float(k_edit.text())
        k1 = float(k1_edit.text())
        k2 = float(k2_edit.text())
        m1 = float(m1_edit.text())
        m2 = float(m2_edit.text())
        m3 = float(m3_edit.text())
        q1 = float(q1_edit.text())
        q2 = float(q2_edit.text())
        a2 = float(a2_edit.text())
        c = float(c_edit.text())

        r = g1 * g2 / k * m1 + q2 * k1 * k2 + g1 * g2 / k*(m2 * q2 * a2 * d1 + (m2 - 1) * q2 * h + m3 * c)
        hv = d1 + z
        result = n / (r + yv * hv - yf * d1)
        a = QMessageBox()
        a.setWindowTitle("Резултат")
        a.setText(str(result))
        a.exec_()
    except:
        
        a = QMessageBox()
        a.setWindowTitle("Резултат")
        a.setText("Не хватает данных")
        a.exec_()
button.clicked.connect(calculation)
window.show()
app.exec_()