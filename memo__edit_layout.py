from PyQt.QtWidgets import QListView, QLineEdit, QFormLayout, QPushButton, QVBoxLayout, QHBoxLayout

# Кнопки
add_question = QPushButton('Нове питання')
del_question = QPushButton('Видалити питання')
start_btn = QPushButton('Почати тренування')

# Форма для питаннь
layout_form = QFormLayout()

# Введення тексту
txt_question = QLineEdit('')
txt_answer = QLineEdit('')
txt_wrong_answer1 = QLineEdit('')
txt_wrong_answer2 = QLineEdit('')
txt_wrong_answer3 = QLineEdit('')

layout_form.addRow('', txt_question)
layout_form.addRow('Правильна відповідь:', txt_answer)
layout_form.addRow('Не правильний варіант №1', txt_wrong_answer1)
layout_form.addRow('Не правильний варіант №2', txt_wrong_answer2)
layout_form.addRow('Не правильний варіант №3', txt_wrong_answer3)

# Список питаннь
list_question_view = QListView()

layout_main = QVBoxLayout()

first_h_layout = QHBoxLayout()
second_h_layout = QHBoxLayout()
third_h_layout = QHBoxLayout()

first_h_layout.addWidget(list_question_view)
first_h_layout.addWidget(layout_form)
second_h_layout.addWidget(add_question)
second_h_layout.addWidget(del_question)
third_h_layout.addWidget(start_btn)

layout_main.assLayout(layout_form)
layout_main.addLayout(first_h_layout)
layout_main.addLayout(second_h_layout)
layout_main.addLayout(third_h_layout)