class Questions:
     '''
     The questions for the quiz
     hindi na gagawa ng list for the question, because we'll be creating a new instance of the Question class per question na sasagutin. tama ba?
     '''

     def __init__(self, question_text, answer, correct_answers):
          self.questionText = question_text                      # string
          self.__questionAnswer = answer                         # string
          self.__correctAnswer = correct_answers or []           # string <list> or depende sa sagot
          if correct_answers not in self.__questionAnswer:
               raise ValueError (f"Wrong answer! The answer was: ", self.__correctAnswer  )

          # this might need to change once the methods are implemented, lalo na kapag may update method

     

