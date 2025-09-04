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
    def load_from_nested_dict(self, nested): 
        for category, subcats in nested.items():
            for subcategory, questions in subcats.items():
                for q in questions:
                    if isinstance(q, Questions):
                        self.__question_bank.append({
                            "question_text": q.get_question_text(),
                            "answers": q.get_answer(),
                            "correct_answer": q.get_correct_answers(),
                            "category": q.get_category(),
                            "subcategory": q.get_subcategory(),
                        })
                    else:
                        self.__question_bank.append({
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
        if index < 0 or index >= len(self.__question_bank):
            return None, []
        
        q = self.__question_bank[index]

        if isinstance(q, dict):
            question_text = q["question_text"]
            answers = q["answers"]
        else:
            question_text = q.get_question_text()
            answers = q.get_answer()
        
        print ("\n" + question_text)
        letters = ["a", "b", "c", "d"]
        for i, option in enumerate (answers):
            if i < len(letters):
                print(f"{letters[i]}) {option}")
        
        return question_text, answers
    
    def check_answer(self, index, player_answer):
        if index < 0 or index >= len(self.__question_bank):
            return False
        
        q = self.__question_bank[index]

        if isinstance(q, dict):
            correct = q["correct_answer"]
            answers = q["answers"]
        else:
            correct = q.get_correct_answers()
            if isinstance(correct, list):
                correct = correct[0] if correct else ""
            answers = q.get_answer()

        letters = ["a", "b", "c", "d"]
        '''
        Allows user to input a, b, c, or d as their answer if they don't want to type the full answer.
        '''
        guess = player_answer.strip().lower()
        if guess in letters:
            idx = letters.index(guess)
            if idx < len(answers):
                player_answer = answers[idx]

        is_ok = player_answer.strip().lower() == str(correct).strip().lower()
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

