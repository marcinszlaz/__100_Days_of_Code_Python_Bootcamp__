#todo zadawanie pytań użytkownikowi
#todo sprzwdzanie czy odpowiedz jest prawidłowa
#todo sprawdzanie czy to już koniec quizu
# czyli pewnie lecimy po kolei z wszystkimi obiektami w bank_question xD

class QuizBrain:

    # question_list: object
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.correct_answers = 0

    def next_question(self):
        self.question_number += 1
        print(f'Q.{self.question_number}: {self.question_list[self.question_number-1].text} {self.question_list[self.question_number-1].answer}. (True/False)?: ')

    def is_answer_valid(self):
        choice = input('')
        if choice.lower() == f'{(self.question_list[self.question_number-1].answer).lower()}':
            print('You got it !')
            print(f'The correct answer is: {self.question_list[self.question_number-1].answer}')
            self.correct_answers +=1
            print(f'Your current score is: {self.correct_answers}/{self.question_number}\n')
        elif choice != f'{self.question_list[self.question_number-1].answer}':
            print('Odpowiedz niepoprawna !')
            print(f'The correct answer was: {self.question_list[self.question_number-1].answer}')
            print(f'Your current score is: {self.correct_answers}/{self.question_number}\n')
        else:
            print('You\'ve typed invalid input (True/False only) !')

    def still_has_questions(self):
        return (self.question_number < len(self.question_list))


        # if self.question_number <= len(self.question_list): poprawne ale to noob version, funkcja ma zwracac prawde
        #         return True # albo fałsz więc wystarczy jedna linijka od razu z return, już kiedyś gdzieś to widziałem
        #     else:
        #         return False

# lista = [1,2,3]
# test = QuizBrain(lista)
# print(len(test.question_list))
# print((test.question_number <= len(test.question_list)))