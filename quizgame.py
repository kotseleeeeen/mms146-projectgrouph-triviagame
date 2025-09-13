from questions import * #Import * means to import all classes under the questions.py file
import random

#removed dataset from here since nandoon na siya sa main.py

class QuizGame:
    def __init__(self):
        self.__question_bank = []
        self.__score = 0

    def add_question(self, question_object):
        self.__question_bank.append(question_object)

    def get_score(self):
        return self.__score
    #Opted to use method calls to access non-subscriptable objects
    def load_from_nested_dict(self, nested):                                        #gives the structure (nested dictionary) for the needed content for questions
        for category, subcats in nested.items():                                    #loops through categories, then subcategories, then each question
            for subcategory, questions in subcats.items():                   
                for q in questions:
                    if isinstance(q, Questions):                                    #handling questions for created Questions objects using the Question class
                        self.__question_bank.append({
                            "question_text": q.get_question_text(),
                            "answers": q.get_answer(),
                            "correct_answer": q.get_correct_answers(),
                            "category": q.get_category(),
                            "subcategory": q.get_subcategory(),
                        })
                    else:
                        self.__question_bank.append({                               #handling questions for created Questions objects from provided dictionary
                            "question_text": q["question"],
                            "answers": q["options"],
                            "correct_answer": q["answer"],
                            "category": category,
                            "subcategory": subcategory,
                        })
    
    def display_question(self, index):
        '''
        Returns question and its multiple choice answers
        '''
        if index < 0 or index >= len(self.__question_bank):                         #check if index (inputted value = the questions) is a valid option. if not, return none
            return None, []
        
        q = self.__question_bank[index]                                             #retrieves question from the question bank, as appended above

        if isinstance(q, dict):                                                     #extract question text and answers
            question_text = q["question_text"]
            answers = q["answers"]
        else:
            question_text = q.get_question_text()
            answers = q.get_answer()
        
        print ("\n" + question_text)                                                #print question and question choices
        letters = ["a", "b", "c", "d"]                                              #assigning the a,b,c,d labels to the multiple choice answers
        for i, option in enumerate (answers):                                       #loop to only print 4 options
            if i < len(letters):
                print(f"{letters[i]}) {option}")
        
        return question_text, answers
    
    def check_answer(self, index, player_answer):                       
        if index < 0 or index >= len(self.__question_bank):
            return False
        
        q = self.__question_bank[index]

        if isinstance(q, dict):                                                     #gets correct answer from the dictionary
            correct = q["correct_answer"]
            answers = q["answers"]
        else:
            correct = q.get_correct_answers()                                       #gets correct answer from the question class
            if isinstance(correct, list):
                correct = correct[0] if correct else ""
            answers = q.get_answer()

        letters = ["a", "b", "c", "d"]
        '''
        Allows user to input a, b, c, or d as their answer if they don't want to type the full answer.
        '''
        guess = player_answer.strip().lower()                                       #takes the player's input, strips it of extra spaces and makes it case-insensitive
        if guess in letters:                                                        #if the player answers just one of the letters, it's converted to its full text corresponding to the index in answers
            idx = letters.index(guess)
            if idx < len(answers):                                                  #error handling
                player_answer = answers[idx]

        is_ok = player_answer.strip().lower() == str(correct).strip().lower()       #compare above result with correct answer
        if is_ok:
            self.__score += 1
        return is_ok

    def shuffle_question_bank(self):
        '''
        Shuffles so the player doesn't know what to expect each time they play
        '''
        random.shuffle(self.__question_bank)

    def reset_game(self):
        self.__score = 0

