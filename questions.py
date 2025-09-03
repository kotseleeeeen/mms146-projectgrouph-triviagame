'''
FINAL PROJECT: Text-Based Quiz/Trivia Game

Submitted by: PROJECT GROUP H
Mary Christen Gemel Tolentino
Dylan Isaac Vela
Ann Carleen Gaile Cuevas
Aria Carmela De Vera
Ryan Jay Buenaventura
Megan Isabel Sharpe

Submitted to:
Asst. Prof. Katrina Joy M. Abriol-Santos

Text-Based Trivia Game: Questions Module
This class represents the questions module of the Trivia Game
'''

# ---------------
# Questions Class 
# ---------------

class Questions:
     '''
     Represents questions in the Text-Based Trivia Game
     '''

     def __init__(self, question_text, answer, correct_answers, category, subcategory):
          '''
          Initializes a new instance of the Questions class.
        
          Parameters:
          question_text: The question text of the Trivia Game             
          answer: The answer to the question in the Trivia Game
          correct_answers: The correct answers to the question in the Trivia Game
          category: The category of the questions in the Trivia Game
          subcategory: The subcategory of questions in the Trivia Game
          '''
          
          self.question_text = question_text                     # string attribute
          self.__answer = answer                                 # string attribute
          self.__correct_answers = correct_answers               # string attribute
          self.__category = category                             # string attribute
          self.__subcategory = subcategory or []                 # string attribute or list (depending on the listed subcategories)
          
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

     def get_subcategory(self):
          ''' Returns the subcategory of the question.'''
          return self.__subcategory

#Adjusted to prevent missmatching keywords | Added 'subcategory' as a parameter | applicable to all 'Questions' subclass
class PopCultureQuestions (Questions):
    '''
    Represents Pop Culture Questions in the trivia game.
    Inherits from the Question class and returns category as "Pop Culture"
    '''
    def __init__(self, question_text, answer, correct_answers, subcategory):
         # the super function allows the PopCultureQuestions to inherit all the methods and attributes of the Questions class
        super().__init__(question_text, answer, correct_answers, category="Pop Culture", subcategory=subcategory)
                         
class AnimeQuestions (Questions):
    '''
    Represents Anime Questions in the trivia game.
    Inherits from the Question class and returns category as "Anime"
    '''
    def __init__(self, question_text, answer, correct_answers, subcategory):
         # the super function allows the AnimeQuestions to inherit all the methods and attributes of the Questions class
        super().__init__(question_text, answer, correct_answers, category="Anime", subcategory=subcategory)

class GameQuestions (Questions):
    '''
    Represents Game Questions in the trivia game.
    Inherits from the Question class and returns category as "Game"
    '''
    def __init__(self, question_text, answer, correct_answers, subcategory):
         # the super function allows the GameQuestions to inherit all the methods and attributes of the Questions class
        super().__init__(question_text, answer, correct_answers, category="Game", subcategory=subcategory)

