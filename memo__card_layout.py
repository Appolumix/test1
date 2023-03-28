''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

# віджети, які треба буде розмістити:
menu_btn = QPushButton("Меню")
stop_btn = QPushButton("Відпочити")

# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
timer = QSpinBox()
timer.setValue(30)
# кнопка відповіді "Відповісти" / "Наступне питання"
ok_btn = QPushButton("Відповісти")
# текст питання
ask = QLabel("")
# Опиши групу перемикачів
answerGroupBox = QGroupBox("Варіанти відповідей")
answerGroup = QButtonGroup()

answer1 = QRadioButton("")
answer2 = QRadioButton("")
answer3 = QRadioButton("")
answer4 = QRadioButton("")

radio_list = [answer1, answer2, answer3, answer4]

answerGroup.addButton(answer1)
answerGroup.addButton(answer2)
answerGroup.addButton(answer3)
answerGroup.addButton(answer4)
# Опиши панень з результатами
resultGroupBox = QGroupBox("Результати")
result = QLabel("")
true_answer = QLabel("")

result_v_layout = QVBoxLayout()
result_v_layout.addWidget(result)
result_v_layout.addWidget(true_answer)

resultGroupBox.setLayout(result_v_layout)
resultGroupBox.hide()

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
v_layout1 = QVBoxLayout()
v_layout2 = QVBoxLayout()
h_layout = QHBoxLayout()

v_layout1.addWidget(answer1)
v_layout1.addWidget(answer2)

v_layout2.addWidget(answer3)
v_layout2.addWidget(answer4)

h_layout.addLayout(v_layout1)
h_layout.addLayout(v_layout2)

answerGroupBox.setLayout(h_layout)
# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
layout_card = QVBoxLayout()

card_h_layout1 = QHBoxLayout()
card_h_layout2 = QHBoxLayout()
card_h_layout3 = QHBoxLayout()
card_h_layout4 = QHBoxLayout()

card_h_layout1.addWidget(menu_btn)
card_h_layout1.addStretch(1)
card_h_layout1.addWidget(stop_btn)
card_h_layout1.addWidget(timer)
card_h_layout1.addWidget(QLabel("хвилин"))

card_h_layout2.addWidget(ask)

card_h_layout3.addWidget(answerGroupBox)
card_h_layout3.addWidget(resultGroupBox)

card_h_layout4.addWidget(ok_btn, alignment=Qt.AlignCenter, stretch=2)

layout_card.addLayout(card_h_layout1)
layout_card.addLayout(card_h_layout2)
layout_card.addLayout(card_h_layout3)
layout_card.addLayout(card_h_layout4)
def show_result():
    ''' показати панель відповідей '''
    answerGroupBox.hide()
    resultGroupBox.show()
    ok_btn.setText("Наступне питання")

def show_question():
    ''' показати панель запитань '''
    answerGroupBox.show()
    resultGroupBox.hide()
    ok_btn.setText("Відповісти")

    answerGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    answerGroup.setExclusive(True)