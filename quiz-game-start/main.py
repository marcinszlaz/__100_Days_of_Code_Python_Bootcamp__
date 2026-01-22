from data import question_data, question_data1
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
question_bank_dict = {}

# for text in question_data: # tu masz zwykla liste z wartosciami po przecinku
#     question = Question(text['text'],text['answer'])
#     question_bank+=(question.text, question.answer)
#     # print(question.text, question.answer)

# for text in question_data: # a tu masz liste z tuple index 0 tuple pytanie i odpowiedz
#     question = Question(text['text'],text['answer'])
#     question_bank.append((question.text, question.answer))
#     question_bank_dict['Question'] = (question_bank)

# for text in question_data: # robimy listę słowników
#     question = Question(text['text'],text['answer'])
#     question_bank_dict['Question'] = (question.text, question.answer)
#     question_bank.append(question_bank_dict)

# ale jej chodziło właśnie o listę obiektów, samych obiektów, pewnie po to, żeby potem dobierać się do pytania,
# odpowiedzi przez kropkę, question.answer, question.text itp
# CZYLI xD:

# for text in question_data: # tutaj do listy wpisujesz obiekty klasy Question(), każdy obiekt inicjalizuje się sam
#     # w innym miejscu w pamieci, nie ma tak jak z zmienną, że każdy obieg pętli nadpisuje adres w pamięci gdzie
#     # przetrzymywana jest zawartosc zmiennej
#     question = Question(text['text'],text['answer'])
#     question_bank.append(question)

for text in question_data1: # tutaj do listy wpisujesz obiekty klasy Question(), każdy obiekt inicjalizuje się sam
    # w innym miejscu w pamieci, nie ma tak jak z zmienną, że każdy obieg pętli nadpisuje adres w pamięci gdzie
    # przetrzymywana jest zawartosc zmiennej
    question = Question(text['question'],text['correct_answer'])
    question_bank.append(question)


# print('question_bank list: ',question_bank)
# print('question_bank type',type(question_bank))
# print('question_bank index 0 type',type(question_bank[0]))
# print('question_bankd_dict, to jest tylko zmienna temporary',question_bank_dict)
# print(brain_quiz)
# print('question_bank index 0 text/answer',question_bank[0].text, question_bank[0].answer )

brain_quiz = QuizBrain(question_bank)

while brain_quiz.still_has_questions():
    brain_quiz.next_question()
    brain_quiz.is_answer_valid()
print('You\'ve completed the quiz !')
print(f'Your final score is: {brain_quiz.correct_answers}/{len(brain_quiz.question_list)}')