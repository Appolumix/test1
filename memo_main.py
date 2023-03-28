from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса
from memo_data import *
from memo__edit_layout import *

card_width, card_height = 600, 500 # начальные размеры окна "карточка"
frm_question = "Яблуко"
frm_right = "Apple"
frm_wrong_answer1 = "sdf"
frm_wrong_answer2 = "Ябwefw3локо"
frm_wrong_answer3 = "sdg"
shuffle(radio_list)
frm_view = QuestionView(frm, ask, radio_list[0], radio_list[1], radio_list[2], radio_list[3])


answer = radio_list[0]
wrong_answer1 = radio_list[1]
wrong_answer2 = radio_list[2]
wrong_answer3 = radio_list[3]


def show_data():
    ''' показывает на экране нужную информацию '''
    frm_view.show()


def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    if frm_view.ans_rb isChecked():
        result.setText('Правильно!')
    elif frm_view.wrans1_rb.isChecked() or frm_view.wrans2_rb.isChecked() or frm_view.wrans3_rb.isChecked():
        result.setText('Не вірно!')
    show_result

def show_random():
    ''' показать случайный вопрос '''
    global frm_card # как бы свойство окна - текущая форма с данными карточки
    # получаем случайные данные, и случайно же распределяем варианты ответов по радиокнопкам:
    frm_card = random_AnswerCheck(questions_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)
    # мы будем запускать функцию, когда окно уже есть. Так что показываем:
    frm_card.show() # загрузить нужные данные в соответствующие виджеты 
    show_question()


win_card = QWidget()
#здесь должны быть параметры окна
win_card.setWindowTitle('Memory card')
win_card.resize(card_width, card_height)
win_card.move(600, 200)
win_card.setLayout(layout_main)
# win_card.setLayout(layout_card)
win_card.show()
app.exec_()

def edit_question(index):
    ''' загружает в форму редактирования вопрос и ответы, соответствующие переданной строке '''
    #  index - это объект класса QModelIndex, см. нужные методы ниже 
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()

def add_form():
    ''' добавляет новый вопрос и предлагает его изменить '''
    questions_listmodel.insertRows() # Новый вопрос появился в данных и автоматически в списке на экране
    last = questions_listmodel.rowCount(0) - 1   # Новый вопрос - последний в списке. Найдем его позицию. 
                                                # В rowCount передаём 0, чтобы соответствовать требованиям функции:
                                                # этот параметр все равно не используется, но
    list_questions.setCurrentIndex(index) # делаем соответствующую строку списка на экране текущей
    edit_question(index)    # этот вопрос надо подгрузить в форму редактирования
                            # клика мышкой у нас тут нет, вызовем нужную функцию из программы
    txt_Question.setFocus(Qt.TabFocusReason)

def del_form():
    ''' удаляет вопрос и переключает фокус '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())  

list_questions.setModel(questions_listmodel) # связать список на экране со списком вопросов
    list_questions.clicked.connect(edit_question) # при нажатии на элемент списка будет открываться для редактирования нужный вопрос
    btn_add.clicked.connect(add_form) # соединили нажатие кнопки "новый вопрос" с функцией добавления
    btn_delete.clicked.connect(del_form)                                          