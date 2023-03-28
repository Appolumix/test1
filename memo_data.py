class Question():
    def __init__ (self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer 
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.correct = 0
        self.attems = 0
        self.shift = True

    def got_right(self):
        self.attems += 1
        self.correct += 1

        print("Це правильна відповідь")
    def got_wrong(self):
        self.attems +=1

class QuestionView():
    def __init__ (self, frm_question, question, ans, wrans1, wrans2, wrans3):
        self.frm_question = frm_question
        self.question_pr = question
        self.ans_rb = ans
        self.wrans1 = wrans1
        self.wrans2 = wrans2
        self.wrans3 = wrans3

    def show(self):
        self.question_pr(self.frm_question.question)
        self.ams_rb.setText(self.frm_question.answer)
        self.wrans1_rb.setText(self.frm_question.wrong_answer1)
        self.wrans2_rb.setText(self.frm_question.wrong_answer2)
        self.wrans3_rb.setText(self.frm_question.wrong_answer3)

    def change(self, new_frm_question):
        self.frm_question = new_frm_question

class QuestionEdit(QuestionView):
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_connects()
    def save_question(self):
        ''' сохраняет текст вопроса '''
        self.frm_model.question = self.question.text() # копируем данные из виджета в объект
    def save_answer(self):
        ''' сохраняет текст правильного ответа '''
        self.frm_model.answer = self.answer.text() # копируем данные из виджета в объект
    def save_wrong(self):
        ''' сохраняет все неправильные ответы '''
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()
    def set_connects(self):
        ''' устанавливает обработки событий в виджетах так, чтобы сохранять данные '''
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong) 
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)


def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    '''возвращает новый экземпляр класса AnswerCheck, 
    со случайным вопросом и случайным разбросом ответов по виджетам'''
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result)
    return frm_card


        