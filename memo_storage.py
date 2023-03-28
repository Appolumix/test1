from memo_data import *

question1 = Question("М'яч", 'ball', 'cat', 'dog', 'first')
question2 = Question('собака', 'dog', 'cat', 'apple', 'mom')
question3 = Question("Я?", "Егор", "Антон", "Дядя Толик", "Гуль")
question4 = Question("кіт", "cat", "dog", "table", "gun")
question5 = Question('1000-...?' '7', '2', '5', '9')
question6 = Question('Що зайве?', 'собака', 'воробей',' ворона' ,'голуб')
question7 = Question("Кто делает СИИИИИИ?", "роналду", "месси", "неймар", "Хз!")
question8 = Question("Коли почалася Велика Французька революція?", "У травні 1789 року", "У червні 1759 року", "У жовтні 1767 року", "У липні 1759 року")

question_list_view = QuestionListModel
question_list_view.setItemData(question1)
question_list_view.setItemData(question2)
question_list_view.setItemData(question3)
question_list_view.setItemData(question4)
question_list_view.setItemData(question5)
question_list_view.setItemData(question6)
question_list_view.setItemData(question7)
question_list_view.setItemData(question8)