class Questions:
     '''
     The questions for the quiz
     hindi na gagawa ng list for the question, because we'll be creating a new instance of the Question class per question na sasagutin. tama ba?
     '''

     def __init__(self, question_text, answer, correct_answers, category):
          self.question_text = question_text                     # string
          self.__answer = answer                                 # string
          self.__correct_answers = correct_answers or []         # string <list> or depende sa sagot
          self.__category = category                             # string, this part allows the users to pick a category to play on
          
          """
          # this line of code could be reserved for main.py

          if correct_answers not in self.__answer:
               raise ValueError (f"Wrong answer! The answer was: ", self.__correct_answers  )
          """

     def get_question_text(self):
          ''' Returns the question text of the game. '''
          return self.question_text
     
     def get_answer (self):
          ''' Returns the answer of the game. '''
          return self.__answer
     
     def get_correct_answers (self):
          ''' Returns the correct answers of the game. '''
          return self.__correct_answers

     def get_category (self):
          ''' Returns the category of the game. '''
          return self.__category

class PopCultureQuestions (Questions):
    '''
    Represents a Pop Culture Questions in the trivia game.
    Inherits from the Question class and returns category as "Pop Culture"
    '''
    def __init__(self, question_text, answers, correct_answer):
        super().__init__(question_text, answers, correct_answer, category="Pop Culture")
                         
class AnimeQuestions (Questions):
    '''
    Represents a Anime Questions in the trivia game.
    Inherits from the Question class and returns category as "Anime"
    '''
    def __init__(self, question_text, answers, correct_answer):
        super().__init__(question_text, answers, correct_answer, category="Anime")

class GameQuestions (Questions):
    '''
    Represents a Game Questions in the trivia game.
    Inherits from the Question class and returns category as "Game"
    '''
    def __init__(self, question_text, answers, correct_answer):
        super().__init__(question_text, answers, correct_answer, category="Game")


''' This segment just tests one of the subclasses! It works naman on my end so if ever move na toh kay main.py she works >:3 '''

test = PopCultureQuestions(question_text="Ayie", answers="A", correct_answer="B")

print(test.get_category())                   # returns as Pop Culture
print(test.get_question_text())              # returns as Ayie
print(test.get_answer())                     # returns as A
print(test.get_correct_answers())            # returns as B
